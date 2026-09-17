# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-17T17:10:31.537817+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.58%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.41%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `927` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `745` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `163` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+-5.7s` (`-0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-18.0s` (`-0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 418 | 45.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 273 | 29.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 50 | 5.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 163 | 17.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 20 | 2.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 25 | 11 | 12 | **`48.0%`** | `88.89%` | `-138.2s` |
| **Route 18** | 36 | 15 | 17 | **`47.22%`** | `83.33%` | `+0.3m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-34.5s` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `-48.0s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `50.0%` | `+1.7m` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.7m` |
| **Route 64** | 23 | 12 | 9 | **`39.13%`** | `77.78%` | `+0.5m` |
| **Route 921** | 31 | 11 | 12 | **`38.71%`** | `100.0%` | `-6.2s` |
| **Route 10** | 34 | 14 | 13 | **`38.24%`** | `71.43%` | `-96.5s` |
| **Route 17** | 27 | 11 | 10 | **`37.04%`** | `81.82%` | `+0.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 698** | `+6.1 min (366.7s)` | `+10.3 min (620s)` | 3 | `33.33%` |
| **Route 901** | `+5.6 min (337.5s)` | `+13.0 min (780s)` | 8 | `50.0%` |
| **Route 94** | `+2.4 min (144.6s)` | `+5.6 min (338s)` | 5 | `80.0%` |
| **Route 725** | `+1.8 min (106.5s)` | `+2.4 min (142s)` | 2 | `100.0%` |
| **Route 215** | `+1.7 min (99.3s)` | `+6.0 min (357s)` | 1 | `50.0%` |
| **Route 546** | `+1.6 min (93.7s)` | `+5.4 min (324s)` | 4 | `83.33%` |
| **Route 902** | `+1.5 min (92.7s)` | `+4.0 min (240s)` | 11 | `100.0%` |
| **Route 923** | `+1.5 min (91.2s)` | `+8.1 min (488s)` | 11 | `94.44%` |
| **Route 80** | `+1.3 min (78.2s)` | `+5.8 min (346s)` | 2 | `80.0%` |
| **Route 645** | `+1.3 min (77.5s)` | `+5.1 min (306s)` | 5 | `87.5%` |

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
| `1325320` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325697` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325814` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325819` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325994` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326177` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326195` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326346` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326353` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326587` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326661` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317828` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318093` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-17 17:10:31` | `17.58%` | `56.41%` | 927 | 745 | `+-5.7s` |
| `2026-09-17 12:18:36` | `15.82%` | `61.21%` | 967 | 812 | `+9.9s` |
| `2026-09-17 06:55:00` | `0.0%` | `100.0%` | 18 | 7 | `+53.1s` |
| `2026-09-17 01:33:58` | `15.52%` | `64.73%` | 567 | 448 | `+104.1s` |
| `2026-09-16 23:04:33` | `14.18%` | `47.86%` | 910 | 746 | `+188.2s` |
| `2026-09-16 20:17:29` | `17.56%` | `58.39%` | 1105 | 883 | `+35.4s` |
| `2026-09-16 17:10:13` | `18.17%` | `56.19%` | 919 | 751 | `+16.9s` |
| `2026-09-16 12:18:43` | `15.35%` | `60.12%` | 977 | 825 | `+34.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-17T17:10:31.537817+00:00`.*
