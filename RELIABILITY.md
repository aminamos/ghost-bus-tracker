# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-22T12:43:14.596149+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.64%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.95%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `959` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `803` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `150` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+72.9s` (`1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 479 | 49.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 250 | 26.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 58 | 6.0% |
| 🔴 **Severe Delay** | Over 15m late | 12 | 1.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 150 | 15.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 8 | 0.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 534** | 5 | 1 | 3 | **`60.0%`** | `100.0%` | `-48.5s` |
| **Route 25** | 9 | 3 | 5 | **`55.56%`** | `75.0%` | `+4.1m` |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `-10.5s` |
| **Route 17** | 25 | 11 | 10 | **`40.0%`** | `88.89%` | `+0.6m` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `+0.9m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-6.3s` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.3m` |
| **Route 11** | 26 | 11 | 10 | **`38.46%`** | `100.0%` | `-60.5s` |
| **Route 921** | 21 | 7 | 8 | **`38.1%`** | `91.67%` | `+1.4m` |
| **Route 10** | 24 | 10 | 9 | **`37.5%`** | `90.91%` | `+0.2m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 46** | `+26.6 min (1597.6s)` | `+78.1 min (4688s)` | 4 | `57.14%` |
| **Route 71** | `+23.1 min (1385.5s)` | `+93.5 min (5612s)` | 6 | `57.14%` |
| **Route 784** | `+11.0 min (660.7s)` | `+35.0 min (2100s)` | 3 | `50.0%` |
| **Route 667** | `+9.1 min (543.0s)` | `+9.1 min (543s)` | 1 | `0.0%` |
| **Route 781** | `+8.4 min (505.1s)` | `+80.0 min (4797s)` | 8 | `83.33%` |
| **Route 673** | `+7.0 min (419.6s)` | `+26.0 min (1562s)` | 5 | `80.0%` |
| **Route 860** | `+6.7 min (402.0s)` | `+6.7 min (402s)` | 1 | `0.0%` |
| **Route 698** | `+6.4 min (381.9s)` | `+12.2 min (734s)` | 7 | `28.57%` |
| **Route 134** | `+5.0 min (300.0s)` | `+5.0 min (300s)` | 1 | `100.0%` |
| **Route 764** | `+4.9 min (293.0s)` | `+4.9 min (293s)` | 1 | `100.0%` |

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
| `1325400` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326157` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326407` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326506` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326753` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326907` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326937` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326971` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327166` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317986` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318353` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318512` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319114` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319387` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350279` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-22 12:43:14` | `15.64%` | `59.95%` | 959 | 803 | `+72.9s` |
| `2026-09-22 07:02:34` | `0.0%` | `75.0%` | 5 | 4 | `+-5.5s` |
| `2026-09-22 01:41:09` | `16.23%` | `66.51%` | 530 | 430 | `+65.0s` |
| `2026-09-21 23:25:41` | `15.03%` | `53.0%` | 825 | 666 | `+13.2s` |
| `2026-09-21 20:03:32` | `17.78%` | `59.44%` | 1108 | 864 | `+35.0s` |
| `2026-09-21 15:12:58` | `19.57%` | `57.29%` | 874 | 679 | `+-9.0s` |
| `2026-09-21 08:05:04` | `0.0%` | `53.85%` | 13 | 13 | `+-52.1s` |
| `2026-09-20 23:42:26` | `14.52%` | `62.89%` | 544 | 450 | `+204.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-22T12:43:14.596149+00:00`.*
