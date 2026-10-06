# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T13:46:34.766700+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.85%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`54.23%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `869` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `745` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `103` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+62.4s` (`+1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+2.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 404 | 46.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 243 | 28.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 85 | 9.8% |
| 🔴 **Severe Delay** | Over 15m late | 13 | 1.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 103 | 11.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 21 | 2.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 8 | 3 | 4 | **`50.0%`** | `50.0%` | `+1.9 min` |
| **Route 888** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `-201.0s` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `50.0%` | `+0.5 min` |
| **Route 721** | 10 | 3 | 4 | **`40.0%`** | `66.67%` | `+3.6 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.4 min` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.5 min` |
| **Route 223** | 8 | 2 | 3 | **`37.5%`** | `60.0%` | `+1.0 min` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `57.14%` | `+2.6 min` |
| **Route 67** | 11 | 5 | 4 | **`36.36%`** | `42.86%` | `-8.1s` |
| **Route 18** | 24 | 13 | 8 | **`33.33%`** | `75.0%` | `+1.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 673** | `+16.2 min (+971.5s)` | `+17.5 min (+1048s)` | 2 | `0.0%` |
| **Route 355** | `+12.9 min (+772.0s)` | `+12.9 min (+772s)` | 1 | `0.0%` |
| **Route 467** | `+11.4 min (+686.0s)` | `+11.4 min (+686s)` | 1 | `0.0%` |
| **Route 698** | `+9.3 min (+556.6s)` | `+23.3 min (+1396s)` | 7 | `14.29%` |
| **Route 904** | `+8.6 min (+517.6s)` | `+29.8 min (+1785s)` | 10 | `23.53%` |
| **Route 790** | `+8.0 min (+477.0s)` | `+8.0 min (+477s)` | 1 | `0.0%` |
| **Route 270** | `+5.5 min (+333.0s)` | `+6.8 min (+410s)` | 1 | `50.0%` |
| **Route 776** | `+5.4 min (+322.0s)` | `+10.9 min (+652s)` | 2 | `50.0%` |
| **Route 113** | `+5.2 min (+310.0s)` | `+10.2 min (+612s)` | 2 | `50.0%` |
| **Route 774** | `+4.5 min (+272.0s)` | `+7.0 min (+418s)` | 2 | `50.0%` |

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
| `1325277` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326702` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326916` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1328795` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364293` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365816` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366713` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366794` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1010201` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1012183` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1131571` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1132349` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360945` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361517` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361742` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 13:46:34` | `11.85%` | `54.23%` | 869 | 745 | `+62.4s` |
| `2026-10-06 06:42:10` | `0.0%` | `81.25%` | 17 | 16 | `+237.0s` |
| `2026-10-06 00:28:45` | `9.69%` | `67.95%` | 650 | 547 | `+74.2s` |
| `2026-10-05 18:39:10` | `13.83%` | `56.53%` | 962 | 749 | `+13.5s` |
| `2026-10-05 17:20:37` | `12.38%` | `58.27%` | 945 | 762 | `+20.1s` |
| `2026-10-05 16:34:15` | `12.45%` | `58.06%` | 932 | 751 | `+17.6s` |
| `2026-10-05 12:15:22` | `10.84%` | `63.85%` | 950 | 805 | `+30.8s` |
| `2026-10-05 12:03:24` | `10.54%` | `64.02%` | 949 | 806 | `+28.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T13:46:34.766700+00:00`.*
