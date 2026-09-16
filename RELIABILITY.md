# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-16T17:10:13.693836+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.17%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`56.19%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `919` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `751` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `167` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+16.9s` (`0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-12.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 422 | 45.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 265 | 28.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 58 | 6.3% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 0.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 167 | 18.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 6 | 2 | 4 | **`66.67%`** | `100.0%` | `-197.5s` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `-35.0s` |
| **Route 18** | 36 | 16 | 16 | **`44.44%`** | `85.71%` | `+0.6m` |
| **Route 9** | 14 | 6 | 6 | **`42.86%`** | `80.0%` | `+1.2m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-17.5s` |
| **Route 10** | 34 | 14 | 14 | **`41.18%`** | `66.67%` | `-59.9s` |
| **Route 11** | 25 | 12 | 10 | **`40.0%`** | `75.0%` | `-94.0s` |
| **Route 921** | 31 | 11 | 12 | **`38.71%`** | `92.31%` | `-28.8s` |
| **Route 64** | 24 | 12 | 9 | **`37.5%`** | `90.0%` | `+0.4m` |
| **Route 17** | 27 | 11 | 10 | **`37.04%`** | `92.31%` | `+0.3m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 114** | `+5.9 min (353.0s)` | `+5.9 min (353s)` | 1 | `0.0%` |
| **Route 904** | `+4.6 min (273.4s)` | `+19.6 min (1179s)` | 9 | `64.29%` |
| **Route 925** | `+4.5 min (270.6s)` | `+38.8 min (2330s)` | 20 | `60.0%` |
| **Route 698** | `+3.9 min (231.3s)` | `+7.8 min (467s)` | 3 | `66.67%` |
| **Route 801** | `+2.8 min (167.3s)` | `+9.4 min (566s)` | 2 | `50.0%` |
| **Route 94** | `+2.6 min (156.9s)` | `+10.4 min (627s)` | 5 | `90.0%` |
| **Route 923** | `+2.3 min (136.0s)` | `+12.4 min (746s)` | 11 | `83.33%` |
| **Route 645** | `+2.1 min (124.2s)` | `+5.0 min (301s)` | 5 | `87.5%` |
| **Route 4** | `+2.0 min (121.9s)` | `+19.0 min (1138s)` | 13 | `70.0%` |
| **Route 725** | `+1.7 min (99.5s)` | `+2.4 min (144s)` | 2 | `100.0%` |

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
| `1325320` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325475` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325697` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325814` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325819` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325994` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326177` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326195` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326346` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326353` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326498` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326587` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326661` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317828` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-16 17:10:13` | `18.17%` | `56.19%` | 919 | 751 | `+16.9s` |
| `2026-09-16 12:18:43` | `15.35%` | `60.12%` | 977 | 825 | `+34.1s` |
| `2026-09-16 06:30:26` | `0.0%` | `67.74%` | 31 | 31 | `+88.8s` |
| `2026-09-16 01:29:53` | `15.6%` | `64.3%` | 545 | 452 | `+119.4s` |
| `2026-09-15 23:18:53` | `13.72%` | `50.71%` | 831 | 698 | `+110.3s` |
| `2026-09-15 20:38:46` | `15.67%` | `58.47%` | 1104 | 916 | `+80.1s` |
| `2026-09-15 17:42:54` | `17.58%` | `55.84%` | 927 | 752 | `+15.1s` |
| `2026-09-15 13:01:31` | `17.39%` | `55.88%` | 949 | 782 | `+93.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-16T17:10:13.693836+00:00`.*
