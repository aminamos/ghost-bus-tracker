# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-26T09:59:50.658844+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`29.5%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.2%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `261` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `184` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `77` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+18.8s` (`0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+8.0s` (`0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 131 | 50.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 46 | 17.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 2.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 77 | 29.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 11 | 0 | 11 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 223** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 9** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `-155.5s` |
| **Route 215** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `-24.0s` |
| **Route 25** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+1.1m` |
| **Route 18** | 13 | 5 | 8 | **`61.54%`** | `100.0%` | `-11.0s` |
| **Route 10** | 8 | 3 | 4 | **`50.0%`** | `100.0%` | `+0.7m` |
| **Route 17** | 8 | 3 | 4 | **`50.0%`** | `100.0%` | `+1.5m` |
| **Route 924** | 20 | 9 | 9 | **`45.0%`** | `100.0%` | `-20.4s` |
| **Route 11** | 9 | 5 | 4 | **`44.44%`** | `75.0%` | `+1.7m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 716** | `+7.1 min (428.0s)` | `+7.1 min (428s)` | 1 | `0.0%` |
| **Route 904** | `+3.2 min (190.3s)` | `+8.4 min (502s)` | 7 | `70.0%` |
| **Route 3** | `+2.5 min (148.5s)` | `+5.6 min (337s)` | 3 | `75.0%` |
| **Route 14** | `+2.2 min (134.3s)` | `+3.0 min (183s)` | 3 | `100.0%` |
| **Route 724** | `+2.1 min (125.5s)` | `+3.8 min (225s)` | 2 | `100.0%` |
| **Route 54** | `+2.1 min (124.1s)` | `+4.5 min (271s)` | 5 | `100.0%` |
| **Route 74** | `+1.7 min (104.0s)` | `+4.0 min (238s)` | 3 | `100.0%` |
| **Route 11** | `+1.7 min (101.6s)` | `+6.6 min (394s)` | 5 | `75.0%` |
| **Route 17** | `+1.5 min (88.0s)` | `+4.5 min (267s)` | 3 | `100.0%` |
| **Route 901** | `+1.2 min (72.0s)` | `+3.0 min (180s)` | 5 | `100.0%` |

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
| `1325586` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325942` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327342` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1328626` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351812` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1352588` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1353002` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1354190` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331569` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331751` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1131869` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1324662` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1334330` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1363742` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1356728` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-26 09:59:50` | `29.5%` | `71.2%` | 261 | 184 | `+18.8s` |
| `2026-09-26 05:12:57` | `1.4%` | `63.83%` | 143 | 141 | `+50.0s` |
| `2026-09-25 21:43:01` | `10.61%` | `57.06%` | 1037 | 892 | `+58.8s` |
| `2026-09-25 18:15:51` | `14.87%` | `55.61%` | 928 | 776 | `+30.8s` |
| `2026-09-25 13:59:05` | `15.02%` | `55.6%` | 832 | 705 | `+-3.5s` |
| `2026-09-25 08:05:53` | `0.0%` | `46.67%` | 15 | 15 | `+-65.4s` |
| `2026-09-25 02:29:37` | `13.75%` | `62.81%` | 502 | 398 | `+52.3s` |
| `2026-09-24 20:37:01` | `12.62%` | `57.31%` | 1109 | 923 | `+92.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-26T09:59:50.658844+00:00`.*
