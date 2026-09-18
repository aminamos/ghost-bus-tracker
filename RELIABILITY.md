# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-18T15:26:34.788077+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.53%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.64%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `884` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `708` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `155` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+-13.0s` (`-0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-31.0s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 401 | 45.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 279 | 31.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 25 | 2.8% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 155 | 17.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 21 | 2.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 921** | 24 | 8 | 12 | **`50.0%`** | `100.0%` | `-1.4s` |
| **Route 25** | 6 | 3 | 3 | **`50.0%`** | `100.0%` | `-82.0s` |
| **Route 537** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `-4.0s` |
| **Route 18** | 35 | 13 | 16 | **`45.71%`** | `88.89%` | `-24.6s` |
| **Route 11** | 25 | 11 | 11 | **`44.0%`** | `100.0%` | `-40.2s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-46.5s` |
| **Route 10** | 30 | 13 | 12 | **`40.0%`** | `100.0%` | `-1.9s` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `-17.8s` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `-41.0s` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-9.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+9.7 min (583.1s)` | `+35.9 min (2154s)` | 6 | `62.5%` |
| **Route 716** | `+4.1 min (246.3s)` | `+7.8 min (468s)` | 1 | `66.67%` |
| **Route 219** | `+2.5 min (149.1s)` | `+24.2 min (1452s)` | 4 | `50.0%` |
| **Route 904** | `+2.3 min (139.2s)` | `+11.6 min (694s)` | 7 | `91.67%` |
| **Route 71** | `+1.7 min (100.9s)` | `+8.4 min (502s)` | 4 | `83.33%` |
| **Route 5** | `+1.7 min (99.8s)` | `+6.9 min (413s)` | 3 | `66.67%` |
| **Route 902** | `+1.2 min (70.9s)` | `+5.0 min (300s)` | 11 | `100.0%` |
| **Route 901** | `+1.1 min (67.5s)` | `+3.0 min (180s)` | 8 | `100.0%` |
| **Route 542** | `+1.1 min (65.2s)` | `+2.2 min (130s)` | 4 | `100.0%` |
| **Route 923** | `+1.0 min (57.4s)` | `+9.6 min (574s)` | 9 | `91.67%` |

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
| `1324991` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325475` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325816` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326022` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326229` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326262` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326324` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326472` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326546` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326706` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326949` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1330840` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317937` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318029` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318613` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-18 15:26:34` | `17.53%` | `56.64%` | 884 | 708 | `+-13.0s` |
| `2026-09-18 06:08:06` | `7.84%` | `68.09%` | 51 | 47 | `+40.8s` |
| `2026-09-18 01:00:45` | `15.29%` | `66.8%` | 595 | 494 | `+67.2s` |
| `2026-09-17 22:57:58` | `14.59%` | `51.39%` | 905 | 755 | `+97.9s` |
| `2026-09-17 20:26:25` | `17.07%` | `57.79%` | 1113 | 905 | `+61.3s` |
| `2026-09-17 17:10:31` | `17.58%` | `56.41%` | 927 | 745 | `+-5.7s` |
| `2026-09-17 12:18:36` | `15.82%` | `61.21%` | 967 | 812 | `+9.9s` |
| `2026-09-17 06:55:00` | `0.0%` | `100.0%` | 18 | 7 | `+53.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-18T15:26:34.788077+00:00`.*
