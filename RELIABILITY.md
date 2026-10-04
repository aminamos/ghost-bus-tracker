# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-04T20:16:15.040396+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.24%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `673` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `591` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `77` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+290.1s` (`4.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+186.0s` (`3.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 356 | 52.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 42 | 6.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 147 | 21.8% |
| 🔴 **Severe Delay** | Over 15m late | 46 | 6.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 77 | 11.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 5 | 0.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+3.6m` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `25.0%` | `+4.8m` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `66.67%` | `+2.6m` |
| **Route 67** | 12 | 4 | 4 | **`33.33%`** | `25.0%` | `+13.1m` |
| **Route 5** | 6 | 3 | 2 | **`33.33%`** | `33.33%` | `+4.2m` |
| **Route 645** | 6 | 2 | 2 | **`33.33%`** | `0.0%` | `+16.9m` |
| **Route 72** | 6 | 3 | 2 | **`33.33%`** | `50.0%` | `+3.5m` |
| **Route 18** | 37 | 18 | 12 | **`32.43%`** | `63.64%` | `+3.8m` |
| **Route 924** | 40 | 18 | 12 | **`30.0%`** | `55.56%` | `+5.9m` |
| **Route 9** | 14 | 7 | 4 | **`28.57%`** | `44.44%` | `+6.3m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 87** | `+20.8 min (1248.8s)` | `+29.0 min (1741s)` | 3 | `25.0%` |
| **Route 65** | `+19.4 min (1162.3s)` | `+21.2 min (1272s)` | 2 | `0.0%` |
| **Route 645** | `+16.9 min (1015.8s)` | `+27.8 min (1668s)` | 2 | `0.0%` |
| **Route 63** | `+15.0 min (898.5s)` | `+40.2 min (2412s)` | 7 | `20.0%` |
| **Route 921** | `+14.9 min (895.9s)` | `+37.3 min (2240s)` | 9 | `23.53%` |
| **Route 67** | `+13.1 min (785.9s)` | `+30.3 min (1820s)` | 4 | `25.0%` |
| **Route 74** | `+7.8 min (470.9s)` | `+31.8 min (1905s)` | 6 | `57.14%` |
| **Route 54** | `+7.4 min (442.2s)` | `+17.1 min (1029s)` | 10 | `26.67%` |
| **Route 10** | `+7.3 min (438.6s)` | `+26.4 min (1585s)` | 16 | `52.0%` |
| **Route 3** | `+7.3 min (436.2s)` | `+16.4 min (981s)` | 7 | `37.5%` |

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
| `1331511` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331841` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332617` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1239111` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1242823` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361068` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361777` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364200` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364623` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365327` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365677` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365857` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366255` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366938` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1368620` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-04 20:16:15` | `11.44%` | `60.24%` | 673 | 591 | `+290.1s` |
| `2026-10-04 17:11:23` | `17.78%` | `59.12%` | 731 | 592 | `+342.9s` |
| `2026-10-04 12:37:23` | `25.23%` | `74.03%` | 555 | 413 | `+160.6s` |
| `2026-10-04 06:05:55` | `0.0%` | `42.31%` | 52 | 52 | `+138.4s` |
| `2026-10-04 00:14:05` | `10.07%` | `68.81%` | 556 | 498 | `+184.7s` |
| `2026-10-03 21:33:49` | `11.32%` | `65.11%` | 751 | 665 | `+156.0s` |
| `2026-10-03 18:04:11` | `12.62%` | `70.93%` | 753 | 657 | `+130.4s` |
| `2026-10-03 14:04:12` | `17.74%` | `70.54%` | 682 | 560 | `+89.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-04T20:16:15.040396+00:00`.*
