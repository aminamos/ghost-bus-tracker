# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-16T23:04:33.512300+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`47.86%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `910` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `746` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `129` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+188.2s` (`3.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+15.5s` (`0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 357 | 39.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 210 | 23.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 114 | 12.5% |
| 🔴 **Severe Delay** | Over 15m late | 65 | 7.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 129 | 14.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 35 | 3.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 921** | 24 | 9 | 12 | **`50.0%`** | `77.78%` | `+0.8m` |
| **Route 65** | 9 | 3 | 4 | **`44.44%`** | `0.0%` | `+6.5m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-35.0s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.5m` |
| **Route 30** | 8 | 3 | 3 | **`37.5%`** | `75.0%` | `+0.9m` |
| **Route 36** | 11 | 4 | 4 | **`36.36%`** | `66.67%` | `+2.5m` |
| **Route 538** | 11 | 3 | 4 | **`36.36%`** | `100.0%` | `-5.4s` |
| **Route 10** | 28 | 15 | 10 | **`35.71%`** | `63.64%` | `+0.2m` |
| **Route 18** | 28 | 13 | 10 | **`35.71%`** | `77.78%` | `+0.4m` |
| **Route 540** | 12 | 6 | 4 | **`33.33%`** | `71.43%` | `+1.9m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 667** | `+54.7 min (3280.0s)` | `+54.7 min (3280s)` | 1 | `0.0%` |
| **Route 784** | `+48.6 min (2917.0s)` | `+92.2 min (5532s)` | 2 | `0.0%` |
| **Route 776** | `+23.6 min (1414.0s)` | `+23.6 min (1414s)` | 1 | `0.0%` |
| **Route 467** | `+22.7 min (1362.5s)` | `+32.9 min (1975s)` | 2 | `0.0%` |
| **Route 645** | `+17.1 min (1025.8s)` | `+37.0 min (2222s)` | 6 | `12.5%` |
| **Route 673** | `+16.7 min (1001.3s)` | `+36.3 min (2179s)` | 2 | `33.33%` |
| **Route 774** | `+15.2 min (911.0s)` | `+32.5 min (1947s)` | 3 | `0.0%` |
| **Route 777** | `+13.3 min (800.8s)` | `+40.7 min (2444s)` | 4 | `0.0%` |
| **Route 925** | `+12.1 min (724.7s)` | `+42.3 min (2536s)` | 18 | `28.0%` |
| **Route 698** | `+11.3 min (680.3s)` | `+24.1 min (1443s)` | 3 | `33.33%` |

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
| `1325344` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325594` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325809` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326039` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326072` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326110` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326527` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326726` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326779` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318481` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319708` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319762` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319967` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349633` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-16 23:04:33` | `14.18%` | `47.86%` | 910 | 746 | `+188.2s` |
| `2026-09-16 20:17:29` | `17.56%` | `58.39%` | 1105 | 883 | `+35.4s` |
| `2026-09-16 17:10:13` | `18.17%` | `56.19%` | 919 | 751 | `+16.9s` |
| `2026-09-16 12:18:43` | `15.35%` | `60.12%` | 977 | 825 | `+34.1s` |
| `2026-09-16 06:30:26` | `0.0%` | `67.74%` | 31 | 31 | `+88.8s` |
| `2026-09-16 01:29:53` | `15.6%` | `64.3%` | 545 | 452 | `+119.4s` |
| `2026-09-15 23:18:53` | `13.72%` | `50.71%` | 831 | 698 | `+110.3s` |
| `2026-09-15 20:38:46` | `15.67%` | `58.47%` | 1104 | 916 | `+80.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-16T23:04:33.512300+00:00`.*
