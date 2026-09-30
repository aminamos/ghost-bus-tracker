# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-30T20:53:53.231542+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.62%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1111` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `940` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `127` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+112.1s` (`1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+48.0s` (`0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 551 | 49.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 219 | 19.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 150 | 13.5% |
| 🔴 **Severe Delay** | Over 15m late | 20 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 127 | 11.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 44 | 4.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 5 | 0 | 5 | **`100.0%`** | `0.0%` | `0.0s` |
| **Route 64** | 25 | 10 | 10 | **`40.0%`** | `80.0%` | `+0.6m` |
| **Route 25** | 8 | 4 | 3 | **`37.5%`** | `80.0%` | `+3.6m` |
| **Route 68** | 22 | 10 | 8 | **`36.36%`** | `77.78%` | `+1.8m` |
| **Route 36** | 11 | 4 | 4 | **`36.36%`** | `100.0%` | `-56.1s` |
| **Route 540** | 11 | 5 | 4 | **`36.36%`** | `60.0%` | `+4.7m` |
| **Route 578** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `+0.7m` |
| **Route 18** | 39 | 19 | 12 | **`30.77%`** | `57.89%` | `+3.4m` |
| **Route 9** | 14 | 8 | 4 | **`28.57%`** | `55.56%` | `+4.8m` |
| **Route 223** | 7 | 2 | 2 | **`28.57%`** | `75.0%` | `+1.2m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 774** | `+16.1 min (965.2s)` | `+19.9 min (1191s)` | 6 | `0.0%` |
| **Route 777** | `+11.8 min (709.0s)` | `+14.8 min (890s)` | 2 | `0.0%` |
| **Route 776** | `+8.5 min (509.0s)` | `+12.7 min (762s)` | 3 | `33.33%` |
| **Route 48** | `+7.3 min (439.2s)` | `+20.4 min (1226s)` | 2 | `33.33%` |
| **Route 747** | `+7.3 min (435.2s)` | `+10.2 min (614s)` | 5 | `20.0%` |
| **Route 717** | `+6.9 min (414.0s)` | `+11.2 min (670s)` | 1 | `33.33%` |
| **Route 667** | `+6.2 min (374.0s)` | `+10.5 min (628s)` | 2 | `50.0%` |
| **Route 467** | `+6.1 min (363.5s)` | `+18.2 min (1090s)` | 4 | `75.0%` |
| **Route 9** | `+4.8 min (288.9s)` | `+15.6 min (935s)` | 8 | `55.56%` |
| **Route 540** | `+4.7 min (280.0s)` | `+14.5 min (869s)` | 5 | `60.0%` |

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
| `1325924` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326066` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326526` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326831` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326865` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318481` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319924` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319973` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331480` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331506` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332154` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332799` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317829` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318426` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-30 20:53:53` | `11.43%` | `58.62%` | 1111 | 940 | `+112.1s` |
| `2026-09-30 16:01:00` | `15.07%` | `58.97%` | 889 | 739 | `+9.4s` |
| `2026-09-30 09:22:54` | `35.85%` | `60.0%` | 265 | 170 | `+-36.8s` |
| `2026-09-30 02:59:00` | `9.84%` | `64.85%` | 437 | 367 | `+52.5s` |
| `2026-09-29 23:49:28` | `9.82%` | `59.97%` | 764 | 642 | `+78.4s` |
| `2026-09-29 20:04:44` | `14.44%` | `65.74%` | 1080 | 895 | `+56.5s` |
| `2026-09-29 15:13:43` | `16.15%` | `55.78%` | 836 | 694 | `+-5.4s` |
| `2026-09-29 08:47:30` | `52.17%` | `59.09%` | 138 | 66 | `+-52.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-30T20:53:53.231542+00:00`.*
