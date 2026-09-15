# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-15T13:01:31.067131+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.39%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.88%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `949` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `782` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `165` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+93.1s` (`1.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 437 | 46.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 238 | 25.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 93 | 9.8% |
| 🔴 **Severe Delay** | Over 15m late | 14 | 1.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 165 | 17.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 465** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 475** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 490** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 10** | 23 | 7 | 12 | **`52.17%`** | `83.33%` | `+0.2m` |
| **Route 17** | 26 | 10 | 12 | **`46.15%`** | `83.33%` | `-0.7s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+1.6m` |
| **Route 18** | 26 | 9 | 11 | **`42.31%`** | `70.0%` | `+1.2m` |
| **Route 64** | 25 | 11 | 10 | **`40.0%`** | `81.82%` | `+1.5m` |
| **Route 921** | 20 | 7 | 8 | **`40.0%`** | `100.0%` | `+0.2m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `60.0%` | `+3.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 860** | `+68.1 min (4085.0s)` | `+68.1 min (4085s)` | 1 | `0.0%` |
| **Route 785** | `+34.2 min (2050.0s)` | `+99.6 min (5978s)` | 3 | `33.33%` |
| **Route 46** | `+26.6 min (1597.0s)` | `+70.1 min (4206s)` | 3 | `42.86%` |
| **Route 755** | `+11.0 min (657.5s)` | `+11.8 min (711s)` | 2 | `0.0%` |
| **Route 355** | `+10.8 min (645.0s)` | `+24.6 min (1478s)` | 3 | `33.33%` |
| **Route 667** | `+8.9 min (533.0s)` | `+8.9 min (533s)` | 1 | `0.0%` |
| **Route 270** | `+7.6 min (453.2s)` | `+13.6 min (817s)` | 4 | `25.0%` |
| **Route 777** | `+7.3 min (436.5s)` | `+14.2 min (851s)` | 2 | `50.0%` |
| **Route 363** | `+6.9 min (415.0s)` | `+6.9 min (415s)` | 1 | `0.0%` |
| **Route 25** | `+6.7 min (400.7s)` | `+25.1 min (1505s)` | 4 | `60.0%` |

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
| `1325089` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325352` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325400` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325574` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326014` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326157` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326407` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326493` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326506` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326753` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326916` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327166` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317864` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318512` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318613` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-15 13:01:31` | `17.39%` | `55.88%` | 949 | 782 | `+93.1s` |
| `2026-09-15 08:16:19` | `0.0%` | `50.0%` | 20 | 20 | `+-50.6s` |
| `2026-09-15 07:55:59` | `0.0%` | `100.0%` | 6 | 6 | `+0.0s` |
| `2026-09-15 02:26:54` | `17.03%` | `91.32%` | 458 | 380 | `+62.9s` |
| `2026-09-14 23:35:16` | `16.58%` | `81.7%` | 760 | 634 | `+110.4s` |
| `2026-09-14 20:46:08` | `17.07%` | `80.61%` | 1113 | 923 | `+111.2s` |
| `2026-09-14 16:59:54` | `19.2%` | `86.8%` | 901 | 728 | `+60.5s` |
| `2026-09-14 11:14:14` | `20.62%` | `92.93%` | 873 | 693 | `+40.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-15T13:01:31.067131+00:00`.*
