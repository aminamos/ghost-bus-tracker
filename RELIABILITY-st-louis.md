# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-18T06:30:19.194000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `73` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `59` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+97.5s` (`+1.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 32 | 43.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 12 | 16.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 4.1% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 19.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19757** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-60.0s` |
| **Route 19780** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 19776** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 19759** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.5 min` |
| **Route 19788** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-90.0s` |
| **Route 19762** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+26.0 min` |
| **Route 19778** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-20.0s` |
| **Route 19750** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 19787** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.3 min` |
| **Route 19785** | 3 | 3 | 0 | **`0.0%`** | `50.0%` | `-30.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19762** | `+26.0 min (+1560.0s)` | `+26.0 min (+1560s)` | 2 | `0.0%` |
| **Route 19781** | `+7.0 min (+420.0s)` | `+7.0 min (+420s)` | 1 | `0.0%` |
| **Route 19793** | `+6.5 min (+390.0s)` | `+14.0 min (+840s)` | 2 | `50.0%` |
| **Route 19754** | `+4.5 min (+270.0s)` | `+5.0 min (+300s)` | 2 | `100.0%` |
| **Route 19787** | `+4.3 min (+260.0s)` | `+8.0 min (+480s)` | 3 | `66.67%` |
| **Route 19789** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19798** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 2 | `100.0%` |
| **Route 19759** | `+3.5 min (+210.0s)` | `+4.0 min (+240s)` | 2 | `100.0%` |
| **Route 19800** | `+3.5 min (+210.0s)` | `+5.0 min (+300s)` | 3 | `100.0%` |
| **Route 19780** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19782** | ~2.0m | ~2.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 19776** | ~5.0m | ~5.0m | **`+0.0 min`** | `70.0 / 100` |
| **Route 19759** | ~1.0m | ~1.0m | **`+0.0 min`** | `50.0 / 100` |
| **Route 19788** | ~4.0m | ~4.0m | **`+0.0 min`** | `87.5 / 100` |
| **Route 19793** | ~1424.0m | ~1424.0m | **`+0.0 min`** | `99.5 / 100` |
| **Route 19778** | ~717.5m | ~717.5m | **`+0.0 min`** | `99.6 / 100` |
| **Route 19750** | ~1406.0m | ~1406.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 19787** | ~705.0m | ~705.0m | **`+0.0 min`** | `99.6 / 100` |
| **Route 19783** | ~1430.0m | ~1430.0m | **`+0.0 min`** | `99.9 / 100` |
| **Route 19785** | ~712.0m | ~712.0m | **`+0.0 min`** | `99.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 06:30:19` | `0.0%` | `66.67%` | 73 | 59 | `+97.5s` |
| `2026-11-18 06:00:27` | `79.78%` | `0.0%` | 89 | 0 | `+0.0s` |
| `2026-11-18 05:30:30` | `0.0%` | `74.07%` | 77 | 70 | `+32.2s` |
| `2026-11-18 05:00:18` | `0.0%` | `73.44%` | 88 | 82 | `+62.8s` |
| `2026-11-18 04:30:19` | `0.0%` | `79.1%` | 90 | 81 | `+81.5s` |
| `2026-11-18 04:00:18` | `0.0%` | `71.62%` | 92 | 92 | `+96.5s` |
| `2026-11-18 03:30:18` | `0.0%` | `66.2%` | 95 | 85 | `+98.9s` |
| `2026-11-18 03:00:19` | `0.0%` | `82.05%` | 95 | 91 | `+103.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T06:30:19.194000+00:00`.*
