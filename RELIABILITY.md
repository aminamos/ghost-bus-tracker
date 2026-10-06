# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T17:21:00.999726+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.34%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.14%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `916` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `770` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `113` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+34.1s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-5.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 440 | 48.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 263 | 28.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 56 | 6.1% |
| 🔴 **Severe Delay** | Over 15m late | 11 | 1.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 113 | 12.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 33 | 3.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `0.0%` | `-118.0s` |
| **Route 36** | 11 | 5 | 5 | **`45.45%`** | `66.67%` | `-19.2s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `75.0%` | `+0.4 min` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `50.0%` | `-42.8s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.4 min` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `+1.3 min` |
| **Route 721** | 11 | 4 | 4 | **`36.36%`** | `80.0%` | `+1.0 min` |
| **Route 18** | 39 | 20 | 13 | **`33.33%`** | `50.0%` | `+0.4 min` |
| **Route 924** | 39 | 18 | 13 | **`33.33%`** | `50.0%` | `+0.5 min` |
| **Route 67** | 12 | 6 | 4 | **`33.33%`** | `37.5%` | `-15.1s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 805** | `+11.6 min (+695.0s)` | `+50.9 min (+3054s)` | 3 | `16.67%` |
| **Route 10** | `+7.4 min (+445.1s)` | `+28.2 min (+1695s)` | 15 | `48.15%` |
| **Route 698** | `+5.3 min (+317.3s)` | `+15.2 min (+913s)` | 3 | `66.67%` |
| **Route 11** | `+4.9 min (+295.7s)` | `+24.2 min (+1454s)` | 12 | `41.18%` |
| **Route 94** | `+3.4 min (+205.4s)` | `+13.5 min (+810s)` | 5 | `77.78%` |
| **Route 17** | `+2.7 min (+163.7s)` | `+21.4 min (+1286s)` | 12 | `38.89%` |
| **Route 75** | `+2.5 min (+147.8s)` | `+9.7 min (+582s)` | 2 | `20.0%` |
| **Route 904** | `+2.4 min (+144.8s)` | `+5.8 min (+350s)` | 8 | `71.43%` |
| **Route 538** | `+2.4 min (+144.0s)` | `+11.3 min (+681s)` | 3 | `85.71%` |
| **Route 542** | `+2.4 min (+143.0s)` | `+6.3 min (+377s)` | 4 | `83.33%` |

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
| `1325320` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325632` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325819` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325994` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326661` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365597` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365892` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366126` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366842` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1010482` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1134032` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1134100` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1221326` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1242793` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 17:21:00` | `12.34%` | `57.14%` | 916 | 770 | `+34.1s` |
| `2026-10-06 13:46:34` | `11.85%` | `54.23%` | 869 | 745 | `+62.4s` |
| `2026-10-06 06:42:10` | `0.0%` | `81.25%` | 17 | 16 | `+237.0s` |
| `2026-10-06 00:28:45` | `9.69%` | `67.95%` | 650 | 547 | `+74.2s` |
| `2026-10-05 18:39:10` | `13.83%` | `56.53%` | 962 | 749 | `+13.5s` |
| `2026-10-05 17:20:37` | `12.38%` | `58.27%` | 945 | 762 | `+20.1s` |
| `2026-10-05 16:34:15` | `12.45%` | `58.06%` | 932 | 751 | `+17.6s` |
| `2026-10-05 12:15:22` | `10.84%` | `63.85%` | 950 | 805 | `+30.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T17:21:00.999726+00:00`.*
