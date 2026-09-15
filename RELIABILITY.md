# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-15T23:18:53.016875+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.72%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.71%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `831` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `698` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `114` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+110.3s` (`1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-1.5s` (`-0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 355 | 42.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 218 | 26.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 100 | 12.0% |
| 🔴 **Severe Delay** | Over 15m late | 27 | 3.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 114 | 13.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 17 | 2.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 26 | 10 | 12 | **`46.15%`** | `62.5%` | `+0.9m` |
| **Route 10** | 26 | 10 | 11 | **`42.31%`** | `60.0%` | `+1.7m` |
| **Route 11** | 17 | 9 | 7 | **`41.18%`** | `100.0%` | `-32.3s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.3m` |
| **Route 25** | 5 | 3 | 2 | **`40.0%`** | `100.0%` | `-61.7s` |
| **Route 538** | 11 | 3 | 4 | **`36.36%`** | `100.0%` | `-14.3s` |
| **Route 540** | 11 | 6 | 4 | **`36.36%`** | `83.33%` | `+1.8m` |
| **Route 921** | 23 | 10 | 8 | **`34.78%`** | `83.33%` | `+1.2m` |
| **Route 62** | 12 | 6 | 4 | **`33.33%`** | `66.67%` | `-109.8s` |
| **Route 9** | 12 | 7 | 4 | **`33.33%`** | `60.0%` | `+1.8m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 113** | `+13.7 min (820.0s)` | `+13.7 min (820s)` | 1 | `0.0%` |
| **Route 705** | `+10.2 min (614.2s)` | `+38.5 min (2312s)` | 2 | `0.0%` |
| **Route 698** | `+8.8 min (531.0s)` | `+21.1 min (1264s)` | 3 | `33.33%` |
| **Route 3** | `+7.7 min (459.9s)` | `+45.5 min (2732s)` | 14 | `40.0%` |
| **Route 777** | `+7.3 min (439.2s)` | `+32.0 min (1922s)` | 4 | `66.67%` |
| **Route 54** | `+7.2 min (432.9s)` | `+28.2 min (1694s)` | 10 | `53.33%` |
| **Route 904** | `+7.0 min (422.5s)` | `+31.3 min (1878s)` | 10 | `50.0%` |
| **Route 645** | `+7.0 min (420.4s)` | `+23.1 min (1384s)` | 6 | `20.0%` |
| **Route 774** | `+6.7 min (404.3s)` | `+12.7 min (759s)` | 3 | `0.0%` |
| **Route 250** | `+6.3 min (378.5s)` | `+12.6 min (753s)` | 2 | `50.0%` |

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
| `1325594` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325715` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325784` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325809` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326039` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326110` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326499` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326526` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326527` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326779` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319708` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319762` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319860` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319967` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-15 23:18:53` | `13.72%` | `50.71%` | 831 | 698 | `+110.3s` |
| `2026-09-15 20:38:46` | `15.67%` | `58.47%` | 1104 | 916 | `+80.1s` |
| `2026-09-15 17:42:54` | `17.58%` | `55.84%` | 927 | 752 | `+15.1s` |
| `2026-09-15 13:01:31` | `17.39%` | `55.88%` | 949 | 782 | `+93.1s` |
| `2026-09-15 08:16:19` | `0.0%` | `50.0%` | 20 | 20 | `+-50.6s` |
| `2026-09-15 07:55:59` | `0.0%` | `100.0%` | 6 | 6 | `+0.0s` |
| `2026-09-15 02:26:54` | `17.03%` | `91.32%` | 458 | 380 | `+62.9s` |
| `2026-09-14 23:35:16` | `16.58%` | `81.7%` | 760 | 634 | `+110.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-15T23:18:53.016875+00:00`.*
