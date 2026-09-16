# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-16T12:18:43.297821+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.35%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.12%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `977` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `825` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `150` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+34.1s` (`0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-6.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 496 | 50.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 280 | 28.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 44 | 4.5% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 150 | 15.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 30** | 7 | 2 | 4 | **`57.14%`** | `100.0%` | `-89.7s` |
| **Route 11** | 25 | 9 | 14 | **`56.0%`** | `100.0%` | `-86.8s` |
| **Route 921** | 20 | 6 | 10 | **`50.0%`** | `100.0%` | `+0.7m` |
| **Route 18** | 25 | 10 | 11 | **`44.0%`** | `90.91%` | `+0.8m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.5m` |
| **Route 10** | 24 | 10 | 10 | **`41.67%`** | `63.64%` | `+2.8m` |
| **Route 64** | 25 | 9 | 10 | **`40.0%`** | `88.89%` | `-21.1s` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `+0.4m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-20.5s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.7m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 25** | `+26.3 min (1579.4s)` | `+101.2 min (6069s)` | 6 | `50.0%` |
| **Route 781** | `+13.7 min (823.6s)` | `+97.4 min (5842s)` | 9 | `71.43%` |
| **Route 294** | `+5.3 min (317.0s)` | `+5.3 min (317s)` | 1 | `0.0%` |
| **Route 467** | `+4.0 min (237.3s)` | `+8.6 min (513s)` | 3 | `0.0%` |
| **Route 777** | `+3.5 min (209.3s)` | `+6.3 min (380s)` | 3 | `66.67%` |
| **Route 698** | `+3.4 min (203.9s)` | `+7.2 min (429s)` | 8 | `75.0%` |
| **Route 5** | `+3.2 min (194.0s)` | `+10.4 min (626s)` | 3 | `80.0%` |
| **Route 667** | `+3.0 min (183.0s)` | `+4.5 min (268s)` | 2 | `100.0%` |
| **Route 645** | `+2.9 min (172.8s)` | `+7.0 min (422s)` | 6 | `77.78%` |
| **Route 10** | `+2.8 min (169.3s)` | `+14.7 min (884s)` | 10 | `63.64%` |

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
| `1324979` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325089` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325218` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325352` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326407` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326506` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326907` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326971` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327017` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327118` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317864` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317986` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318353` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318512` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318573` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-16 12:18:43` | `15.35%` | `60.12%` | 977 | 825 | `+34.1s` |
| `2026-09-16 06:30:26` | `0.0%` | `67.74%` | 31 | 31 | `+88.8s` |
| `2026-09-16 01:29:53` | `15.6%` | `64.3%` | 545 | 452 | `+119.4s` |
| `2026-09-15 23:18:53` | `13.72%` | `50.71%` | 831 | 698 | `+110.3s` |
| `2026-09-15 20:38:46` | `15.67%` | `58.47%` | 1104 | 916 | `+80.1s` |
| `2026-09-15 17:42:54` | `17.58%` | `55.84%` | 927 | 752 | `+15.1s` |
| `2026-09-15 13:01:31` | `17.39%` | `55.88%` | 949 | 782 | `+93.1s` |
| `2026-09-15 08:16:19` | `0.0%` | `50.0%` | 20 | 20 | `+-50.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-16T12:18:43.297821+00:00`.*
