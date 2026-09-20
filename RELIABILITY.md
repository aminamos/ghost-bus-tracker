# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-20T23:42:26.904348+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.89%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `544` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `450` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `79` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+204.9s` (`3.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+127.5s` (`2.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 283 | 52.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 45 | 8.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 113 | 20.8% |
| 🔴 **Severe Delay** | Over 15m late | 9 | 1.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 79 | 14.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 15 | 2.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.9m` |
| **Route 18** | 25 | 10 | 11 | **`44.0%`** | `76.92%` | `+2.2m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `66.67%` | `+2.6m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `-50.7s` |
| **Route 68** | 13 | 7 | 5 | **`38.46%`** | `62.5%` | `+4.9m` |
| **Route 38** | 14 | 6 | 5 | **`35.71%`** | `66.67%` | `+4.9m` |
| **Route 921** | 23 | 7 | 8 | **`34.78%`** | `85.71%` | `+2.2m` |
| **Route 534** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `-78.8s` |
| **Route 17** | 13 | 6 | 4 | **`30.77%`** | `55.56%` | `+4.6m` |
| **Route 64** | 13 | 6 | 4 | **`30.77%`** | `75.0%` | `+2.5m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+11.6 min (696.4s)` | `+45.7 min (2743s)` | 7 | `35.71%` |
| **Route 9** | `+9.2 min (552.6s)` | `+33.6 min (2017s)` | 6 | `28.57%` |
| **Route 54** | `+8.0 min (481.6s)` | `+32.0 min (1921s)` | 11 | `42.86%` |
| **Route 645** | `+7.8 min (468.0s)` | `+19.2 min (1154s)` | 2 | `66.67%` |
| **Route 67** | `+6.9 min (414.8s)` | `+12.8 min (770s)` | 4 | `16.67%` |
| **Route 11** | `+5.2 min (314.3s)` | `+19.3 min (1158s)` | 7 | `60.0%` |
| **Route 3** | `+5.1 min (308.8s)` | `+10.6 min (633s)` | 6 | `55.56%` |
| **Route 38** | `+4.9 min (296.0s)` | `+10.5 min (628s)` | 6 | `66.67%` |
| **Route 68** | `+4.9 min (295.6s)` | `+13.9 min (835s)` | 7 | `62.5%` |
| **Route 345** | `+4.7 min (283.5s)` | `+10.6 min (635s)` | 2 | `75.0%` |

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
| `1325374` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325503` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326161` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1334023` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317958` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1320057` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349363` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349886` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331241` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333050` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1132794` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1320632` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1320936` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333416` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349549` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-20 23:42:26` | `14.52%` | `62.89%` | 544 | 450 | `+204.9s` |
| `2026-09-20 21:42:01` | `16.79%` | `67.44%` | 679 | 563 | `+174.9s` |
| `2026-09-20 19:11:50` | `19.74%` | `67.57%` | 694 | 555 | `+169.7s` |
| `2026-09-20 16:38:06` | `18.7%` | `69.73%` | 706 | 565 | `+185.1s` |
| `2026-09-20 12:45:08` | `19.49%` | `76.49%` | 513 | 404 | `+116.4s` |
| `2026-09-20 07:50:25` | `0.0%` | `100.0%` | 4 | 4 | `+68.2s` |
| `2026-09-20 02:21:35` | `16.33%` | `70.92%` | 447 | 368 | `+162.2s` |
| `2026-09-19 23:49:14` | `13.98%` | `71.89%` | 615 | 523 | `+139.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-20T23:42:26.904348+00:00`.*
