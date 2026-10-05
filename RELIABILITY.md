# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T12:03:24.772372+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.54%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.02%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `949` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `806` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `100` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+28.8s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 516 | 54.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 238 | 25.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 46 | 4.8% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 100 | 10.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 43 | 4.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 537** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `-0.5s` |
| **Route 765** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.6 min` |
| **Route 540** | 11 | 4 | 5 | **`45.45%`** | `83.33%` | `+0.9 min` |
| **Route 542** | 7 | 3 | 3 | **`42.86%`** | `100.0%` | `+1.6 min` |
| **Route 36** | 10 | 4 | 4 | **`40.0%`** | `83.33%` | `+1.0 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.3 min` |
| **Route 67** | 11 | 4 | 4 | **`36.36%`** | `71.43%` | `+0.7 min` |
| **Route 924** | 30 | 15 | 10 | **`33.33%`** | `70.0%` | `+0.2 min` |
| **Route 25** | 9 | 5 | 3 | **`33.33%`** | `66.67%` | `+3.3 min` |
| **Route 827** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `-169.2s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 716** | `+9.2 min (+554.7s)` | `+18.6 min (+1115s)` | 1 | `33.33%` |
| **Route 784** | `+7.7 min (+459.0s)` | `+12.0 min (+722s)` | 3 | `33.33%` |
| **Route 71** | `+7.5 min (+447.3s)` | `+52.6 min (+3154s)` | 6 | `40.0%` |
| **Route 467** | `+6.1 min (+366.0s)` | `+7.6 min (+457s)` | 3 | `33.33%` |
| **Route 698** | `+4.9 min (+291.3s)` | `+9.6 min (+576s)` | 8 | `44.44%` |
| **Route 294** | `+4.5 min (+272.0s)` | `+4.5 min (+272s)` | 1 | `100.0%` |
| **Route 223** | `+4.5 min (+269.8s)` | `+16.8 min (+1010s)` | 2 | `80.0%` |
| **Route 755** | `+4.5 min (+268.2s)` | `+9.3 min (+561s)` | 3 | `25.0%` |
| **Route 901** | `+3.4 min (+201.4s)` | `+12.0 min (+720s)` | 7 | `85.71%` |
| **Route 25** | `+3.3 min (+197.0s)` | `+6.7 min (+400s)` | 5 | `66.67%` |

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
| `1366088` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366792` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331609` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332184` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332665` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1012205` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1012594` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1132723` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1134267` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360917` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360919` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361436` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361731` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364586` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364628` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 12:03:24` | `10.54%` | `64.02%` | 949 | 806 | `+28.8s` |
| `2026-10-05 11:43:44` | `10.82%` | `64.04%` | 915 | 773 | `+8.8s` |
| `2026-10-05 09:18:29` | `33.33%` | `57.79%` | 231 | 154 | `-42.7s` |
| `2026-10-05 02:10:28` | `11.4%` | `67.17%` | 386 | 332 | `+204.7s` |
| `2026-10-04 23:20:57` | `9.43%` | `61.8%` | 562 | 501 | `+251.0s` |
| `2026-10-04 20:16:15` | `11.44%` | `60.24%` | 673 | 591 | `+290.1s` |
| `2026-10-04 17:11:23` | `17.78%` | `59.12%` | 731 | 592 | `+342.9s` |
| `2026-10-04 12:37:23` | `25.23%` | `74.03%` | 555 | 413 | `+160.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T12:03:24.772372+00:00`.*
