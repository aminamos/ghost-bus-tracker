# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-15T17:42:54.028976+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.58%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.84%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `927` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `752` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `163` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+15.1s` (`0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-18.0s` (`-0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 416 | 44.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 274 | 29.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 48 | 5.2% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 0.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 163 | 17.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 12 | 1.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 8 | 3 | 4 | **`50.0%`** | `0.0%` | `-172.0s` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `-21.0s` |
| **Route 768** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `-2.0s` |
| **Route 18** | 38 | 16 | 17 | **`44.74%`** | `83.33%` | `+0.5m` |
| **Route 10** | 36 | 14 | 15 | **`41.67%`** | `80.0%` | `-18.5s` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `+0.7m` |
| **Route 850** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `-46.0s` |
| **Route 921** | 33 | 12 | 13 | **`39.39%`** | `93.33%` | `-14.4s` |
| **Route 64** | 23 | 10 | 9 | **`39.13%`** | `72.73%` | `+2.6m` |
| **Route 17** | 26 | 11 | 10 | **`38.46%`** | `90.0%` | `+0.4m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 705** | `+35.1 min (2103.8s)` | `+66.0 min (3962s)` | 2 | `25.0%` |
| **Route 698** | `+5.1 min (307.7s)` | `+15.4 min (926s)` | 3 | `66.67%` |
| **Route 904** | `+3.1 min (188.2s)` | `+9.1 min (545s)` | 7 | `69.23%` |
| **Route 542** | `+3.0 min (177.7s)` | `+6.7 min (400s)` | 4 | `83.33%` |
| **Route 64** | `+2.6 min (155.4s)` | `+18.0 min (1082s)` | 10 | `72.73%` |
| **Route 725** | `+2.0 min (122.0s)` | `+4.6 min (275s)` | 2 | `100.0%` |
| **Route 87** | `+1.8 min (109.0s)` | `+7.0 min (417s)` | 5 | `83.33%` |
| **Route 923** | `+1.8 min (106.5s)` | `+8.2 min (490s)` | 10 | `76.47%` |
| **Route 345** | `+1.5 min (91.0s)` | `+6.5 min (392s)` | 2 | `66.67%` |
| **Route 901** | `+1.4 min (86.2s)` | `+4.0 min (240s)` | 8 | `100.0%` |

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
| `1324974` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325320` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325632` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325697` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325980` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326096` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326177` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326194` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326346` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326415` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326430` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326861` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327089` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327296` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-15 17:42:54` | `17.58%` | `55.84%` | 927 | 752 | `+15.1s` |
| `2026-09-15 13:01:31` | `17.39%` | `55.88%` | 949 | 782 | `+93.1s` |
| `2026-09-15 08:16:19` | `0.0%` | `50.0%` | 20 | 20 | `+-50.6s` |
| `2026-09-15 07:55:59` | `0.0%` | `100.0%` | 6 | 6 | `+0.0s` |
| `2026-09-15 02:26:54` | `17.03%` | `91.32%` | 458 | 380 | `+62.9s` |
| `2026-09-14 23:35:16` | `16.58%` | `81.7%` | 760 | 634 | `+110.4s` |
| `2026-09-14 20:46:08` | `17.07%` | `80.61%` | 1113 | 923 | `+111.2s` |
| `2026-09-14 16:59:54` | `19.2%` | `86.8%` | 901 | 728 | `+60.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-15T17:42:54.028976+00:00`.*
