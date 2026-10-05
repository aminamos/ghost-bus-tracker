# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T11:43:44.868765+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.82%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.04%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `915` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `773` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `99` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+8.8s` (`+0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-5.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 495 | 54.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 246 | 26.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 31 | 3.4% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 99 | 10.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 43 | 4.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 537** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `-38.0s` |
| **Route 540** | 10 | 3 | 6 | **`60.0%`** | `75.0%` | `+3.0 min` |
| **Route 542** | 7 | 2 | 4 | **`57.14%`** | `100.0%` | `+1.5 min` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.6 min` |
| **Route 615** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-191.0s` |
| **Route 765** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.3 min` |
| **Route 9** | 13 | 6 | 6 | **`46.15%`** | `71.43%` | `+0.1 min` |
| **Route 223** | 8 | 2 | 3 | **`37.5%`** | `80.0%` | `+2.7 min` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `85.71%` | `+0.9 min` |
| **Route 67** | 11 | 4 | 4 | **`36.36%`** | `57.14%` | `-26.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 698** | `+4.3 min (+257.7s)` | `+9.3 min (+556s)` | 7 | `57.14%` |
| **Route 71** | `+3.7 min (+223.6s)` | `+32.7 min (+1962s)` | 6 | `22.22%` |
| **Route 467** | `+3.5 min (+207.7s)` | `+7.6 min (+457s)` | 3 | `66.67%` |
| **Route 921** | `+3.3 min (+200.7s)` | `+6.9 min (+414s)` | 7 | `85.71%` |
| **Route 540** | `+3.0 min (+179.2s)` | `+8.6 min (+517s)` | 3 | `75.0%` |
| **Route 223** | `+2.7 min (+162.2s)` | `+8.7 min (+521s)` | 2 | `80.0%` |
| **Route 227** | `+2.6 min (+158.0s)` | `+2.6 min (+158s)` | 1 | `100.0%` |
| **Route 902** | `+2.5 min (+150.0s)` | `+9.0 min (+540s)` | 12 | `83.33%` |
| **Route 888** | `+2.4 min (+143.3s)` | `+7.4 min (+442s)` | 4 | `33.33%` |
| **Route 54** | `+2.4 min (+142.1s)` | `+14.3 min (+858s)` | 11 | `86.67%` |

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
| `1332184` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332665` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333252` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360902` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360919` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361721` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361731` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364291` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365082` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365848` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366539` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1280563` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1286561` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364330` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365254` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 11:43:44` | `10.82%` | `64.04%` | 915 | 773 | `+8.8s` |
| `2026-10-05 09:18:29` | `33.33%` | `57.79%` | 231 | 154 | `-42.7s` |
| `2026-10-05 02:10:28` | `11.4%` | `67.17%` | 386 | 332 | `+204.7s` |
| `2026-10-04 23:20:57` | `9.43%` | `61.8%` | 562 | 501 | `+251.0s` |
| `2026-10-04 20:16:15` | `11.44%` | `60.24%` | 673 | 591 | `+290.1s` |
| `2026-10-04 17:11:23` | `17.78%` | `59.12%` | 731 | 592 | `+342.9s` |
| `2026-10-04 12:37:23` | `25.23%` | `74.03%` | 555 | 413 | `+160.6s` |
| `2026-10-04 06:05:55` | `0.0%` | `42.31%` | 52 | 52 | `+138.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T11:43:44.868765+00:00`.*
