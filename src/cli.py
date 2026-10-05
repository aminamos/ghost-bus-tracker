"""Command-line interface for Ghost Bus Tracker."""

import argparse
import json
import logging
import os
import sys
from pathlib import Path
from typing import Optional

from src import __version__, config
from src.analyzer import ReliabilityAnalyzer
from src.fetcher import FeedFetcher
from src.models import ReliabilitySnapshot
from src.reporter import ReportGenerator

logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")
logger = logging.getLogger("ghost-bus-tracker")

# Ensure UTF-8 output on Windows consoles
if hasattr(sys.stdout, "reconfigure"):
    try:
        sys.stdout.reconfigure(encoding="utf-8", errors="replace")
        sys.stderr.reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # pragma: no cover
        pass


def run_scan(args: argparse.Namespace) -> int:
    """Executes a scan of GTFS-RT feeds and computes reliability metrics."""
    fetcher = FeedFetcher()

    preset = None
    if getattr(args, "preset", None):
        preset = config.get_preset(args.preset)
        if not preset:
            logger.error(
                f"Unknown preset '{args.preset}'. Available presets: {', '.join(config.AGENCY_PRESETS.keys())}. "
                f"Run 'ghost-bus presets' to see all supported cities."
            )
            return 1

    agency_name = getattr(args, "agency", None) or (preset["agency"] if preset else config.AGENCY_NAME)
    city_name = getattr(args, "city", None) or (preset["city"] if preset else config.CITY_NAME)
    transit_system = getattr(args, "transit_system", None) or (preset["name"] if preset else config.TRANSIT_SYSTEM)
    region_name = getattr(args, "region", None) or (preset["region"] if preset else config.REGION_NAME)
    state_name = (preset["state"] if preset else config.STATE_NAME)
    country_name = (preset["country"] if preset else config.COUNTRY_NAME)

    analyzer = ReliabilityAnalyzer(
        agency_name=agency_name,
        city_name=city_name,
        transit_system=transit_system,
        region_name=region_name,
        state_name=state_name,
        country_name=country_name,
    )
    reporter = ReportGenerator(
        latest_path=Path(args.latest_file) if args.latest_file else config.LATEST_FILE,
        history_path=Path(args.history_file) if args.history_file else config.HISTORY_FILE,
        report_path=Path(args.report_file) if args.report_file else config.REPORT_FILE,
    )
    if getattr(args, "live", False) and getattr(args, "sample", False):
        logger.error("Pass only one of --live or --sample, not both.")
        return 1

    try:
        source = "live"
        used_fallback = False
        if getattr(args, "sample", False):
            if preset and preset.get("id") != "twin-cities" and not getattr(args, "vp_feed", None) and not getattr(args, "tu_feed", None):
                logger.warning(
                    f"Sample bundle holds Twin Cities feeds, so --preset {preset['id']} labels are not applied. "
                    "Snapshot is labeled Twin Cities with source=sample. Pass --vp-feed/--tu-feed for real city data."
                )
                agency_name = getattr(args, "agency", None) or config.AGENCY_NAME
                city_name = getattr(args, "city", None) or config.CITY_NAME
                transit_system = getattr(args, "transit_system", None) or config.TRANSIT_SYSTEM
                region_name = getattr(args, "region", None) or config.REGION_NAME
                state_name = config.STATE_NAME
                country_name = config.COUNTRY_NAME
                analyzer = ReliabilityAnalyzer(
                    agency_name=agency_name,
                    city_name=city_name,
                    transit_system=transit_system,
                    region_name=region_name,
                    state_name=state_name,
                    country_name=country_name,
                )
            vp_src = args.vp_feed or config.SAMPLE_VP_FILE
            tu_src = args.tu_feed or config.SAMPLE_TU_FILE
            logger.info("Using sample/offline feeds:")
            logger.info(f"  Vehicle Positions: {vp_src}")
            logger.info(f"  Trip Updates:      {tu_src}")
            vehicles, v_ts = fetcher.fetch_vehicle_positions(vp_src)
            trips, t_ts = fetcher.fetch_trip_updates(tu_src)
            feed_ts = t_ts or v_ts
            source = "sample"
        else:
            vp_src = args.vp_feed or (preset["vp_url"] if preset else config.VEHICLE_POSITIONS_URL)
            tu_src = args.tu_feed or (preset["tu_url"] if preset else config.TRIP_UPDATES_URL)

            # Handle API key if required by preset or provided via CLI / env.
            # Order: --api-key flag, agency variable, shared GTFS_RT_API_KEY.
            api_key = getattr(args, "api_key", None)
            if preset and preset.get("requires_key"):
                api_key = config.resolve_api_key(preset, api_key)

                if api_key:
                    if preset.get("key_param"):
                        sep = "&" if "?" in vp_src else "?"
                        vp_src = f"{vp_src}{sep}{preset['key_param']}={api_key}"
                        sep = "&" if "?" in tu_src else "?"
                        tu_src = f"{tu_src}{sep}{preset['key_param']}={api_key}"
                    elif preset.get("key_header"):
                        fetcher.session.headers.update({preset["key_header"]: api_key})
                else:
                    logger.warning(
                        f"⚠️  {preset['name']} ({preset['city']}) GTFS-RT feed requires an API key from {preset.get('key_url')}."
                    )
                    logger.warning(
                        f"   Pass --api-key <KEY>, set {preset.get('key_env_var')}=<KEY>, or set {config.SHARED_API_KEY_ENV}=<KEY> once for all keyed feeds."
                    )

            logger.info(f"Fetching live feeds for {transit_system} ({city_name})...")
            if api_key:
                logger.info(f"  VP Feed: {vp_src.replace(api_key, '***')}")
                logger.info(f"  TU Feed: {tu_src.replace(api_key, '***')}")
            else:
                logger.info(f"  VP Feed: {vp_src}")
                logger.info(f"  TU Feed: {tu_src}")
            try:
                vehicles, v_ts = fetcher.fetch_vehicle_positions(vp_src)
                trips, t_ts = fetcher.fetch_trip_updates(tu_src)
                feed_ts = t_ts or v_ts
            except Exception as e:
                if getattr(args, "fallback_sample", False):
                    logger.warning(f"Live feed fetch failed ({e}). Falling back to sample data...")
                    vehicles, trips, feed_ts = fetcher.load_sample_feeds()
                    source = "sample"
                    used_fallback = True
                else:
                    raise

        # Run analysis
        snapshot = analyzer.analyze(vehicles, trips, feed_timestamp=feed_ts)
        snapshot.source = source

        # Sample data pulled in as an implicit fallback must never land in
        # committed artifacts — latest.json, history.json, RELIABILITY.md all
        # get committed by the track workflow. Explicit --sample saves are fine
        # (they're marked source="sample"), but a failed live fetch should
        # leave the last real data untouched.
        if args.save:
            if used_fallback:
                logger.warning("Skipping --save: fallback sample data is never persisted to the metrics store")
                history = None
            else:
                saved_json = reporter.save_latest_json(snapshot)
                history = reporter.update_history_json(snapshot)
                logger.info(f"Metrics saved to {saved_json}")
        else:
            history = None

        if args.report or args.save:
            if used_fallback:
                logger.warning("Skipping report write: snapshot is sample fallback data")
            else:
                saved_report = reporter.write_markdown_report(snapshot, history)
                logger.info(f"Dashboard updated at {saved_report}")

        if not args.quiet:
            print("\n" + reporter.generate_console_summary(snapshot) + "\n")

        return 0
    except Exception as e:
        logger.error(f"Scan failed: {e}", exc_info=args.debug)
        return 1


