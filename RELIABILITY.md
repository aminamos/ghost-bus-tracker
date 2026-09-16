# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-16T01:29:53.790613+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.6%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.3%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `545` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `452` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `85` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+119.4s` (`2.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+50.0s` (`0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 290 | 53.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 93 | 17.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 55 | 10.1% |
| 🔴 **Severe Delay** | Over 15m late | 13 | 2.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 85 | 15.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 8 | 1.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 23 | 9 | 12 | **`52.17%`** | `57.14%` | `+1.4m` |
| **Route 540** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `+1.1m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.3m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `-47.3s` |
| **Route 9** | 8 | 4 | 3 | **`37.5%`** | `75.0%` | `+1.3m` |
| **Route 921** | 22 | 7 | 8 | **`36.36%`** | `81.82%` | `+1.4m` |
| **Route 62** | 11 | 4 | 4 | **`36.36%`** | `60.0%` | `+2.1m` |
| **Route 17** | 12 | 6 | 4 | **`33.33%`** | `83.33%` | `+2.0m` |
| **Route 723** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `-24.0s` |
| **Route 64** | 13 | 5 | 4 | **`30.77%`** | `77.78%` | `+3.0m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 705** | `+19.7 min (1180.0s)` | `+42.5 min (2550s)` | 2 | `33.33%` |
| **Route 645** | `+14.9 min (892.8s)` | `+33.1 min (1989s)` | 3 | `0.0%` |
| **Route 924** | `+5.6 min (338.1s)` | `+27.6 min (1658s)` | 13 | `66.67%` |
| **Route 716** | `+5.2 min (311.0s)` | `+5.2 min (311s)` | 1 | `0.0%` |
| **Route 54** | `+4.9 min (291.4s)` | `+42.5 min (2550s)` | 11 | `87.5%` |
| **Route 10** | `+4.4 min (262.3s)` | `+24.3 min (1458s)` | 8 | `63.64%` |
| **Route 904** | `+4.2 min (252.5s)` | `+15.6 min (937s)` | 8 | `61.54%` |
| **Route 22** | `+4.0 min (242.9s)` | `+19.5 min (1171s)` | 7 | `77.78%` |
| **Route 2** | `+3.2 min (192.3s)` | `+15.1 min (906s)` | 7 | `77.78%` |
| **Route 64** | `+3.0 min (179.8s)` | `+9.7 min (582s)` | 5 | `77.78%` |

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
| `1325266` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325397` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326479` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326639` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327013` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319879` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348999` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351263` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332519` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332776` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1132530` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1133532` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318967` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319804` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-16 01:29:53` | `15.6%` | `64.3%` | 545 | 452 | `+119.4s` |
| `2026-09-15 23:18:53` | `13.72%` | `50.71%` | 831 | 698 | `+110.3s` |
| `2026-09-15 20:38:46` | `15.67%` | `58.47%` | 1104 | 916 | `+80.1s` |
| `2026-09-15 17:42:54` | `17.58%` | `55.84%` | 927 | 752 | `+15.1s` |
| `2026-09-15 13:01:31` | `17.39%` | `55.88%` | 949 | 782 | `+93.1s` |
| `2026-09-15 08:16:19` | `0.0%` | `50.0%` | 20 | 20 | `+-50.6s` |
| `2026-09-15 07:55:59` | `0.0%` | `100.0%` | 6 | 6 | `+0.0s` |
| `2026-09-15 02:26:54` | `17.03%` | `91.32%` | 458 | 380 | `+62.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-16T01:29:53.790613+00:00`.*
