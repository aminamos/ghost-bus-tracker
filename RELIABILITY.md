# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-02T15:11:12.362219+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.86%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.4%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `828` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `704` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `123` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+9.0s` (`0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-23.0s` (`-0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 390 | 47.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 272 | 32.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 39 | 4.7% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 123 | 14.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 7 | 2 | 4 | **`57.14%`** | `50.0%` | `+4.1m` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.0m` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-73.2s` |
| **Route 67** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-28.3s` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.6m` |
| **Route 18** | 31 | 14 | 12 | **`38.71%`** | `91.67%` | `+0.3m` |
| **Route 925** | 35 | 15 | 13 | **`37.14%`** | `80.0%` | `+1.2m` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `75.0%` | `+0.8m` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `-1.0s` |
| **Route 827** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `-143.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 716** | `+6.8 min (406.0s)` | `+15.2 min (914s)` | 1 | `66.67%` |
| **Route 25** | `+4.1 min (247.7s)` | `+14.6 min (877s)` | 2 | `50.0%` |
| **Route 11** | `+3.0 min (178.1s)` | `+13.1 min (788s)` | 11 | `75.0%` |
| **Route 902** | `+2.9 min (175.0s)` | `+8.5 min (510s)` | 12 | `91.67%` |
| **Route 921** | `+2.2 min (132.2s)` | `+9.0 min (541s)` | 7 | `85.71%` |
| **Route 10** | `+1.8 min (106.4s)` | `+12.8 min (770s)` | 12 | `86.67%` |
| **Route 46** | `+1.8 min (105.5s)` | `+4.2 min (253s)` | 2 | `100.0%` |
| **Route 5** | `+1.7 min (104.2s)` | `+8.6 min (513s)` | 3 | `66.67%` |
| **Route 645** | `+1.7 min (103.0s)` | `+4.0 min (240s)` | 4 | `100.0%` |
| **Route 94** | `+1.6 min (96.3s)` | `+4.2 min (253s)` | 7 | `100.0%` |

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
| `1326774` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330840` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317937` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318707` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319460` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319548` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319585` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319702` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331033` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331107` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332415` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-02 15:11:12` | `14.86%` | `55.4%` | 828 | 704 | `+9.0s` |
| `2026-10-02 08:43:38` | `51.59%` | `62.3%` | 126 | 61 | `+-55.2s` |
| `2026-10-02 02:21:57` | `10.25%` | `63.33%` | 478 | 420 | `+57.4s` |
| `2026-10-01 23:17:02` | `9.31%` | `54.51%` | 838 | 733 | `+125.8s` |
| `2026-10-01 19:08:55` | `15.25%` | `60.36%` | 951 | 777 | `+44.8s` |
| `2026-10-01 13:37:18` | `12.67%` | `55.91%` | 892 | 763 | `+54.9s` |
| `2026-10-01 06:13:46` | `1.64%` | `56.52%` | 61 | 46 | `+167.1s` |
| `2026-09-30 20:53:53` | `11.43%` | `58.62%` | 1111 | 940 | `+112.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-02T15:11:12.362219+00:00`.*
