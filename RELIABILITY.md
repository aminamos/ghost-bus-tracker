# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-01T13:37:18.256700+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.67%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.91%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `892` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `763` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `113` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+54.9s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 426 | 47.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 248 | 27.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 79 | 8.9% |
| 🔴 **Severe Delay** | Over 15m late | 9 | 1.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 113 | 12.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 1.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 9 | 4 | 4 | **`44.44%`** | `50.0%` | `+3.1m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.1m` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.1m` |
| **Route 540** | 11 | 5 | 4 | **`36.36%`** | `100.0%` | `-8.6s` |
| **Route 62** | 14 | 7 | 5 | **`35.71%`** | `100.0%` | `-124.8s` |
| **Route 64** | 23 | 11 | 8 | **`34.78%`** | `85.71%` | `-21.7s` |
| **Route 68** | 21 | 11 | 7 | **`33.33%`** | `100.0%` | `-109.6s` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `+0.6m` |
| **Route 18** | 25 | 14 | 8 | **`32.0%`** | `87.5%` | `+1.7m` |
| **Route 9** | 13 | 6 | 4 | **`30.77%`** | `57.14%` | `+3.2m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+10.5 min (631.9s)` | `+40.6 min (2434s)` | 10 | `43.75%` |
| **Route 850** | `+9.9 min (593.3s)` | `+31.7 min (1900s)` | 3 | `50.0%` |
| **Route 467** | `+7.2 min (432.0s)` | `+7.2 min (432s)` | 1 | `0.0%` |
| **Route 698** | `+5.2 min (309.4s)` | `+15.9 min (956s)` | 7 | `50.0%` |
| **Route 901** | `+4.6 min (277.5s)` | `+9.0 min (540s)` | 8 | `50.0%` |
| **Route 765** | `+4.1 min (246.0s)` | `+4.1 min (246s)` | 1 | `100.0%` |
| **Route 10** | `+3.9 min (232.7s)` | `+20.2 min (1212s)` | 11 | `50.0%` |
| **Route 673** | `+3.8 min (226.0s)` | `+3.8 min (226s)` | 1 | `100.0%` |
| **Route 645** | `+3.7 min (221.7s)` | `+14.1 min (843s)` | 5 | `71.43%` |
| **Route 355** | `+3.5 min (212.0s)` | `+3.5 min (212s)` | 1 | `100.0%` |

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
| `1325090` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325574` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326788` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327166` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317968` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318613` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318707` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319387` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331177` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331945` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332080` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1291036` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1293517` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319487` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319845` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-01 13:37:18` | `12.67%` | `55.91%` | 892 | 763 | `+54.9s` |
| `2026-10-01 06:13:46` | `1.64%` | `56.52%` | 61 | 46 | `+167.1s` |
| `2026-09-30 20:53:53` | `11.43%` | `58.62%` | 1111 | 940 | `+112.1s` |
| `2026-09-30 16:01:00` | `15.07%` | `58.97%` | 889 | 739 | `+9.4s` |
| `2026-09-30 09:22:54` | `35.85%` | `60.0%` | 265 | 170 | `+-36.8s` |
| `2026-09-30 02:59:00` | `9.84%` | `64.85%` | 437 | 367 | `+52.5s` |
| `2026-09-29 23:49:28` | `9.82%` | `59.97%` | 764 | 642 | `+78.4s` |
| `2026-09-29 20:04:44` | `14.44%` | `65.74%` | 1080 | 895 | `+56.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-01T13:37:18.256700+00:00`.*
