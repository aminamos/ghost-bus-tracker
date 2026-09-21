# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-21T23:25:41.158521+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.03%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`53.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `825` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `666` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `124` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+13.2s` (`0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-21.5s` (`-0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 353 | 42.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 260 | 31.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 47 | 5.7% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 124 | 15.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 35 | 4.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 25** | 5 | 1 | 4 | **`80.0%`** | `100.0%` | `+2.2m` |
| **Route 10** | 26 | 8 | 15 | **`57.69%`** | `100.0%` | `-79.6s` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `-66.7s` |
| **Route 17** | 18 | 9 | 7 | **`38.89%`** | `100.0%` | `-45.0s` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `50.0%` | `-62.6s` |
| **Route 18** | 26 | 13 | 9 | **`34.62%`** | `50.0%` | `+2.9m` |
| **Route 64** | 21 | 11 | 7 | **`33.33%`** | `91.67%` | `+3.0m` |
| **Route 65** | 9 | 4 | 3 | **`33.33%`** | `33.33%` | `+2.9m` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `-39.8s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+3.9 min (233.4s)` | `+13.4 min (804s)` | 9 | `46.15%` |
| **Route 542** | `+3.0 min (180.7s)` | `+5.4 min (326s)` | 6 | `66.67%` |
| **Route 64** | `+3.0 min (180.1s)` | `+29.7 min (1780s)` | 11 | `91.67%` |
| **Route 65** | `+2.9 min (176.7s)` | `+15.8 min (950s)` | 4 | `33.33%` |
| **Route 18** | `+2.9 min (172.6s)` | `+39.1 min (2346s)` | 13 | `50.0%` |
| **Route 923** | `+2.7 min (161.5s)` | `+14.4 min (866s)` | 10 | `71.43%` |
| **Route 921** | `+2.3 min (136.7s)` | `+7.5 min (449s)` | 10 | `82.35%` |
| **Route 768** | `+2.3 min (136.0s)` | `+2.3 min (136s)` | 1 | `100.0%` |
| **Route 25** | `+2.2 min (132.0s)` | `+2.2 min (132s)` | 1 | `100.0%` |
| **Route 902** | `+2.2 min (130.0s)` | `+7.0 min (420s)` | 9 | `75.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `1325186` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325594` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325648` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325715` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325784` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325809` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325924` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326110` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326327` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326499` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326527` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326726` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-21 23:25:41` | `15.03%` | `53.0%` | 825 | 666 | `+13.2s` |
| `2026-09-21 20:03:32` | `17.78%` | `59.44%` | 1108 | 864 | `+35.0s` |
| `2026-09-21 15:12:58` | `19.57%` | `57.29%` | 874 | 679 | `+-9.0s` |
| `2026-09-21 08:05:04` | `0.0%` | `53.85%` | 13 | 13 | `+-52.1s` |
| `2026-09-20 23:42:26` | `14.52%` | `62.89%` | 544 | 450 | `+204.9s` |
| `2026-09-20 21:42:01` | `16.79%` | `67.44%` | 679 | 563 | `+174.9s` |
| `2026-09-20 19:11:50` | `19.74%` | `67.57%` | 694 | 555 | `+169.7s` |
| `2026-09-20 16:38:06` | `18.7%` | `69.73%` | 706 | 565 | `+185.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-21T23:25:41.158521+00:00`.*
