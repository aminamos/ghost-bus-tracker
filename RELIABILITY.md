# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-17T01:33:58.172464+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`64.73%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `567` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `448` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `88` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+104.1s` (`1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+29.0s` (`0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 290 | 51.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 93 | 16.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 58 | 10.2% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 1.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 88 | 15.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 31 | 5.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17** | 12 | 5 | 6 | **`50.0%`** | `80.0%` | `+2.2m` |
| **Route 36** | 10 | 4 | 5 | **`50.0%`** | `75.0%` | `+1.1m` |
| **Route 62** | 8 | 3 | 4 | **`50.0%`** | `100.0%` | `-13.5s` |
| **Route 18** | 24 | 8 | 11 | **`45.83%`** | `57.14%` | `+1.6m` |
| **Route 921** | 21 | 6 | 9 | **`42.86%`** | `90.0%` | `+1.5m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `50.0%` | `+2.7m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `-35.7s` |
| **Route 68** | 12 | 6 | 4 | **`33.33%`** | `100.0%` | `+0.9m` |
| **Route 9** | 9 | 4 | 3 | **`33.33%`** | `60.0%` | `+3.5m` |
| **Route 723** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `-19.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+18.0 min (1082.8s)` | `+63.6 min (3816s)` | 3 | `33.33%` |
| **Route 22** | `+5.9 min (351.1s)` | `+26.4 min (1586s)` | 9 | `61.54%` |
| **Route 87** | `+5.1 min (308.8s)` | `+23.1 min (1386s)` | 5 | `60.0%` |
| **Route 2** | `+4.1 min (246.3s)` | `+18.1 min (1084s)` | 7 | `72.73%` |
| **Route 901** | `+3.7 min (222.0s)` | `+7.5 min (450s)` | 5 | `60.0%` |
| **Route 924** | `+3.5 min (211.1s)` | `+20.2 min (1215s)` | 11 | `66.67%` |
| **Route 716** | `+3.5 min (209.0s)` | `+3.5 min (209s)` | 1 | `100.0%` |
| **Route 9** | `+3.5 min (207.0s)` | `+11.8 min (711s)` | 4 | `60.0%` |
| **Route 904** | `+3.4 min (203.5s)` | `+13.0 min (778s)` | 7 | `76.92%` |
| **Route 11** | `+3.1 min (183.8s)` | `+12.9 min (772s)` | 5 | `57.14%` |

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
| `1325324` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325397` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325888` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326479` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327013` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319569` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319879` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1348999` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351263` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332019` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332519` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332593` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332776` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1131704` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-17 01:33:58` | `15.52%` | `64.73%` | 567 | 448 | `+104.1s` |
| `2026-09-16 23:04:33` | `14.18%` | `47.86%` | 910 | 746 | `+188.2s` |
| `2026-09-16 20:17:29` | `17.56%` | `58.39%` | 1105 | 883 | `+35.4s` |
| `2026-09-16 17:10:13` | `18.17%` | `56.19%` | 919 | 751 | `+16.9s` |
| `2026-09-16 12:18:43` | `15.35%` | `60.12%` | 977 | 825 | `+34.1s` |
| `2026-09-16 06:30:26` | `0.0%` | `67.74%` | 31 | 31 | `+88.8s` |
| `2026-09-16 01:29:53` | `15.6%` | `64.3%` | 545 | 452 | `+119.4s` |
| `2026-09-15 23:18:53` | `13.72%` | `50.71%` | 831 | 698 | `+110.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-17T01:33:58.172464+00:00`.*
