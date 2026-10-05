# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T18:02:18.416708+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.71%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.11%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `952` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `752` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `121` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+37.7s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-8.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 437 | 45.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 256 | 26.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 55 | 5.8% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 121 | 12.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 79 | 8.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 8 | 2 | 6 | **`75.0%`** | `50.0%` | `+0.2 min` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `33.33%` | `+1.7 min` |
| **Route 540** | 10 | 4 | 4 | **`40.0%`** | `33.33%` | `-36.8s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-1.0s` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `-64.0s` |
| **Route 827** | 5 | 3 | 2 | **`40.0%`** | `66.67%` | `+0.1 min` |
| **Route 9** | 13 | 8 | 5 | **`38.46%`** | `87.5%` | `+2.1 min` |
| **Route 67** | 12 | 6 | 4 | **`33.33%`** | `50.0%` | `+0.8 min` |
| **Route 721** | 12 | 4 | 4 | **`33.33%`** | `50.0%` | `+3.5 min` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `75.0%` | `-15.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 805** | `+45.3 min (+2719.5s)` | `+110.2 min (+6612s)` | 3 | `0.0%` |
| **Route 721** | `+3.5 min (+211.0s)` | `+21.0 min (+1258s)` | 4 | `50.0%` |
| **Route 227** | `+3.3 min (+199.7s)` | `+9.1 min (+548s)` | 2 | `66.67%` |
| **Route 225** | `+3.3 min (+198.7s)` | `+8.3 min (+498s)` | 2 | `66.67%` |
| **Route 904** | `+2.9 min (+176.7s)` | `+4.9 min (+296s)` | 7 | `100.0%` |
| **Route 725** | `+2.7 min (+162.8s)` | `+7.4 min (+442s)` | 2 | `50.0%` |
| **Route 38** | `+2.7 min (+161.9s)` | `+12.1 min (+724s)` | 6 | `37.5%` |
| **Route 923** | `+2.2 min (+133.8s)` | `+13.9 min (+836s)` | 8 | `50.0%` |
| **Route 9** | `+2.1 min (+126.8s)` | `+13.7 min (+824s)` | 8 | `87.5%` |
| **Route 75** | `+2.0 min (+121.2s)` | `+7.8 min (+467s)` | 2 | `60.0%` |

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
| `1324974` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1324995` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325632` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325813` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325980` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326096` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318288` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365064` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365582` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365792` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366126` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332584` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332687` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333002` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 18:02:18` | `12.71%` | `58.11%` | 952 | 752 | `+37.7s` |
| `2026-10-05 17:57:47` | `12.3%` | `58.16%` | 943 | 748 | `+38.7s` |
| `2026-10-05 17:20:37` | `12.38%` | `58.27%` | 945 | 762 | `+20.1s` |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T18:02:18.416708+00:00`.*
