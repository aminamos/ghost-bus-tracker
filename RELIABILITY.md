# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-20T02:21:35.400289+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.92%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `447` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `368` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `73` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+162.2s` (`2.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+115.5s` (`1.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 261 | 58.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 34 | 7.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 68 | 15.2% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 73 | 16.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 6 | 1.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 12 | 4 | 6 | **`50.0%`** | `75.0%` | `+1.8m` |
| **Route 11** | 12 | 4 | 6 | **`50.0%`** | `100.0%` | `+1.8m` |
| **Route 64** | 15 | 5 | 7 | **`46.67%`** | `85.71%` | `+2.8m` |
| **Route 18** | 24 | 10 | 10 | **`41.67%`** | `83.33%` | `+1.4m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `-97.3s` |
| **Route 921** | 22 | 6 | 8 | **`36.36%`** | `83.33%` | `+2.4m` |
| **Route 36** | 12 | 5 | 4 | **`33.33%`** | `75.0%` | `+4.0m` |
| **Route 38** | 12 | 6 | 4 | **`33.33%`** | `75.0%` | `-65.9s` |
| **Route 7** | 6 | 3 | 2 | **`33.33%`** | `100.0%` | `+3.4m` |
| **Route 17** | 13 | 6 | 4 | **`30.77%`** | `77.78%` | `+3.0m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9** | `+8.2 min (494.5s)` | `+26.6 min (1594s)` | 5 | `33.33%` |
| **Route 14** | `+5.6 min (337.6s)` | `+17.1 min (1024s)` | 7 | `62.5%` |
| **Route 904** | `+5.2 min (314.1s)` | `+8.9 min (536s)` | 7 | `42.86%` |
| **Route 54** | `+4.7 min (284.6s)` | `+8.9 min (536s)` | 13 | `56.25%` |
| **Route 32** | `+4.6 min (278.5s)` | `+9.2 min (549s)` | 1 | `50.0%` |
| **Route 63** | `+4.6 min (275.6s)` | `+9.5 min (570s)` | 5 | `50.0%` |
| **Route 22** | `+4.3 min (258.9s)` | `+10.7 min (644s)` | 6 | `62.5%` |
| **Route 36** | `+4.0 min (242.4s)` | `+8.7 min (523s)` | 5 | `75.0%` |
| **Route 925** | `+3.9 min (236.2s)` | `+12.0 min (720s)` | 10 | `68.75%` |
| **Route 902** | `+3.9 min (232.5s)` | `+10.0 min (600s)` | 8 | `62.5%` |

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
| `1324986` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326967` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1328775` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330848` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1358290` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1359692` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318409` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319059` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319404` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348909` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349215` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350258` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1335783` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1132752` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319660` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-20 02:21:35` | `16.33%` | `70.92%` | 447 | 368 | `+162.2s` |
| `2026-09-19 23:49:14` | `13.98%` | `71.89%` | 615 | 523 | `+139.8s` |
| `2026-09-19 21:56:09` | `17.13%` | `67.68%` | 759 | 622 | `+110.3s` |
| `2026-09-19 17:35:31` | `21.22%` | `71.71%` | 787 | 617 | `+125.3s` |
| `2026-09-19 14:34:03` | `21.62%` | `72.91%` | 717 | 561 | `+80.6s` |
| `2026-09-19 13:42:25` | `23.87%` | `74.32%` | 683 | 518 | `+82.8s` |
| `2026-09-19 13:37:58` | `23.7%` | `71.4%` | 675 | 514 | `+83.2s` |
| `2026-09-19 13:33:11` | `24.19%` | `72.29%` | 682 | 516 | `+82.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-20T02:21:35.400289+00:00`.*
