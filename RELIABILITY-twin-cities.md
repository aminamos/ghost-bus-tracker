# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T18:30:37.035000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.91%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.46%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `977` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `773` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `175` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+21.0s` (`+0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-6.5s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 437 | 44.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 276 | 28.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 58 | 5.9% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 175 | 17.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 28 | 2.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 785** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 46** | 10 | 2 | 5 | **`50.0%`** | `40.0%` | `-51.8s` |
| **Route 850** | 6 | 2 | 3 | **`50.0%`** | `33.33%` | `-123.0s` |
| **Route 781** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `+0.9 min` |
| **Route 64** | 27 | 11 | 12 | **`44.44%`** | `80.0%` | `+0.5 min` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `50.0%` | `-38.8s` |
| **Route 534** | 10 | 2 | 4 | **`40.0%`** | `83.33%` | `-14.2s` |
| **Route 539** | 10 | 4 | 4 | **`40.0%`** | `83.33%` | `+0.5 min` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `50.0%` | `+0.4 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+3.7 min (+222.5s)` | `+11.1 min (+667s)` | 8 | `69.23%` |
| **Route 75** | `+3.6 min (+215.0s)` | `+9.1 min (+546s)` | 2 | `75.0%` |
| **Route 9** | `+3.3 min (+196.6s)` | `+25.1 min (+1505s)` | 8 | `44.44%` |
| **Route 345** | `+2.9 min (+175.8s)` | `+10.6 min (+633s)` | 2 | `75.0%` |
| **Route 542** | `+2.4 min (+141.2s)` | `+8.7 min (+522s)` | 5 | `83.33%` |
| **Route 22** | `+2.3 min (+140.5s)` | `+22.4 min (+1343s)` | 16 | `36.36%` |
| **Route 94** | `+2.3 min (+135.8s)` | `+4.9 min (+292s)` | 6 | `100.0%` |
| **Route 11** | `+2.2 min (+133.5s)` | `+9.5 min (+571s)` | 12 | `64.71%` |
| **Route 83** | `+2.2 min (+132.0s)` | `+9.6 min (+577s)` | 2 | `80.0%` |
| **Route 645** | `+2.1 min (+128.9s)` | `+12.9 min (+774s)` | 5 | `71.43%` |

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
| `1131166` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1131478` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1133909` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1134199` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1136024` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1136082` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1187364` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318691` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318988` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319664` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319998` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364825` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365582` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365792` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365913` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 18:30:37` | `17.91%` | `56.46%` | 977 | 773 | `+21.0s` |
| `2026-10-22 15:01:09` | `16.82%` | `53.5%` | 886 | 714 | `-4.2s` |
| `2026-10-22 13:31:54` | `15.92%` | `57.37%` | 911 | 760 | `+35.3s` |
| `2026-10-22 13:03:21` | `14.75%` | `60.8%` | 949 | 801 | `+39.5s` |
| `2026-10-22 12:30:37` | `14.21%` | `67.22%` | 985 | 836 | `+39.0s` |
| `2026-10-22 12:00:40` | `14.89%` | `65.16%` | 967 | 818 | `+11.8s` |
| `2026-10-22 11:30:35` | `16.47%` | `61.36%` | 923 | 766 | `-1.0s` |
| `2026-10-22 11:00:35` | `18.77%` | `59.72%` | 794 | 650 | `-9.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T18:30:37.035000+00:00`.*
