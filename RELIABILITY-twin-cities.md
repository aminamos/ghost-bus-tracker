# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T16:34:15.973040+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.45%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.06%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `932` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `751` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `116` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+17.6s` (`+0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-14.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 436 | 46.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 262 | 28.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 48 | 5.2% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 116 | 12.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 65 | 7.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 7 | 3 | 4 | **`57.14%`** | `66.67%` | `+0.4 min` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `66.67%` | `+1.2 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.4 min` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `-37.7s` |
| **Route 540** | 11 | 5 | 4 | **`36.36%`** | `57.14%` | `+0.8 min` |
| **Route 67** | 11 | 4 | 4 | **`36.36%`** | `42.86%` | `+0.3 min` |
| **Route 721** | 11 | 2 | 4 | **`36.36%`** | `42.86%` | `+5.0 min` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `+0.5 min` |
| **Route 827** | 6 | 2 | 2 | **`33.33%`** | `0.0%` | `-149.8s` |
| **Route 18** | 37 | 18 | 12 | **`32.43%`** | `72.0%` | `+1.7 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+6.1 min (+368.9s)` | `+44.4 min (+2663s)` | 7 | `42.86%` |
| **Route 901** | `+5.2 min (+311.2s)` | `+14.0 min (+840s)` | 8 | `50.0%` |
| **Route 721** | `+5.0 min (+298.4s)` | `+14.6 min (+878s)` | 2 | `42.86%` |
| **Route 805** | `+4.8 min (+286.0s)` | `+22.0 min (+1320s)` | 3 | `75.0%` |
| **Route 9** | `+3.1 min (+187.8s)` | `+15.4 min (+922s)` | 7 | `66.67%` |
| **Route 542** | `+3.0 min (+180.0s)` | `+8.3 min (+499s)` | 5 | `71.43%` |
| **Route 902** | `+2.6 min (+155.5s)` | `+6.5 min (+390s)` | 11 | `81.82%` |
| **Route 904** | `+2.4 min (+143.6s)` | `+6.7 min (+401s)` | 9 | `92.31%` |
| **Route 227** | `+1.8 min (+106.7s)` | `+3.5 min (+208s)` | 1 | `100.0%` |
| **Route 18** | `+1.7 min (+102.6s)` | `+13.5 min (+810s)` | 18 | `72.0%` |

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
| `1325819` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326195` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326415` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326498` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326661` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329942` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365498` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365794` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365901` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366842` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331830` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332145` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332560` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333185` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1010128` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 16:34:15` | `12.45%` | `58.06%` | 932 | 751 | `+17.6s` |
| `2026-10-05 12:15:23` | `10.84%` | `63.85%` | 950 | 805 | `+30.8s` |
| `2026-10-05 12:14:27` | `11.02%` | `64.16%` | 944 | 798 | `+31.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T16:34:15.973040+00:00`.*
