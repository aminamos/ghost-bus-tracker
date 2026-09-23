# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-23T20:50:54.759371+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.16%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.52%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1148` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `919` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `174` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+80.1s` (`1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+14.5s` (`0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 528 | 46.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 246 | 21.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 134 | 11.7% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 0.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 174 | 15.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 55 | 4.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 921** | 34 | 11 | 16 | **`47.06%`** | `70.59%` | `+3.1m` |
| **Route 10** | 36 | 15 | 16 | **`44.44%`** | `90.91%` | `-13.4s` |
| **Route 17** | 27 | 13 | 11 | **`40.74%`** | `72.73%` | `+1.2m` |
| **Route 645** | 10 | 5 | 4 | **`40.0%`** | `60.0%` | `+2.5m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `33.33%` | `+2.7m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-0.7s` |
| **Route 850** | 8 | 4 | 3 | **`37.5%`** | `100.0%` | `+1.0m` |
| **Route 64** | 27 | 11 | 10 | **`37.04%`** | `50.0%` | `+1.6m` |
| **Route 25** | 11 | 5 | 4 | **`36.36%`** | `66.67%` | `+0.3m` |
| **Route 538** | 11 | 3 | 4 | **`36.36%`** | `85.71%` | `+1.2m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 467** | `+8.5 min (509.2s)` | `+14.9 min (892s)` | 4 | `25.0%` |
| **Route 777** | `+6.7 min (404.3s)` | `+9.6 min (575s)` | 3 | `33.33%` |
| **Route 667** | `+5.8 min (346.0s)` | `+11.5 min (692s)` | 2 | `50.0%` |
| **Route 904** | `+5.2 min (311.9s)` | `+14.4 min (863s)` | 11 | `52.17%` |
| **Route 87** | `+4.8 min (288.1s)` | `+23.3 min (1398s)` | 6 | `66.67%` |
| **Route 540** | `+4.6 min (273.8s)` | `+17.4 min (1046s)` | 5 | `50.0%` |
| **Route 27** | `+4.4 min (263.2s)` | `+15.5 min (928s)` | 3 | `66.67%` |
| **Route 48** | `+4.3 min (259.2s)` | `+10.2 min (614s)` | 2 | `50.0%` |
| **Route 673** | `+4.2 min (250.6s)` | `+11.6 min (693s)` | 4 | `80.0%` |
| **Route 5** | `+3.7 min (219.3s)` | `+8.0 min (482s)` | 5 | `50.0%` |

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
| `1325186` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325247` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325344` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325648` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325924` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326013` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326050` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326066` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326160` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326370` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326526` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326831` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326865` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327099` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-23 20:50:54` | `15.16%` | `57.52%` | 1148 | 919 | `+80.1s` |
| `2026-09-23 17:34:40` | `18.14%` | `57.32%` | 948 | 746 | `+10.8s` |
| `2026-09-23 12:33:17` | `14.94%` | `60.59%` | 964 | 818 | `+82.3s` |
| `2026-09-23 06:58:05` | `0.0%` | `80.0%` | 5 | 5 | `+16.6s` |
| `2026-09-22 23:04:38` | `13.54%` | `51.67%` | 886 | 720 | `+81.8s` |
| `2026-09-22 20:19:25` | `16.97%` | `58.02%` | 1155 | 910 | `+57.0s` |
| `2026-09-22 17:26:26` | `18.48%` | `57.47%` | 958 | 743 | `+26.2s` |
| `2026-09-22 12:43:14` | `15.64%` | `59.95%` | 959 | 803 | `+72.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-23T20:50:54.759371+00:00`.*
