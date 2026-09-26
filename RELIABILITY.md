# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-26T23:01:23.675228+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.53%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.08%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `726` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `595` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `91` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+115.2s` (`1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+52.0s` (`0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 417 | 57.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 83 | 11.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 85 | 11.7% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 1.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 91 | 12.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 40 | 5.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 11 | 0 | 11 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 36** | 10 | 3 | 5 | **`50.0%`** | `100.0%` | `+0.3m` |
| **Route 888** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-3.0s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-4.0s` |
| **Route 30** | 7 | 2 | 3 | **`42.86%`** | `50.0%` | `+3.5m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.7m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.6m` |
| **Route 9** | 15 | 7 | 5 | **`33.33%`** | `60.0%` | `+3.0m` |
| **Route 25** | 6 | 2 | 2 | **`33.33%`** | `25.0%` | `+6.3m` |
| **Route 645** | 6 | 2 | 2 | **`33.33%`** | `50.0%` | `+9.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+9.6 min (573.5s)` | `+22.9 min (1372s)` | 2 | `50.0%` |
| **Route 17** | `+7.5 min (448.8s)` | `+19.6 min (1179s)` | 10 | `30.0%` |
| **Route 25** | `+6.3 min (375.2s)` | `+9.3 min (558s)` | 2 | `25.0%` |
| **Route 721** | `+6.2 min (373.3s)` | `+12.9 min (773s)` | 2 | `66.67%` |
| **Route 10** | `+5.4 min (322.5s)` | `+26.6 min (1598s)` | 11 | `64.71%` |
| **Route 67** | `+4.4 min (266.1s)` | `+10.7 min (639s)` | 4 | `42.86%` |
| **Route 94** | `+4.0 min (237.4s)` | `+8.6 min (514s)` | 5 | `71.43%` |
| **Route 14** | `+3.9 min (234.0s)` | `+10.7 min (644s)` | 10 | `36.36%` |
| **Route 925** | `+3.8 min (230.8s)` | `+15.9 min (957s)` | 14 | `72.73%` |
| **Route 11** | `+3.8 min (230.3s)` | `+21.4 min (1286s)` | 10 | `69.23%` |

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
| `1325000` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326366` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327229` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327688` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330007` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348728` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348739` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362900` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318458` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351405` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1354333` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1354413` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333554` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333796` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1334400` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-26 23:01:23` | `12.53%` | `70.08%` | 726 | 595 | `+115.2s` |
| `2026-09-26 20:22:11` | `16.18%` | `70.23%` | 816 | 655 | `+114.3s` |
| `2026-09-26 17:50:32` | `16.6%` | `73.61%` | 807 | 649 | `+114.4s` |
| `2026-09-26 14:13:02` | `18.17%` | `71.12%` | 688 | 560 | `+121.0s` |
| `2026-09-26 09:59:50` | `29.5%` | `71.2%` | 261 | 184 | `+18.8s` |
| `2026-09-26 05:12:57` | `1.4%` | `63.83%` | 143 | 141 | `+50.0s` |
| `2026-09-25 21:43:01` | `10.61%` | `57.06%` | 1037 | 892 | `+58.8s` |
| `2026-09-25 18:15:51` | `14.87%` | `55.61%` | 928 | 776 | `+30.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-26T23:01:23.675228+00:00`.*
