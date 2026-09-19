# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-19T23:49:14.173390+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.98%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.89%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `615` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `523` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `86` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+139.8s` (`2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+88.0s` (`1.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 376 | 61.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 63 | 10.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 75 | 12.2% |
| 🔴 **Severe Delay** | Over 15m late | 9 | 1.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 86 | 14.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 6 | 1.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.5m` |
| **Route 18** | 25 | 11 | 10 | **`40.0%`** | `81.82%` | `+1.6m` |
| **Route 921** | 22 | 8 | 8 | **`36.36%`** | `57.14%` | `+6.4m` |
| **Route 11** | 14 | 7 | 5 | **`35.71%`** | `75.0%` | `+2.1m` |
| **Route 36** | 12 | 5 | 4 | **`33.33%`** | `85.71%` | `+2.0m` |
| **Route 38** | 12 | 7 | 4 | **`33.33%`** | `83.33%` | `+1.1m` |
| **Route 10** | 19 | 9 | 6 | **`31.58%`** | `58.33%` | `+6.6m` |
| **Route 64** | 21 | 11 | 6 | **`28.57%`** | `80.0%` | `+2.8m` |
| **Route 17** | 14 | 6 | 4 | **`28.57%`** | `70.0%` | `+4.4m` |
| **Route 62** | 11 | 5 | 3 | **`27.27%`** | `60.0%` | `+2.0m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 805** | `+6.7 min (403.0s)` | `+6.7 min (403s)` | 1 | `0.0%` |
| **Route 10** | `+6.6 min (396.9s)` | `+31.7 min (1901s)` | 9 | `58.33%` |
| **Route 921** | `+6.4 min (383.1s)` | `+16.8 min (1007s)` | 8 | `57.14%` |
| **Route 54** | `+5.3 min (317.9s)` | `+27.8 min (1666s)` | 11 | `60.0%` |
| **Route 72** | `+5.2 min (312.0s)` | `+11.8 min (705s)` | 2 | `75.0%` |
| **Route 904** | `+4.9 min (296.6s)` | `+11.7 min (700s)` | 7 | `57.14%` |
| **Route 17** | `+4.4 min (261.2s)` | `+17.4 min (1043s)` | 6 | `70.0%` |
| **Route 61** | `+4.3 min (257.1s)` | `+14.8 min (888s)` | 6 | `77.78%` |
| **Route 925** | `+4.2 min (253.2s)` | `+17.5 min (1048s)` | 14 | `70.0%` |
| **Route 922** | `+3.7 min (224.5s)` | `+14.7 min (884s)` | 15 | `71.43%` |

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
| `1325843` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326366` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327200` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327391` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330864` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348749` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318409` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318458` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350899` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351405` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351511` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333554` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1334602` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1320107` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1320113` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 23:49:14` | `13.98%` | `71.89%` | 615 | 523 | `+139.8s` |
| `2026-09-19 21:56:09` | `17.13%` | `67.68%` | 759 | 622 | `+110.3s` |
| `2026-09-19 17:35:31` | `21.22%` | `71.71%` | 787 | 617 | `+125.3s` |
| `2026-09-19 14:34:03` | `21.62%` | `72.91%` | 717 | 561 | `+80.6s` |
| `2026-09-19 13:42:25` | `23.87%` | `74.32%` | 683 | 518 | `+82.8s` |
| `2026-09-19 13:37:58` | `23.7%` | `71.4%` | 675 | 514 | `+83.2s` |
| `2026-09-19 13:33:11` | `24.19%` | `72.29%` | 682 | 516 | `+82.7s` |
| `2026-09-19 13:13:58` | `24.44%` | `71.97%` | 667 | 503 | `+73.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T23:49:14.173390+00:00`.*
