# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-22T23:04:38.698836+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.54%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`51.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `886` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `720` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `120` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+81.8s` (`1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 372 | 42.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 229 | 25.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 102 | 11.5% |
| 🔴 **Severe Delay** | Over 15m late | 17 | 1.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 120 | 13.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 46 | 5.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 36** | 10 | 3 | 5 | **`50.0%`** | `66.67%` | `-21.8s` |
| **Route 25** | 6 | 2 | 3 | **`50.0%`** | `50.0%` | `+2.3m` |
| **Route 888** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `-119.0s` |
| **Route 65** | 9 | 3 | 4 | **`44.44%`** | `33.33%` | `+6.3m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-6.2s` |
| **Route 10** | 27 | 12 | 11 | **`40.74%`** | `81.82%` | `+0.5m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-16.7s` |
| **Route 538** | 11 | 3 | 4 | **`36.36%`** | `66.67%` | `+2.7m` |
| **Route 540** | 11 | 6 | 4 | **`36.36%`** | `100.0%` | `+0.3m` |
| **Route 64** | 20 | 11 | 7 | **`35.0%`** | `100.0%` | `-14.1s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 882** | `+17.4 min (1043.0s)` | `+17.4 min (1043s)` | 1 | `0.0%` |
| **Route 467** | `+13.2 min (794.0s)` | `+13.2 min (794s)` | 1 | `0.0%` |
| **Route 698** | `+10.2 min (612.7s)` | `+20.2 min (1212s)` | 3 | `33.33%` |
| **Route 755** | `+7.8 min (470.0s)` | `+7.8 min (470s)` | 1 | `0.0%` |
| **Route 113** | `+7.8 min (466.0s)` | `+7.8 min (466s)` | 1 | `0.0%` |
| **Route 645** | `+7.7 min (462.6s)` | `+32.9 min (1974s)` | 5 | `33.33%` |
| **Route 774** | `+7.7 min (459.5s)` | `+15.9 min (952s)` | 4 | `0.0%` |
| **Route 904** | `+6.5 min (388.7s)` | `+17.8 min (1066s)` | 10 | `41.18%` |
| **Route 65** | `+6.3 min (378.6s)` | `+20.2 min (1210s)` | 3 | `33.33%` |
| **Route 921** | `+5.4 min (321.5s)` | `+19.7 min (1184s)` | 11 | `53.33%` |

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
| `1325186` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325556` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325594` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325809` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326072` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326110` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326499` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326527` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326726` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326779` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318481` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319708` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319762` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349633` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-22 23:04:38` | `13.54%` | `51.67%` | 886 | 720 | `+81.8s` |
| `2026-09-22 20:19:25` | `16.97%` | `58.02%` | 1155 | 910 | `+57.0s` |
| `2026-09-22 17:26:26` | `18.48%` | `57.47%` | 958 | 743 | `+26.2s` |
| `2026-09-22 12:43:14` | `15.64%` | `59.95%` | 959 | 803 | `+72.9s` |
| `2026-09-22 07:02:34` | `0.0%` | `75.0%` | 5 | 4 | `+-5.5s` |
| `2026-09-22 01:41:09` | `16.23%` | `66.51%` | 530 | 430 | `+65.0s` |
| `2026-09-21 23:25:41` | `15.03%` | `53.0%` | 825 | 666 | `+13.2s` |
| `2026-09-21 20:03:32` | `17.78%` | `59.44%` | 1108 | 864 | `+35.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-22T23:04:38.698836+00:00`.*
