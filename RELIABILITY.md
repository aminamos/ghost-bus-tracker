# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T02:10:28.251748+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.4%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`67.17%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `386` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `332` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `44` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+204.7s` (`3.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+156.5s` (`2.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 223 | 57.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 27 | 7.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 76 | 19.7% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 1.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 44 | 11.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 10 | 2.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 9** | 7 | 3 | 3 | **`42.86%`** | `75.0%` | `+3.9m` |
| **Route 36** | 10 | 4 | 4 | **`40.0%`** | `83.33%` | `+2.3m` |
| **Route 2** | 12 | 5 | 4 | **`33.33%`** | `57.14%` | `+3.7m` |
| **Route 3** | 14 | 6 | 4 | **`28.57%`** | `33.33%` | `+6.9m` |
| **Route 68** | 11 | 5 | 3 | **`27.27%`** | `87.5%` | `+4.0m` |
| **Route 18** | 23 | 11 | 6 | **`26.09%`** | `78.57%` | `+1.9m` |
| **Route 924** | 25 | 12 | 6 | **`24.0%`** | `82.35%` | `+3.6m` |
| **Route 925** | 21 | 9 | 5 | **`23.81%`** | `50.0%` | `+5.3m` |
| **Route 63** | 9 | 5 | 2 | **`22.22%`** | `71.43%` | `+2.9m` |
| **Route 64** | 10 | 4 | 2 | **`20.0%`** | `33.33%` | `+3.7m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 22** | `+10.2 min (612.3s)` | `+50.0 min (3000s)` | 9 | `50.0%` |
| **Route 54** | `+8.3 min (497.7s)` | `+17.1 min (1024s)` | 6 | `44.44%` |
| **Route 10** | `+7.3 min (436.1s)` | `+16.2 min (975s)` | 5 | `25.0%` |
| **Route 3** | `+6.9 min (413.6s)` | `+12.4 min (744s)` | 6 | `33.33%` |
| **Route 30** | `+6.8 min (411.0s)` | `+6.8 min (411s)` | 1 | `0.0%` |
| **Route 27** | `+5.8 min (351.0s)` | `+10.3 min (618s)` | 2 | `50.0%` |
| **Route 923** | `+5.4 min (324.3s)` | `+17.4 min (1044s)` | 6 | `61.54%` |
| **Route 925** | `+5.3 min (317.1s)` | `+23.1 min (1389s)` | 9 | `50.0%` |
| **Route 4** | `+4.7 min (279.1s)` | `+12.7 min (760s)` | 5 | `71.43%` |
| **Route 802** | `+4.6 min (276.0s)` | `+4.6 min (276s)` | 1 | `100.0%` |

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
| `1331871` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360984` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364439` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365364` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365391` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366737` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368500` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331818` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331862` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360893` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361244` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364438` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1180701` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1182276` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1184400` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 02:10:28` | `11.4%` | `67.17%` | 386 | 332 | `+204.7s` |
| `2026-10-04 23:20:57` | `9.43%` | `61.8%` | 562 | 501 | `+251.0s` |
| `2026-10-04 20:16:15` | `11.44%` | `60.24%` | 673 | 591 | `+290.1s` |
| `2026-10-04 17:11:23` | `17.78%` | `59.12%` | 731 | 592 | `+342.9s` |
| `2026-10-04 12:37:23` | `25.23%` | `74.03%` | 555 | 413 | `+160.6s` |
| `2026-10-04 06:05:55` | `0.0%` | `42.31%` | 52 | 52 | `+138.4s` |
| `2026-10-04 00:14:05` | `10.07%` | `68.81%` | 556 | 498 | `+184.7s` |
| `2026-10-03 21:33:49` | `11.32%` | `65.11%` | 751 | 665 | `+156.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T02:10:28.251748+00:00`.*
