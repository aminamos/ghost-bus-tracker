# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-25T13:59:05.063902+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.02%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.6%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `832` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `705` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `125` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+-3.5s` (`-0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-28.0s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 392 | 47.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 267 | 32.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 44 | 5.3% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 125 | 15.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 902** | 12 | 0 | 12 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 850** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `-61.0s` |
| **Route 537** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.4m` |
| **Route 18** | 29 | 12 | 14 | **`48.28%`** | `66.67%` | `+0.8m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-72.2s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.6m` |
| **Route 64** | 22 | 9 | 8 | **`36.36%`** | `100.0%` | `-65.4s` |
| **Route 921** | 22 | 7 | 8 | **`36.36%`** | `92.86%` | `+1.3m` |
| **Route 36** | 11 | 4 | 4 | **`36.36%`** | `75.0%` | `+1.4m` |
| **Route 540** | 11 | 5 | 4 | **`36.36%`** | `100.0%` | `+0.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 113** | `+8.6 min (514.0s)` | `+11.8 min (706s)` | 2 | `0.0%` |
| **Route 725** | `+6.4 min (382.0s)` | `+15.1 min (908s)` | 2 | `66.67%` |
| **Route 252** | `+4.8 min (287.0s)` | `+4.8 min (287s)` | 1 | `100.0%` |
| **Route 5** | `+3.8 min (225.5s)` | `+16.5 min (991s)` | 4 | `75.0%` |
| **Route 904** | `+2.9 min (176.6s)` | `+7.8 min (470s)` | 8 | `61.54%` |
| **Route 542** | `+1.7 min (99.5s)` | `+3.7 min (223s)` | 5 | `100.0%` |
| **Route 901** | `+1.5 min (90.0s)` | `+5.5 min (330s)` | 8 | `87.5%` |
| **Route 25** | `+1.5 min (87.2s)` | `+5.1 min (306s)` | 3 | `66.67%` |
| **Route 30** | `+1.4 min (82.9s)` | `+6.4 min (382s)` | 4 | `83.33%` |
| **Route 36** | `+1.4 min (81.0s)` | `+13.1 min (786s)` | 4 | `75.0%` |

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
| `1331177` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331653` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331945` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332772` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1241247` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348925` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349189` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350010` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350209` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350286` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350472` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351107` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351461` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351487` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1355734` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-25 13:59:05` | `15.02%` | `55.6%` | 832 | 705 | `+-3.5s` |
| `2026-09-25 08:05:53` | `0.0%` | `46.67%` | 15 | 15 | `+-65.4s` |
| `2026-09-25 02:29:37` | `13.75%` | `62.81%` | 502 | 398 | `+52.3s` |
| `2026-09-24 20:37:01` | `12.62%` | `57.31%` | 1109 | 923 | `+92.5s` |
| `2026-09-24 12:27:28` | `13.19%` | `61.43%` | 940 | 809 | `+45.2s` |
| `2026-09-24 06:56:04` | `0.0%` | `72.73%` | 11 | 11 | `+521.7s` |
| `2026-09-24 01:32:00` | `14.93%` | `63.6%` | 576 | 456 | `+105.3s` |
| `2026-09-23 23:19:59` | `15.63%` | `54.14%` | 870 | 677 | `+92.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-25T13:59:05.063902+00:00`.*