def run_report(args: argparse.Namespace) -> int:
    """Generates Markdown report from existing or fresh snapshot."""
    input_path = Path(args.input) if args.input else config.LATEST_FILE
    output_path = Path(args.output) if args.output else config.REPORT_FILE
    history_path = Path(args.history) if args.history else config.HISTORY_FILE

    reporter = ReportGenerator(
        latest_path=input_path,
        history_path=history_path,
        report_path=output_path,
    )

    if not input_path.is_file():
        logger.warning(f"Snapshot not found at {input_path}. Running quick scan first...")
        scan_args = argparse.Namespace(
            sample=False,
            mock=False,
            vp_feed=None,
            tu_feed=None,
            agency=None,
            save=True,
            report=True,
            quiet=True,
            fallback_sample=True,
            latest_file=str(input_path),
            history_file=str(history_path),
            report_file=str(output_path),
            debug=False,
        )
        return run_scan(scan_args)

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        snapshot = ReliabilitySnapshot(**data)

        history = None
        if history_path.is_file():
            try:
                with open(history_path, "r", encoding="utf-8") as f:
                    history = json.load(f)
            except Exception:
                pass

        target = reporter.write_markdown_report(snapshot, history, output_path=output_path)
        logger.info(f"Report generated successfully at {target}")
        return 0
    except Exception as e:
        logger.error(f"Failed to generate report: {e}")
        return 1


