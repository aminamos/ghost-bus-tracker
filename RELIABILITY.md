# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-26T20:22:11.556098+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.23%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `816` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `655` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `132` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+114.3s` (`1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+70.0s` (`1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 460 | 56.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 102 | 12.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 83 | 10.2% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 1.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 132 | 16.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 29 | 3.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 25** | 7 | 2 | 4 | **`57.14%`** | `33.33%` | `+5.9m` |
| **Route 30** | 10 | 3 | 5 | **`50.0%`** | `80.0%` | `+4.6m` |
| **Route 36** | 11 | 6 | 5 | **`45.45%`** | `100.0%` | `+0.6m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.9m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.9m` |
| **Route 10** | 36 | 14 | 15 | **`41.67%`** | `94.12%` | `+1.2m` |
| **Route 18** | 36 | 16 | 15 | **`41.67%`** | `86.67%` | `+0.9m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+2.2m` |
| **Route 7** | 13 | 6 | 5 | **`38.46%`** | `75.0%` | `+3.7m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+9.2 min (550.5s)` | `+21.0 min (1262s)` | 3 | `50.0%` |
| **Route 25** | `+5.9 min (351.7s)` | `+9.3 min (558s)` | 2 | `33.33%` |
| **Route 925** | `+5.1 min (305.8s)` | `+20.1 min (1204s)` | 16 | `55.0%` |
| **Route 22** | `+5.0 min (297.3s)` | `+17.7 min (1064s)` | 11 | `53.85%` |
| **Route 901** | `+4.8 min (290.0s)` | `+9.0 min (540s)` | 3 | `66.67%` |
| **Route 30** | `+4.6 min (273.2s)` | `+11.0 min (659s)` | 3 | `80.0%` |
| **Route 14** | `+4.5 min (268.5s)` | `+16.3 min (978s)` | 9 | `80.0%` |
| **Route 3** | `+4.4 min (261.4s)` | `+12.5 min (750s)` | 11 | `64.71%` |
| **Route 9** | `+4.3 min (257.4s)` | `+7.4 min (446s)` | 7 | `33.33%` |
| **Route 7** | `+3.7 min (220.5s)` | `+9.5 min (570s)` | 6 | `75.0%` |

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
| `1325373` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325562` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325977` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326079` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326960` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327455` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327475` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1328503` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1328920` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1329815` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1334227` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348763` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1352445` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1355279` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362759` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-26 20:22:11` | `16.18%` | `70.23%` | 816 | 655 | `+114.3s` |
| `2026-09-26 17:50:32` | `16.6%` | `73.61%` | 807 | 649 | `+114.4s` |
| `2026-09-26 14:13:02` | `18.17%` | `71.12%` | 688 | 560 | `+121.0s` |
| `2026-09-26 09:59:50` | `29.5%` | `71.2%` | 261 | 184 | `+18.8s` |
| `2026-09-26 05:12:57` | `1.4%` | `63.83%` | 143 | 141 | `+50.0s` |
| `2026-09-25 21:43:01` | `10.61%` | `57.06%` | 1037 | 892 | `+58.8s` |
| `2026-09-25 18:15:51` | `14.87%` | `55.61%` | 928 | 776 | `+30.8s` |
| `2026-09-25 13:59:05` | `15.02%` | `55.6%` | 832 | 705 | `+-3.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-26T20:22:11.556098+00:00`.*
