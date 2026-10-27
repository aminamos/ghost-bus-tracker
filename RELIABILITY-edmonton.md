# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-27T05:00:22.575000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.84%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`87.55%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `289` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `131` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `40` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+78.3s` (`+1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+38.0s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 204 | 70.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 3.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 18 | 6.2% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 40 | 13.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 709** | 5 | 1 | 3 | **`60.0%`** | `100.0%` | `+1.5 min` |
| **Route A15** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 004** | 20 | 9 | 9 | **`45.0%`** | `100.0%` | `+0.5 min` |
| **Route 052** | 7 | 4 | 3 | **`42.86%`** | `100.0%` | `+0.1 min` |
| **Route 002** | 20 | 10 | 8 | **`40.0%`** | `90.91%` | `-19.3s` |
| **Route 056** | 9 | 5 | 3 | **`33.33%`** | `80.0%` | `+3.1 min` |
| **Route 916** | 6 | 3 | 2 | **`33.33%`** | `50.0%` | `+3.7 min` |
| **Route 001B** | 6 | 3 | 2 | **`33.33%`** | `100.0%` | `+1.1 min` |
| **Route 705** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `-7.0s` |
| **Route 501** | 3 | 1 | 1 | **`33.33%`** | `50.0%` | `-95.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 716** | `+13.0 min (+779.0s)` | `+13.3 min (+800s)` | 1 | `0.0%` |
| **Route 411** | `+8.0 min (+479.5s)` | `+11.8 min (+705s)` | 1 | `50.0%` |
| **Route 707** | `+7.9 min (+471.5s)` | `+15.0 min (+900s)` | 2 | `50.0%` |
| **Route 121** | `+6.6 min (+398.5s)` | `+7.4 min (+444s)` | 1 | `0.0%` |
| **Route 715** | `+6.0 min (+359.0s)` | `+7.0 min (+421s)` | 1 | `50.0%` |
| **Route 106** | `+5.0 min (+298.0s)` | `+6.3 min (+379s)` | 2 | `50.0%` |
| **Route 051** | `+4.5 min (+271.0s)` | `+6.0 min (+362s)` | 2 | `50.0%` |
| **Route 916** | `+3.7 min (+219.2s)` | `+5.6 min (+337s)` | 3 | `50.0%` |
| **Route 914** | `+3.3 min (+200.0s)` | `+4.6 min (+276s)` | 2 | `100.0%` |
| **Route 915** | `+3.1 min (+185.3s)` | `+5.2 min (+314s)` | 3 | `66.67%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 009** | ~20.0m | ~20.0m | **`+0.0 min`** | `68.6 / 100` |
| **Route 707** | ~60.0m | ~60.0m | **`+0.0 min`** | `88.1 / 100` |
| **Route 007** | ~20.0m | ~20.0m | **`+0.0 min`** | `82.0 / 100` |
| **Route 056** | ~60.0m | ~60.0m | **`+0.0 min`** | `90.2 / 100` |
| **Route 008** | ~20.0m | ~20.0m | **`+0.0 min`** | `86.9 / 100` |
| **Route 119** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.3 / 100` |
| **Route 901** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.4 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `90.2 / 100` |
| **Route 002** | ~20.0m | ~20.0m | **`+0.0 min`** | `92.1 / 100` |
| **Route 009** | ~20.0m | ~20.0m | **`+0.0 min`** | `92.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `33374155` | Route A15 | `18:30:00` | `SCHEDULED` | Assigned vehicle 8250 is missing from active GPS transponder fleet |
| `32760326` | Route 002 | `23:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762449` | Route 518 | `23:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762560` | Route 519 | `24:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904643` | Route 004 | `25:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32763923` | Route 916 | `23:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32763958` | Route 917 | `23:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762968` | Route 709 | `23:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762972` | Route 709 | `24:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32762967` | Route 709 | `23:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760166` | Route 001B | `24:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `33771320` | Route 501 | `23:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760949` | Route 056 | `24:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32763875` | Route 916 | `23:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 05:00:22` | `13.84%` | `87.55%` | 289 | 131 | `+78.3s` |
| `2026-10-27 04:30:19` | `17.33%` | `81.71%` | 329 | 146 | `+118.7s` |
| `2026-10-27 04:00:57` | `16.15%` | `83.47%` | 452 | 231 | `+70.2s` |
| `2026-10-27 03:30:24` | `17.28%` | `82.41%` | 573 | 265 | `+50.9s` |
| `2026-10-27 02:30:22` | `23.06%` | `83.37%` | 707 | 278 | `+54.0s` |
| `2026-10-27 01:30:24` | `29.77%` | `80.42%` | 786 | 287 | `+131.1s` |
| `2026-10-27 00:30:57` | `29.95%` | `76.45%` | 1015 | 408 | `+77.3s` |
| `2026-10-26 23:00:23` | `27.06%` | `65.1%` | 1641 | 678 | `+262.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T05:00:22.575000+00:00`.*
