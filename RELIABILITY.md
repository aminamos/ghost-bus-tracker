# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-03T21:33:49.938869+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.32%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.11%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `751` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `665` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `85` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+156.0s` (`2.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+92.0s` (`1.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 433 | 57.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 98 | 13.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 121 | 16.1% |
| 🔴 **Severe Delay** | Over 15m late | 13 | 1.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 85 | 11.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.1m` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `+2.3m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.7m` |
| **Route 540** | 8 | 2 | 3 | **`37.5%`** | `100.0%` | `+0.8m` |
| **Route 67** | 11 | 4 | 4 | **`36.36%`** | `85.71%` | `+2.2m` |
| **Route 68** | 24 | 12 | 8 | **`33.33%`** | `81.82%` | `+1.2m` |
| **Route 65** | 9 | 5 | 3 | **`33.33%`** | `80.0%` | `+1.6m` |
| **Route 645** | 6 | 2 | 2 | **`33.33%`** | `25.0%` | `+8.1m` |
| **Route 25** | 7 | 3 | 2 | **`28.57%`** | `50.0%` | `+2.7m` |
| **Route 924** | 36 | 19 | 10 | **`27.78%`** | `69.57%` | `+3.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 38** | `+10.1 min (605.2s)` | `+43.8 min (2630s)` | 6 | `50.0%` |
| **Route 645** | `+8.1 min (483.2s)` | `+16.1 min (964s)` | 2 | `25.0%` |
| **Route 27** | `+6.7 min (402.7s)` | `+12.4 min (743s)` | 2 | `66.67%` |
| **Route 925** | `+6.0 min (359.0s)` | `+22.3 min (1340s)` | 16 | `47.37%` |
| **Route 904** | `+5.7 min (342.6s)` | `+10.3 min (619s)` | 8 | `35.71%` |
| **Route 54** | `+5.7 min (341.2s)` | `+18.0 min (1078s)` | 11 | `58.82%` |
| **Route 83** | `+5.3 min (319.1s)` | `+12.8 min (771s)` | 3 | `33.33%` |
| **Route 46** | `+5.0 min (303.0s)` | `+7.2 min (431s)` | 1 | `50.0%` |
| **Route 94** | `+4.8 min (288.6s)` | `+11.0 min (661s)` | 3 | `71.43%` |
| **Route 921** | `+4.2 min (253.0s)` | `+14.6 min (874s)` | 9 | `76.47%` |

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
| `1334451` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1358678` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367390` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360986` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364587` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364746` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365319` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367701` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367729` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368417` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368458` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368740` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1272250` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1273283` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364793` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-03 21:33:49` | `11.32%` | `65.11%` | 751 | 665 | `+156.0s` |
| `2026-10-03 18:04:11` | `12.62%` | `70.93%` | 753 | 657 | `+130.4s` |
| `2026-10-03 14:04:12` | `17.74%` | `70.54%` | 682 | 560 | `+89.0s` |
| `2026-10-03 08:42:45` | `50.0%` | `73.33%` | 90 | 45 | `+56.7s` |
| `2026-10-03 02:53:57` | `7.89%` | `57.81%` | 431 | 384 | `+89.2s` |
| `2026-10-02 23:53:15` | `8.34%` | `61.71%` | 731 | 637 | `+87.4s` |
| `2026-10-02 15:11:12` | `14.86%` | `55.4%` | 828 | 704 | `+9.0s` |
| `2026-10-02 08:43:38` | `51.59%` | `62.3%` | 126 | 61 | `+-55.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-03T21:33:49.938869+00:00`.*
