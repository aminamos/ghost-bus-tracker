# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-04T17:11:23.795041+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.78%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.12%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `731` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `592` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `130` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+342.9s` (`5.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+208.5s` (`3.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 350 | 47.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 32 | 4.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 157 | 21.5% |
| 🔴 **Severe Delay** | Over 15m late | 53 | 7.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 130 | 17.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 9 | 1.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 83** | 11 | 1 | 9 | **`81.82%`** | `100.0%` | `-3.5s` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+3.3m` |
| **Route 888** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-66.0s` |
| **Route 36** | 11 | 4 | 5 | **`45.45%`** | `83.33%` | `+2.7m` |
| **Route 921** | 34 | 11 | 14 | **`41.18%`** | `26.32%` | `+13.4m` |
| **Route 72** | 10 | 4 | 4 | **`40.0%`** | `80.0%` | `+2.5m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+14.8m` |
| **Route 63** | 18 | 7 | 7 | **`38.89%`** | `60.0%` | `+5.0m` |
| **Route 540** | 8 | 2 | 3 | **`37.5%`** | `100.0%` | `+2.4m` |
| **Route 62** | 11 | 4 | 4 | **`36.36%`** | `83.33%` | `+2.7m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 645** | `+24.3 min (1457.8s)` | `+33.9 min (2034s)` | 3 | `0.0%` |
| **Route 7** | `+20.8 min (1249.0s)` | `+50.4 min (3026s)` | 6 | `22.22%` |
| **Route 924** | `+16.1 min (967.0s)` | `+55.3 min (3320s)` | 18 | `28.12%` |
| **Route 65** | `+14.8 min (891.0s)` | `+16.6 min (999s)` | 2 | `0.0%` |
| **Route 46** | `+14.1 min (845.5s)` | `+26.9 min (1612s)` | 2 | `25.0%` |
| **Route 921** | `+13.4 min (804.9s)` | `+43.9 min (2631s)` | 11 | `26.32%` |
| **Route 22** | `+11.0 min (662.7s)` | `+30.2 min (1815s)` | 9 | `36.36%` |
| **Route 67** | `+10.5 min (629.0s)` | `+20.0 min (1198s)` | 5 | `25.0%` |
| **Route 87** | `+10.4 min (623.8s)` | `+22.2 min (1332s)` | 3 | `25.0%` |
| **Route 38** | `+9.6 min (578.2s)` | `+23.0 min (1378s)` | 7 | `12.5%` |

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
| `1331575` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331651` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332092` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332197` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1241556` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1242317` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361331` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361825` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1362090` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365262` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365615` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365876` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365972` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366467` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366921` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-04 17:11:23` | `17.78%` | `59.12%` | 731 | 592 | `+342.9s` |
| `2026-10-04 12:37:23` | `25.23%` | `74.03%` | 555 | 413 | `+160.6s` |
| `2026-10-04 06:05:55` | `0.0%` | `42.31%` | 52 | 52 | `+138.4s` |
| `2026-10-04 00:14:05` | `10.07%` | `68.81%` | 556 | 498 | `+184.7s` |
| `2026-10-03 21:33:49` | `11.32%` | `65.11%` | 751 | 665 | `+156.0s` |
| `2026-10-03 18:04:11` | `12.62%` | `70.93%` | 753 | 657 | `+130.4s` |
| `2026-10-03 14:04:12` | `17.74%` | `70.54%` | 682 | 560 | `+89.0s` |
| `2026-10-03 08:42:45` | `50.0%` | `73.33%` | 90 | 45 | `+56.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-04T17:11:23.795041+00:00`.*
