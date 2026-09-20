# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-20T21:42:01.381590+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.79%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`67.44%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `679` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `563` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `114` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+174.9s` (`2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+131.5s` (`2.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 379 | 55.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 49 | 7.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 127 | 18.7% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 1.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 114 | 16.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `-7.5s` |
| **Route 538** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.8m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `+0.6m` |
| **Route 64** | 18 | 8 | 7 | **`38.89%`** | `100.0%` | `+1.8m` |
| **Route 18** | 32 | 17 | 12 | **`37.5%`** | `88.89%` | `+1.3m` |
| **Route 540** | 8 | 2 | 3 | **`37.5%`** | `50.0%` | `+2.3m` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `71.43%` | `+3.8m` |
| **Route 921** | 32 | 10 | 11 | **`34.38%`** | `78.95%` | `+2.2m` |
| **Route 11** | 24 | 10 | 8 | **`33.33%`** | `66.67%` | `+4.2m` |
| **Route 46** | 3 | 1 | 1 | **`33.33%`** | `50.0%` | `+3.4m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9** | `+7.7 min (463.4s)` | `+26.6 min (1598s)` | 7 | `50.0%` |
| **Route 54** | `+6.7 min (402.2s)` | `+15.4 min (926s)` | 14 | `35.29%` |
| **Route 645** | `+6.2 min (372.5s)` | `+17.0 min (1022s)` | 2 | `33.33%` |
| **Route 38** | `+6.1 min (366.6s)` | `+11.2 min (674s)` | 7 | `22.22%` |
| **Route 904** | `+5.9 min (354.7s)` | `+11.2 min (675s)` | 8 | `23.08%` |
| **Route 22** | `+5.8 min (346.0s)` | `+20.9 min (1253s)` | 11 | `42.86%` |
| **Route 3** | `+5.7 min (344.9s)` | `+12.5 min (752s)` | 7 | `37.5%` |
| **Route 71** | `+5.1 min (305.7s)` | `+11.4 min (684s)` | 2 | `66.67%` |
| **Route 725** | `+5.0 min (300.0s)` | `+10.9 min (654s)` | 2 | `50.0%` |
| **Route 14** | `+5.0 min (299.6s)` | `+11.0 min (659s)` | 8 | `50.0%` |

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
| `1325087` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325108` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325503` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325875` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325909` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326003` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326165` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326180` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326906` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326975` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319247` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319669` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319916` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349293` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351503` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-20 21:42:01` | `16.79%` | `67.44%` | 679 | 563 | `+174.9s` |
| `2026-09-20 19:11:50` | `19.74%` | `67.57%` | 694 | 555 | `+169.7s` |
| `2026-09-20 16:38:06` | `18.7%` | `69.73%` | 706 | 565 | `+185.1s` |
| `2026-09-20 12:45:08` | `19.49%` | `76.49%` | 513 | 404 | `+116.4s` |
| `2026-09-20 07:50:25` | `0.0%` | `100.0%` | 4 | 4 | `+68.2s` |
| `2026-09-20 02:21:35` | `16.33%` | `70.92%` | 447 | 368 | `+162.2s` |
| `2026-09-19 23:49:14` | `13.98%` | `71.89%` | 615 | 523 | `+139.8s` |
| `2026-09-19 21:56:09` | `17.13%` | `67.68%` | 759 | 622 | `+110.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-20T21:42:01.381590+00:00`.*
