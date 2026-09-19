# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-19T06:07:20.097383+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.91%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`76.6%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `55` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `47` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+120.9s` (`2.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+79.0s` (`1.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 36 | 65.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 5.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 14.5% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 10.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 3.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 17** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+2.0m` |
| **Route 921** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+4.7m` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-104.5s` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2m` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.7m` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.2m` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+2.4m` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.8m` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+1.6m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 925** | `+7.8 min (466.5s)` | `+8.0 min (479s)` | 2 | `0.0%` |
| **Route 923** | `+7.7 min (463.3s)` | `+11.1 min (664s)` | 2 | `0.0%` |
| **Route 36** | `+5.8 min (347.5s)` | `+11.5 min (691s)` | 2 | `50.0%` |
| **Route 921** | `+4.7 min (281.0s)` | `+4.7 min (281s)` | 1 | `100.0%` |
| **Route 61** | `+2.9 min (171.0s)` | `+2.9 min (171s)` | 1 | `100.0%` |
| **Route 3** | `+2.4 min (145.8s)` | `+6.0 min (362s)` | 5 | `80.0%` |
| **Route 62** | `+2.2 min (132.0s)` | `+5.0 min (299s)` | 1 | `100.0%` |
| **Route 22** | `+2.2 min (130.0s)` | `+3.6 min (216s)` | 2 | `100.0%` |
| **Route 17** | `+2.0 min (119.0s)` | `+2.0 min (119s)` | 1 | `100.0%` |
| **Route 922** | `+1.8 min (110.3s)` | `+4.5 min (267s)` | 3 | `100.0%` |

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
| `1135133` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317940` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349023` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1136096` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318865` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1354470` | Route 921 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 06:07:20` | `10.91%` | `76.6%` | 55 | 47 | `+120.9s` |
| `2026-09-19 01:20:14` | `15.47%` | `67.6%` | 569 | 463 | `+53.6s` |
| `2026-09-18 21:21:42` | `14.29%` | `55.31%` | 1120 | 905 | `+107.1s` |
| `2026-09-18 18:35:51` | `18.28%` | `55.26%` | 979 | 751 | `+9.8s` |
| `2026-09-18 15:26:34` | `17.53%` | `56.64%` | 884 | 708 | `+-13.0s` |
| `2026-09-18 06:08:06` | `7.84%` | `68.09%` | 51 | 47 | `+40.8s` |
| `2026-09-18 01:00:45` | `15.29%` | `66.8%` | 595 | 494 | `+67.2s` |
| `2026-09-17 22:57:58` | `14.59%` | `51.39%` | 905 | 755 | `+97.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T06:07:20.097383+00:00`.*
