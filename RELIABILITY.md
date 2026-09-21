# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-21T15:12:58.501478+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.57%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.29%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `874` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `679` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `171` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+-9.0s` (`-0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-32.0s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 389 | 44.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 255 | 29.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 33 | 3.8% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 171 | 19.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 24 | 2.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `-58.5s` |
| **Route 921** | 24 | 6 | 12 | **`50.0%`** | `90.0%` | `+1.3m` |
| **Route 723** | 6 | 1 | 3 | **`50.0%`** | `100.0%` | `-41.0s` |
| **Route 10** | 29 | 11 | 14 | **`48.28%`** | `91.67%` | `+0.8m` |
| **Route 11** | 24 | 10 | 11 | **`45.83%`** | `100.0%` | `-53.8s` |
| **Route 64** | 22 | 9 | 10 | **`45.45%`** | `100.0%` | `-67.5s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.2m` |
| **Route 18** | 31 | 14 | 13 | **`41.94%`** | `100.0%` | `-5.7s` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `-36.8s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+5.0 min (297.4s)` | `+19.7 min (1180s)` | 6 | `66.67%` |
| **Route 725** | `+4.0 min (241.0s)` | `+8.2 min (494s)` | 2 | `66.67%` |
| **Route 904** | `+3.2 min (189.5s)` | `+7.3 min (439s)` | 7 | `58.33%` |
| **Route 71** | `+3.1 min (187.3s)` | `+22.6 min (1353s)` | 5 | `75.0%` |
| **Route 721** | `+3.1 min (185.0s)` | `+11.2 min (670s)` | 2 | `66.67%` |
| **Route 5** | `+2.0 min (119.8s)` | `+6.4 min (384s)` | 3 | `75.0%` |
| **Route 542** | `+2.0 min (117.7s)` | `+4.5 min (268s)` | 4 | `100.0%` |
| **Route 9** | `+1.9 min (113.4s)` | `+7.2 min (432s)` | 6 | `83.33%` |
| **Route 902** | `+1.6 min (98.2s)` | `+7.0 min (420s)` | 11 | `90.91%` |
| **Route 54** | `+1.5 min (88.8s)` | `+8.4 min (505s)` | 11 | `80.0%` |

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
| `1324991` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325090` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325475` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326022` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326229` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326262` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326324` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326472` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326520` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326700` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326706` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326774` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326947` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330840` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317937` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-21 15:12:58` | `19.57%` | `57.29%` | 874 | 679 | `+-9.0s` |
| `2026-09-21 08:05:04` | `0.0%` | `53.85%` | 13 | 13 | `+-52.1s` |
| `2026-09-20 23:42:26` | `14.52%` | `62.89%` | 544 | 450 | `+204.9s` |
| `2026-09-20 21:42:01` | `16.79%` | `67.44%` | 679 | 563 | `+174.9s` |
| `2026-09-20 19:11:50` | `19.74%` | `67.57%` | 694 | 555 | `+169.7s` |
| `2026-09-20 16:38:06` | `18.7%` | `69.73%` | 706 | 565 | `+185.1s` |
| `2026-09-20 12:45:08` | `19.49%` | `76.49%` | 513 | 404 | `+116.4s` |
| `2026-09-20 07:50:25` | `0.0%` | `100.0%` | 4 | 4 | `+68.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-21T15:12:58.501478+00:00`.*
