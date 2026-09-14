"""Command-line interface for Ghost Bus Tracker."""

import argparse
import json
import logging
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
    except Exception:
        pass


def run_scan(args: argparse.Namespace) -> int:
    """Executes a scan of GTFS-RT feeds and computes reliability metrics."""
    fetcher = FeedFetcher()
    analyzer = ReliabilityAnalyzer(agency_name=args.agency or config.AGENCY_NAME)
    reporter = ReportGenerator(
        latest_path=Path(args.latest_file) if args.latest_file else config.LATEST_FILE,
        history_path=Path(args.history_file) if args.history_file else config.HISTORY_FILE,
        report_path=Path(args.report_file) if args.report_file else config.REPORT_FILE,
    )

    try:
        if getattr(args, "sample", False):
            vp_src = args.vp_feed or config.SAMPLE_VP_FILE
            tu_src = args.tu_feed or config.SAMPLE_TU_FILE
            logger.info("Using sample/offline feeds:")
            logger.info(f"  Vehicle Positions: {vp_src}")
            logger.info(f"  Trip Updates:      {tu_src}")
            vehicles, v_ts = fetcher.fetch_vehicle_positions(vp_src)
            trips, t_ts = fetcher.fetch_trip_updates(tu_src)
            feed_ts = t_ts or v_ts
        else:
            vp_src = args.vp_feed or config.VEHICLE_POSITIONS_URL
            tu_src = args.tu_feed or config.TRIP_UPDATES_URL
            logger.info(f"Fetching live feeds from {vp_src} & {tu_src}...")
            try:
                vehicles, v_ts = fetcher.fetch_vehicle_positions(vp_src)
                trips, t_ts = fetcher.fetch_trip_updates(tu_src)
                feed_ts = t_ts or v_ts
            except Exception as e:
                if args.fallback_sample:
                    logger.warning(f"Live feed fetch failed ({e}). Falling back to sample data...")
                    vehicles, trips, feed_ts = fetcher.load_sample_feeds()
                else:
                    raise

        # Run analysis
        snapshot = analyzer.analyze(vehicles, trips, feed_timestamp=feed_ts)

        # Output / Save
        if args.save:
            saved_json = reporter.save_latest_json(snapshot)
            history = reporter.update_history_json(snapshot)
            logger.info(f"Metrics saved to {saved_json}")
        else:
            history = None

        if args.report or args.save:
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
    scan_p.add_argument("--live", action="store_true", help="Fetch live feeds from network (default)")
    scan_p.add_argument("--sample", "--mock", dest="sample", action="store_true", help="Use local sample feeds")
    scan_p.add_argument("--vp-feed", type=str, help="Custom URL or file path for vehicle positions")
    scan_p.add_argument("--tu-feed", type=str, help="Custom URL or file path for trip updates")
    scan_p.add_argument("--agency", type=str, help="Transit agency name")
    scan_p.add_argument("--save", action="store_true", help="Save metrics to data/latest.json and update history.json")
    scan_p.add_argument("--report", action="store_true", help="Generate or update RELIABILITY.md")
    scan_p.add_argument("--quiet", action="store_true", help="Do not print terminal scorecard")
    scan_p.add_argument("--fallback-sample", action="store_true", default=True, help="Fallback to sample feed if network fails")
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
    elif args.command == "report":
        return run_report(args)
    elif args.command == "summary":
        return run_summary(args)
    else:
        parser.print_help()
        return 1


if __name__ == "__main__":
    sys.exit(main())