def run_summary(args: argparse.Namespace) -> int:
    """Prints a quick summary scorecard of transit reliability."""
    input_path = Path(args.input) if args.input else config.LATEST_FILE
    reporter = ReportGenerator()

    if not input_path.is_file():
        logger.error(f"No snapshot found at {input_path}. Run 'ghost-bus scan --save' first.")
        return 1

    try:
        with open(input_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        snapshot = ReliabilitySnapshot(**data)
        print("\n" + reporter.generate_console_summary(snapshot) + "\n")
        return 0
    except Exception as e:
        logger.error(f"Failed to load summary: {e}")
        return 1


def run_presets(args: argparse.Namespace) -> int:
    """Lists all built-in city transit agency presets."""
    print("=" * 70)
    print(" 🏙️ GHOST BUS TRACKER: BUILT-IN TRANSIT AGENCY PRESETS")
    print("=" * 70)
    for p_id, p in config.AGENCY_PRESETS.items():
        key_status = (
            "Open (No key required)"
            if not p.get("requires_key")
            else f"Requires API Key (env: {p.get('key_env_var')}, register at {p.get('key_url')})"
        )
        print(f"\n[{p['id'].upper()}] - {p['name']} ({p['city']})")
        print(f"  Agency:      {p['agency']}")
        print(f"  Region:      {p['region']}")
        print(f"  Access:      {key_status}")
        print(f"  Description: {p['description']}")
        print(f"  VP Feed:     {p['vp_url']}")
        print(f"  TU Feed:     {p['tu_url']}")
        print(f"  Scan Cmd:    ghost-bus scan --preset {p['id']}")
    print("\n" + "=" * 70)
    return 0


def run_scan_all(args: argparse.Namespace) -> int:
    """Scans every (or selected) preset, writing per-city JSON and Markdown."""
    if getattr(args, "sample", False):
        logger.error("--sample holds only Twin Cities data and cannot back scan-all.")
        return 1

    if getattr(args, "presets", None):
        ids = [p.strip() for p in args.presets.split(",") if p.strip()]
    else:
        ids = list(config.AGENCY_PRESETS.keys())

    ok, failed, skipped = [], [], []
    for pid in ids:
        preset = config.get_preset(pid)
        if not preset:
            logger.error(f"Unknown preset '{pid}'. Skipping.")
            failed.append(pid)
            continue
        if preset.get("requires_key") and not config.resolve_api_key(preset, getattr(args, "api_key", None)):
            logger.warning(f"Skipping {pid}: set {preset.get('key_env_var')} or {config.SHARED_API_KEY_ENV} to scan it.")
            skipped.append(pid)
            continue
        city_args = argparse.Namespace(
            preset=preset["id"],
            api_key=getattr(args, "api_key", None),
            vp_feed=None,
            tu_feed=None,
            agency=None,
            city=None,
            transit_system=None,
            region=None,
            live=True,
            sample=False,
            save=True,
            report=True,
            quiet=True,
            fallback_sample=getattr(args, "fallback_sample", False),
            latest_file=str(config.DATA_DIR / "latest" / f"{preset['id']}.json"),
            history_file=str(config.DATA_DIR / "history" / f"{preset['id']}.json"),
            report_file=str(config.BASE_DIR / f"RELIABILITY-{preset['id']}.md"),
            debug=getattr(args, "debug", False),
        )
        code = run_scan(city_args)
        (ok if code == 0 else failed).append(pid)
        logger.info(f"scan-all {preset['id']}: {'ok' if code == 0 else 'FAILED'}")

    print(f"scan-all: {len(ok)} ok, {len(failed)} failed, {len(skipped)} skipped (no key)")
    return 1 if failed else 0


def build_parser() -> argparse.ArgumentParser:
    """Builds CLI argument parser."""
    parser = argparse.ArgumentParser(
        prog="ghost-bus",
        description="Ghost Bus Tracker: Automated public transit reliability and ghost bus tracker.",
    )
    parser.add_argument(
        "--version", action="version", version=f"%(prog)s {__version__}"
    )

    subparsers = parser.add_subparsers(dest="command", help="Available subcommands")

    # scan subcommand
    scan_p = subparsers.add_parser("scan", help="Fetch feeds and analyze transit reliability")
    scan_p.add_argument("--live", action="store_true", help="Fetch live feeds from network (default when --sample is absent)")
    scan_p.add_argument("--sample", "--mock", dest="sample", action="store_true", help="Use bundled Twin Cities sample feeds (labels stay Twin Cities)")
    scan_p.add_argument(
        "--preset",
        type=str,
        help="Use built-in city/agency preset (e.g. chicago, cta, boston, mbta, twin-cities, nyc)",
    )
    scan_p.add_argument(
        "--api-key",
        type=str,
        help="API key for feeds that require authentication (e.g. CTA or MTA)",
    )
    scan_p.add_argument("--vp-feed", type=str, help="Custom URL or file path for vehicle positions")
    scan_p.add_argument("--tu-feed", type=str, help="Custom URL or file path for trip updates")
    scan_p.add_argument("--agency", type=str, help="Transit agency name")
    scan_p.add_argument("--city", type=str, help="City / Metropolitan area name")
    scan_p.add_argument("--transit-system", type=str, help="Transit system name")
    scan_p.add_argument("--region", type=str, help="Region name")
    scan_p.add_argument("--save", action="store_true", help="Save metrics to data/latest.json and update history.json")
    scan_p.add_argument("--report", action="store_true", help="Generate or update RELIABILITY.md")
    scan_p.add_argument("--quiet", action="store_true", help="Do not print terminal scorecard")
    scan_p.add_argument("--fallback-sample", dest="fallback_sample", action="store_true", help="Fallback to sample feed if network fails (default: fail loudly)")
    scan_p.add_argument("--no-fallback-sample", dest="fallback_sample", action="store_false", help="Disable fallback to sample feed")
    scan_p.set_defaults(fallback_sample=False)
    scan_p.add_argument("--latest-file", type=str, help="Custom path for latest.json")
    scan_p.add_argument("--history-file", type=str, help="Custom path for history.json")
    scan_p.add_argument("--report-file", type=str, help="Custom path for RELIABILITY.md")
    scan_p.add_argument("--debug", action="store_true", help="Print debug stack traces on error")

    # report subcommand
    report_p = subparsers.add_parser("report", help="Generate Markdown reliability dashboard")
    report_p.add_argument("--input", type=str, help="Input JSON snapshot file (default: data/latest.json)")
    report_p.add_argument("--output", type=str, help="Output Markdown file (default: RELIABILITY.md)")
    report_p.add_argument("--history", type=str, help="History JSON file (default: data/history.json)")

    # summary subcommand
    summary_p = subparsers.add_parser("summary", help="Print quick scorecard from latest snapshot")
    summary_p.add_argument("--input", type=str, help="Input JSON snapshot file (default: data/latest.json)")

    # presets subcommand
    subparsers.add_parser("presets", help="List built-in city transit agency presets (Chicago CTA, Boston MBTA, etc.)")

    # scan-all subcommand
    all_p = subparsers.add_parser("scan-all", help="Scan all city presets, writing per-city snapshots")
    all_p.add_argument("--presets", type=str, help="Comma-separated preset ids (default: all)")
    all_p.add_argument("--fallback-sample", dest="fallback_sample", action="store_true", help="Fallback to sample feed if network fails")
    all_p.add_argument("--no-fallback-sample", dest="fallback_sample", action="store_false", help="Disable fallback to sample feed")
    all_p.set_defaults(fallback_sample=False)
    all_p.add_argument("--debug", action="store_true", help="Print debug stack traces on error")

    return parser


def main(argv: Optional[list] = None) -> int:
    """CLI entrypoint."""
    parser = build_parser()
    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 0

    if args.command == "scan":
        return run_scan(args)
    elif args.command == "scan-all":
        return run_scan_all(args)
    elif args.command == "report":
        return run_report(args)
    elif args.command == "summary":
        return run_summary(args)
    elif args.command == "presets":
        return run_presets(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":  # pragma: no cover
    sys.exit(main())
