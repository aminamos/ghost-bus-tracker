# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-15T20:38:46.594184+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.67%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.47%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1104` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `916` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `173` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+80.1s` (`1.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+22.0s` (`0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 535 | 48.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 249 | 22.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 119 | 10.8% |
| 🔴 **Severe Delay** | Over 15m late | 12 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 173 | 15.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 15 | 1.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 766** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+4.8m` |
| **Route 18** | 39 | 13 | 20 | **`51.28%`** | `77.78%` | `+0.1m` |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-106.0s` |
| **Route 10** | 37 | 17 | 17 | **`45.95%`** | `75.0%` | `-46.5s` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `60.0%` | `+2.2m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.3m` |
| **Route 921** | 32 | 13 | 12 | **`37.5%`** | `84.62%` | `+0.3m` |
| **Route 25** | 11 | 5 | 4 | **`36.36%`** | `66.67%` | `+2.0m` |
| **Route 538** | 11 | 3 | 4 | **`36.36%`** | `100.0%` | `-10.0s` |
| **Route 540** | 11 | 6 | 4 | **`36.36%`** | `80.0%` | `+2.0m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 467** | `+12.7 min (762.5s)` | `+44.9 min (2696s)` | 4 | `75.0%` |
| **Route 777** | `+7.6 min (456.0s)` | `+7.6 min (456s)` | 1 | `0.0%` |
| **Route 904** | `+5.9 min (356.0s)` | `+21.8 min (1308s)` | 12 | `60.87%` |
| **Route 667** | `+5.5 min (328.0s)` | `+10.9 min (656s)` | 2 | `50.0%` |
| **Route 87** | `+5.3 min (318.4s)` | `+21.5 min (1290s)` | 5 | `50.0%` |
| **Route 113** | `+5.0 min (297.0s)` | `+5.0 min (297s)` | 1 | `100.0%` |
| **Route 766** | `+4.8 min (288.0s)` | `+4.8 min (288s)` | 1 | `100.0%` |
| **Route 673** | `+4.0 min (241.8s)` | `+9.1 min (544s)` | 5 | `80.0%` |
| **Route 785** | `+4.0 min (239.8s)` | `+11.6 min (697s)` | 3 | `75.0%` |
| **Route 790** | `+4.0 min (237.3s)` | `+7.1 min (427s)` | 3 | `66.67%` |

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
| `1325247` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325344` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325432` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325648` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325699` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325774` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325813` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326050` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326066` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326221` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326370` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326419` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326526` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326865` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-15 20:38:46` | `15.67%` | `58.47%` | 1104 | 916 | `+80.1s` |
| `2026-09-15 17:42:54` | `17.58%` | `55.84%` | 927 | 752 | `+15.1s` |
| `2026-09-15 13:01:31` | `17.39%` | `55.88%` | 949 | 782 | `+93.1s` |
| `2026-09-15 08:16:19` | `0.0%` | `50.0%` | 20 | 20 | `+-50.6s` |
| `2026-09-15 07:55:59` | `0.0%` | `100.0%` | 6 | 6 | `+0.0s` |
| `2026-09-15 02:26:54` | `17.03%` | `91.32%` | 458 | 380 | `+62.9s` |
| `2026-09-14 23:35:16` | `16.58%` | `81.7%` | 760 | 634 | `+110.4s` |
| `2026-09-14 20:46:08` | `17.07%` | `80.61%` | 1113 | 923 | `+111.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-15T20:38:46.594184+00:00`.*
