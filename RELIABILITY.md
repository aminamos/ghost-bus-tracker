# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-23T17:34:40.914857+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.14%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`57.32%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `948` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `746` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `172` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+10.8s` (`0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-8.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 427 | 45.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 266 | 28.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 49 | 5.2% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 172 | 18.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 30 | 3.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 64** | 23 | 11 | 11 | **`47.83%`** | `100.0%` | `-46.9s` |
| **Route 17** | 26 | 9 | 12 | **`46.15%`** | `100.0%` | `-16.9s` |
| **Route 10** | 35 | 13 | 16 | **`45.71%`** | `85.71%` | `-81.2s` |
| **Route 36** | 11 | 5 | 5 | **`45.45%`** | `75.0%` | `+1.5m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.3m` |
| **Route 25** | 7 | 3 | 3 | **`42.86%`** | `50.0%` | `-33.2s` |
| **Route 921** | 34 | 11 | 14 | **`41.18%`** | `73.68%` | `+3.1m` |
| **Route 18** | 35 | 17 | 14 | **`40.0%`** | `92.31%` | `+0.3m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-24.0s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+5.0 min (298.6s)` | `+17.2 min (1033s)` | 8 | `64.29%` |
| **Route 705** | `+3.4 min (205.3s)` | `+10.4 min (626s)` | 2 | `50.0%` |
| **Route 921** | `+3.1 min (187.7s)` | `+11.2 min (671s)` | 11 | `73.68%` |
| **Route 227** | `+2.7 min (161.0s)` | `+5.9 min (355s)` | 2 | `66.67%` |
| **Route 345** | `+2.3 min (139.5s)` | `+9.2 min (554s)` | 2 | `75.0%` |
| **Route 645** | `+2.1 min (123.7s)` | `+7.8 min (466s)` | 5 | `83.33%` |
| **Route 923** | `+2.0 min (122.2s)` | `+7.6 min (455s)` | 11 | `84.21%` |
| **Route 94** | `+1.8 min (107.3s)` | `+3.2 min (194s)` | 6 | `100.0%` |
| **Route 725** | `+1.7 min (100.5s)` | `+3.9 min (231s)` | 2 | `100.0%` |
| **Route 36** | `+1.5 min (92.8s)` | `+10.2 min (610s)` | 5 | `75.0%` |

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
| `1325320` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325475` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325632` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325697` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325980` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325994` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326096` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326177` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326262` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326346` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326353` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326498` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326861` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327089` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-23 17:34:40` | `18.14%` | `57.32%` | 948 | 746 | `+10.8s` |
| `2026-09-23 12:33:17` | `14.94%` | `60.59%` | 964 | 818 | `+82.3s` |
| `2026-09-23 06:58:05` | `0.0%` | `80.0%` | 5 | 5 | `+16.6s` |
| `2026-09-22 23:04:38` | `13.54%` | `51.67%` | 886 | 720 | `+81.8s` |
| `2026-09-22 20:19:25` | `16.97%` | `58.02%` | 1155 | 910 | `+57.0s` |
| `2026-09-22 17:26:26` | `18.48%` | `57.47%` | 958 | 743 | `+26.2s` |
| `2026-09-22 12:43:14` | `15.64%` | `59.95%` | 959 | 803 | `+72.9s` |
| `2026-09-22 07:02:34` | `0.0%` | `75.0%` | 5 | 4 | `+-5.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-23T17:34:40.914857+00:00`.*
