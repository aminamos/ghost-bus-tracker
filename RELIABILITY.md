# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-19T01:20:14.068342+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.47%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`67.6%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `569` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `463` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `88` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+53.6s` (`0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+10.0s` (`0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 313 | 55.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 111 | 19.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 35 | 6.2% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 88 | 15.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 18 | 3.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 25 | 9 | 13 | **`52.0%`** | `100.0%` | `-15.7s` |
| **Route 11** | 13 | 4 | 6 | **`46.15%`** | `83.33%` | `+2.0m` |
| **Route 921** | 21 | 6 | 9 | **`42.86%`** | `100.0%` | `-31.5s` |
| **Route 540** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `+0.2m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.9m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `-20.7s` |
| **Route 64** | 13 | 5 | 5 | **`38.46%`** | `87.5%` | `+1.4m` |
| **Route 10** | 21 | 7 | 8 | **`38.1%`** | `88.89%` | `+0.3m` |
| **Route 36** | 12 | 6 | 4 | **`33.33%`** | `100.0%` | `+0.2m` |
| **Route 68** | 12 | 7 | 4 | **`33.33%`** | `85.71%` | `+2.2m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 903** | `+11.2 min (673.6s)` | `+25.9 min (1554s)` | 2 | `40.0%` |
| **Route 925** | `+4.0 min (242.4s)` | `+29.5 min (1770s)` | 13 | `77.78%` |
| **Route 22** | `+3.2 min (194.2s)` | `+9.3 min (558s)` | 10 | `72.73%` |
| **Route 904** | `+3.0 min (181.2s)` | `+7.8 min (468s)` | 8 | `69.23%` |
| **Route 63** | `+2.4 min (141.9s)` | `+8.7 min (523s)` | 5 | `87.5%` |
| **Route 32** | `+2.4 min (141.0s)` | `+4.0 min (240s)` | 2 | `100.0%` |
| **Route 54** | `+2.3 min (138.5s)` | `+7.2 min (432s)` | 11 | `86.67%` |
| **Route 716** | `+2.3 min (136.0s)` | `+2.3 min (136s)` | 1 | `100.0%` |
| **Route 68** | `+2.2 min (134.0s)` | `+8.2 min (491s)` | 7 | `85.71%` |
| **Route 11** | `+2.0 min (120.0s)` | `+11.8 min (711s)` | 4 | `83.33%` |

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
| `1325784` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325968` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326479` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326639` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327013` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318421` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319093` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319879` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348999` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350049` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351263` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332519` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-19 01:20:14` | `15.47%` | `67.6%` | 569 | 463 | `+53.6s` |
| `2026-09-18 21:21:42` | `14.29%` | `55.31%` | 1120 | 905 | `+107.1s` |
| `2026-09-18 18:35:51` | `18.28%` | `55.26%` | 979 | 751 | `+9.8s` |
| `2026-09-18 15:26:34` | `17.53%` | `56.64%` | 884 | 708 | `+-13.0s` |
| `2026-09-18 06:08:06` | `7.84%` | `68.09%` | 51 | 47 | `+40.8s` |
| `2026-09-18 01:00:45` | `15.29%` | `66.8%` | 595 | 494 | `+67.2s` |
| `2026-09-17 22:57:58` | `14.59%` | `51.39%` | 905 | 755 | `+97.9s` |
| `2026-09-17 20:26:25` | `17.07%` | `57.79%` | 1113 | 905 | `+61.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-19T01:20:14.068342+00:00`.*
