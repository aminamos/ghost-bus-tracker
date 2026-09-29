# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-29T15:13:43.960445+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.15%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.78%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `836` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `694` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `135` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+-5.4s` (`-0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-26.0s` (`-0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 391 | 46.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 277 | 33.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 33 | 3.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 135 | 16.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.1m` |
| **Route 32** | 13 | 4 | 6 | **`46.15%`** | `100.0%` | `-81.3s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-36.5s` |
| **Route 64** | 22 | 9 | 9 | **`40.91%`** | `85.71%` | `-30.8s` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-88.8s` |
| **Route 5** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `-77.3s` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.3m` |
| **Route 18** | 31 | 14 | 12 | **`38.71%`** | `86.67%` | `+1.2m` |
| **Route 10** | 22 | 10 | 8 | **`36.36%`** | `66.67%` | `+1.9m` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `100.0%` | `-33.1s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 725** | `+4.1 min (245.3s)` | `+9.5 min (571s)` | 2 | `66.67%` |
| **Route 25** | `+2.8 min (168.2s)` | `+11.0 min (661s)` | 3 | `66.67%` |
| **Route 645** | `+2.6 min (157.4s)` | `+6.5 min (392s)` | 5 | `75.0%` |
| **Route 10** | `+1.9 min (112.8s)` | `+13.3 min (800s)` | 10 | `66.67%` |
| **Route 921** | `+1.8 min (109.4s)` | `+4.9 min (296s)` | 6 | `100.0%` |
| **Route 9** | `+1.8 min (109.2s)` | `+14.2 min (853s)` | 7 | `83.33%` |
| **Route 901** | `+1.8 min (108.8s)` | `+4.0 min (240s)` | 8 | `100.0%` |
| **Route 227** | `+1.7 min (99.3s)` | `+6.0 min (362s)` | 2 | `50.0%` |
| **Route 46** | `+1.4 min (85.1s)` | `+7.5 min (447s)` | 3 | `85.71%` |
| **Route 925** | `+1.4 min (82.8s)` | `+10.2 min (610s)` | 16 | `76.47%` |

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
| `1324991` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325475` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326229` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326520` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326546` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326719` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326774` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330840` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317937` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318707` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319440` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319548` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319585` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348990` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349161` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-29 15:13:43` | `16.15%` | `55.78%` | 836 | 694 | `+-5.4s` |
| `2026-09-29 08:47:30` | `52.17%` | `59.09%` | 138 | 66 | `+-52.2s` |
| `2026-09-29 02:07:24` | `11.2%` | `65.25%` | 500 | 423 | `+53.5s` |
| `2026-09-28 22:11:30` | `10.83%` | `55.27%` | 997 | 854 | `+53.1s` |
| `2026-09-28 16:23:26` | `14.55%` | `56.91%` | 873 | 739 | `+7.1s` |
| `2026-09-28 07:57:13` | `0.0%` | `55.56%` | 9 | 9 | `+-82.7s` |
| `2026-09-28 01:53:47` | `11.36%` | `70.89%` | 396 | 347 | `+171.9s` |
| `2026-09-27 23:29:25` | `9.87%` | `65.48%` | 537 | 478 | `+215.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-29T15:13:43.960445+00:00`.*
