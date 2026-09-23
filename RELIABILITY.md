# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-23T23:19:59.503789+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`54.14%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `870` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `677` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `136` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+92.4s` (`1.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+1.5s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 366 | 42.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 204 | 23.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 87 | 10.0% |
| 🔴 **Severe Delay** | Over 15m late | 19 | 2.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 136 | 15.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 57 | 6.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 61** | 13 | 4 | 8 | **`61.54%`** | `66.67%` | `+3.7m` |
| **Route 25** | 5 | 2 | 3 | **`60.0%`** | `100.0%` | `-39.0s` |
| **Route 921** | 23 | 8 | 12 | **`52.17%`** | `63.64%` | `+3.8m` |
| **Route 10** | 25 | 9 | 13 | **`52.0%`** | `100.0%` | `+0.1m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.5m` |
| **Route 538** | 11 | 3 | 4 | **`36.36%`** | `85.71%` | `+1.3m` |
| **Route 11** | 18 | 10 | 6 | **`33.33%`** | `85.71%` | `+0.5m` |
| **Route 17** | 18 | 10 | 6 | **`33.33%`** | `100.0%` | `-55.6s` |
| **Route 36** | 12 | 6 | 4 | **`33.33%`** | `50.0%` | `+0.3m` |
| **Route 223** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `+0.3m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 673** | `+27.5 min (1650.0s)` | `+54.6 min (3276s)` | 2 | `50.0%` |
| **Route 790** | `+11.5 min (692.0s)` | `+11.5 min (692s)` | 1 | `0.0%` |
| **Route 113** | `+6.7 min (402.0s)` | `+6.7 min (402s)` | 1 | `0.0%` |
| **Route 781** | `+6.0 min (358.0s)` | `+9.6 min (576s)` | 2 | `50.0%` |
| **Route 904** | `+5.2 min (313.0s)` | `+13.7 min (824s)` | 9 | `46.67%` |
| **Route 698** | `+4.6 min (278.5s)` | `+8.7 min (523s)` | 2 | `50.0%` |
| **Route 645** | `+4.5 min (268.2s)` | `+14.9 min (896s)` | 5 | `60.0%` |
| **Route 9** | `+4.2 min (251.9s)` | `+28.3 min (1699s)` | 8 | `50.0%` |
| **Route 2** | `+3.8 min (227.6s)` | `+28.4 min (1707s)` | 14 | `70.59%` |
| **Route 921** | `+3.8 min (226.9s)` | `+13.3 min (798s)` | 8 | `63.64%` |

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
| `1325594` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325648` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325715` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325784` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325809` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326072` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326110` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326291` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326327` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326499` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326527` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326779` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319708` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319762` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-23 23:19:59` | `15.63%` | `54.14%` | 870 | 677 | `+92.4s` |
| `2026-09-23 20:50:54` | `15.16%` | `57.52%` | 1148 | 919 | `+80.1s` |
| `2026-09-23 17:34:40` | `18.14%` | `57.32%` | 948 | 746 | `+10.8s` |
| `2026-09-23 12:33:17` | `14.94%` | `60.59%` | 964 | 818 | `+82.3s` |
| `2026-09-23 06:58:05` | `0.0%` | `80.0%` | 5 | 5 | `+16.6s` |
| `2026-09-22 23:04:38` | `13.54%` | `51.67%` | 886 | 720 | `+81.8s` |
| `2026-09-22 20:19:25` | `16.97%` | `58.02%` | 1155 | 910 | `+57.0s` |
| `2026-09-22 17:26:26` | `18.48%` | `57.47%` | 958 | 743 | `+26.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-23T23:19:59.503789+00:00`.*
