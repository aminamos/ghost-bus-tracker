# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T17:21:51.765596+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.49%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.22%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `913` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `766` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `114` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+39.0s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-2.0s` (`-0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 446 | 48.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 254 | 27.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 55 | 6.0% |
| 🔴 **Severe Delay** | Over 15m late | 11 | 1.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 114 | 12.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 33 | 3.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `0.0%` | `-118.5s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `75.0%` | `+0.4 min` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `50.0%` | `-31.8s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.3 min` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `+1.3 min` |
| **Route 36** | 11 | 6 | 4 | **`36.36%`** | `71.43%` | `+1.2 min` |
| **Route 721** | 11 | 4 | 4 | **`36.36%`** | `80.0%` | `+1.3 min` |
| **Route 18** | 40 | 20 | 14 | **`35.0%`** | `53.85%` | `+0.4 min` |
| **Route 924** | 40 | 18 | 14 | **`35.0%`** | `50.0%` | `+0.7 min` |
| **Route 67** | 12 | 6 | 4 | **`33.33%`** | `37.5%` | `-13.8s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 805** | `+11.9 min (+714.8s)` | `+52.1 min (+3126s)` | 3 | `16.67%` |
| **Route 10** | `+7.5 min (+450.4s)` | `+28.3 min (+1697s)` | 15 | `48.15%` |
| **Route 11** | `+5.1 min (+303.9s)` | `+24.9 min (+1497s)` | 12 | `41.18%` |
| **Route 698** | `+4.1 min (+247.2s)` | `+15.2 min (+913s)` | 4 | `75.0%` |
| **Route 94** | `+3.7 min (+223.6s)` | `+14.7 min (+882s)` | 5 | `77.78%` |
| **Route 17** | `+2.8 min (+168.4s)` | `+21.2 min (+1275s)` | 12 | `38.89%` |
| **Route 75** | `+2.7 min (+161.4s)` | `+10.2 min (+611s)` | 2 | `20.0%` |
| **Route 904** | `+2.6 min (+154.9s)` | `+7.8 min (+469s)` | 8 | `71.43%` |
| **Route 542** | `+2.5 min (+152.7s)` | `+6.5 min (+393s)` | 4 | `83.33%` |
| **Route 538** | `+2.4 min (+144.6s)` | `+11.7 min (+704s)` | 3 | `85.71%` |

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
| `2026-10-06 17:21:51` | `12.49%` | `58.22%` | 913 | 766 | `+39.0s` |
| `2026-10-06 17:21:00` | `12.34%` | `57.14%` | 916 | 770 | `+34.1s` |
| `2026-10-06 13:46:34` | `11.85%` | `54.23%` | 869 | 745 | `+62.4s` |
| `2026-10-06 06:42:10` | `0.0%` | `81.25%` | 17 | 16 | `+237.0s` |
| `2026-10-06 00:28:45` | `9.69%` | `67.95%` | 650 | 547 | `+74.2s` |
| `2026-10-05 18:39:10` | `13.83%` | `56.53%` | 962 | 749 | `+13.5s` |
| `2026-10-05 17:20:37` | `12.38%` | `58.27%` | 945 | 762 | `+20.1s` |
| `2026-10-05 16:34:15` | `12.45%` | `58.06%` | 932 | 751 | `+17.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T17:21:51.765596+00:00`.*
