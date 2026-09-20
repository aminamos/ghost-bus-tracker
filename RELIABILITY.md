# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-20T16:38:06.612528+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.7%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`69.73%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `706` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `565` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `132` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+185.1s` (`3.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+139.0s` (`2.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 394 | 55.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 42 | 5.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 125 | 17.7% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 132 | 18.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 9 | 1.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 46** | 6 | 1 | 4 | **`66.67%`** | `100.0%` | `+3.2m` |
| **Route 36** | 10 | 4 | 5 | **`50.0%`** | `80.0%` | `+4.0m` |
| **Route 11** | 23 | 10 | 10 | **`43.48%`** | `72.73%` | `+3.3m` |
| **Route 18** | 36 | 15 | 15 | **`41.67%`** | `90.0%` | `+2.2m` |
| **Route 64** | 15 | 6 | 6 | **`40.0%`** | `88.89%` | `+2.7m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.5m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `+0.7m` |
| **Route 538** | 8 | 2 | 3 | **`37.5%`** | `80.0%` | `+2.1m` |
| **Route 10** | 33 | 14 | 12 | **`36.36%`** | `76.19%` | `+3.6m` |
| **Route 17** | 25 | 10 | 9 | **`36.0%`** | `75.0%` | `+1.9m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5** | `+7.8 min (468.5s)` | `+13.4 min (802s)` | 3 | `25.0%` |
| **Route 22** | `+6.7 min (402.1s)` | `+19.3 min (1159s)` | 10 | `46.15%` |
| **Route 74** | `+6.4 min (385.2s)` | `+24.6 min (1479s)` | 6 | `25.0%` |
| **Route 925** | `+6.2 min (374.5s)` | `+17.6 min (1057s)` | 16 | `42.86%` |
| **Route 3** | `+5.8 min (346.0s)` | `+12.8 min (769s)` | 7 | `50.0%` |
| **Route 725** | `+5.4 min (323.2s)` | `+8.3 min (498s)` | 2 | `50.0%` |
| **Route 904** | `+5.4 min (322.1s)` | `+10.5 min (628s)` | 9 | `50.0%` |
| **Route 54** | `+4.9 min (292.3s)` | `+10.2 min (612s)` | 14 | `53.33%` |
| **Route 9** | `+4.7 min (279.0s)` | `+14.8 min (887s)` | 6 | `66.67%` |
| **Route 14** | `+4.6 min (274.1s)` | `+14.4 min (864s)` | 8 | `69.23%` |

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
| `1325107` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325268` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325404` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325452` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325606` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325946` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325954` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326106` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326373` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326504` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326902` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327135` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317805` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318185` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318200` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-20 16:38:06` | `18.7%` | `69.73%` | 706 | 565 | `+185.1s` |
| `2026-09-20 12:45:08` | `19.49%` | `76.49%` | 513 | 404 | `+116.4s` |
| `2026-09-20 07:50:25` | `0.0%` | `100.0%` | 4 | 4 | `+68.2s` |
| `2026-09-20 02:21:35` | `16.33%` | `70.92%` | 447 | 368 | `+162.2s` |
| `2026-09-19 23:49:14` | `13.98%` | `71.89%` | 615 | 523 | `+139.8s` |
| `2026-09-19 21:56:09` | `17.13%` | `67.68%` | 759 | 622 | `+110.3s` |
| `2026-09-19 17:35:31` | `21.22%` | `71.71%` | 787 | 617 | `+125.3s` |
| `2026-09-19 14:34:03` | `21.62%` | `72.91%` | 717 | 561 | `+80.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-20T16:38:06.612528+00:00`.*
