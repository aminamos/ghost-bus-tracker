# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-04T00:14:05.710393+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.81%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `556` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `498` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `56` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+184.7s` (`3.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+112.0s` (`1.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 342 | 61.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 45 | 8.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 97 | 17.4% |
| 🔴 **Severe Delay** | Over 15m late | 13 | 2.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 56 | 10.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 0.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 25 | 11 | 10 | **`40.0%`** | `71.43%` | `+2.3m` |
| **Route 645** | 5 | 2 | 2 | **`40.0%`** | `33.33%` | `+14.1m` |
| **Route 36** | 11 | 4 | 4 | **`36.36%`** | `100.0%` | `+0.7m` |
| **Route 540** | 6 | 2 | 2 | **`33.33%`** | `100.0%` | `+2.3m` |
| **Route 215** | 3 | 1 | 1 | **`33.33%`** | `100.0%` | `+2.0m` |
| **Route 65** | 7 | 3 | 2 | **`28.57%`** | `100.0%` | `+1.9m` |
| **Route 64** | 16 | 8 | 4 | **`25.0%`** | `55.56%` | `+4.0m` |
| **Route 924** | 30 | 15 | 7 | **`23.33%`** | `68.18%` | `+5.0m` |
| **Route 87** | 9 | 5 | 2 | **`22.22%`** | `100.0%` | `+1.4m` |
| **Route 9** | 14 | 7 | 3 | **`21.43%`** | `66.67%` | `+3.1m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+14.1 min (847.3s)` | `+28.4 min (1706s)` | 2 | `33.33%` |
| **Route 83** | `+11.9 min (716.0s)` | `+11.9 min (716s)` | 1 | `0.0%` |
| **Route 74** | `+8.2 min (492.1s)` | `+39.8 min (2387s)` | 8 | `45.45%` |
| **Route 25** | `+7.0 min (421.3s)` | `+7.7 min (460s)` | 3 | `0.0%` |
| **Route 54** | `+7.0 min (418.2s)` | `+36.7 min (2200s)` | 13 | `62.5%` |
| **Route 17** | `+6.1 min (363.2s)` | `+22.8 min (1369s)` | 6 | `60.0%` |
| **Route 904** | `+5.4 min (322.1s)` | `+12.6 min (755s)` | 7 | `42.86%` |
| **Route 924** | `+5.0 min (301.5s)` | `+34.6 min (2078s)` | 15 | `68.18%` |
| **Route 2** | `+5.0 min (300.5s)` | `+21.2 min (1273s)` | 6 | `58.33%` |
| **Route 27** | `+4.5 min (267.3s)` | `+7.8 min (470s)` | 2 | `66.67%` |

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
| `1334602` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368043` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364989` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365773` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366658` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368067` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368277` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368562` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368698` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368740` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1369160` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1369258` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1265673` | Route 215 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366769` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1367334` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-04 00:14:05` | `10.07%` | `68.81%` | 556 | 498 | `+184.7s` |
| `2026-10-03 21:33:49` | `11.32%` | `65.11%` | 751 | 665 | `+156.0s` |
| `2026-10-03 18:04:11` | `12.62%` | `70.93%` | 753 | 657 | `+130.4s` |
| `2026-10-03 14:04:12` | `17.74%` | `70.54%` | 682 | 560 | `+89.0s` |
| `2026-10-03 08:42:45` | `50.0%` | `73.33%` | 90 | 45 | `+56.7s` |
| `2026-10-03 02:53:57` | `7.89%` | `57.81%` | 431 | 384 | `+89.2s` |
| `2026-10-02 23:53:15` | `8.34%` | `61.71%` | 731 | 637 | `+87.4s` |
| `2026-10-02 15:11:12` | `14.86%` | `55.4%` | 828 | 704 | `+9.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-04T00:14:05.710393+00:00`.*
