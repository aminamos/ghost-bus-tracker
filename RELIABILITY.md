# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-18T21:21:42.921721+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.31%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1120` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `905` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `160` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+107.1s` (`1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+20.5s` (`0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 500 | 44.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 252 | 22.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 122 | 10.9% |
| 🔴 **Severe Delay** | Over 15m late | 30 | 2.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 160 | 14.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 55 | 4.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 8 | 4 | 4 | **`50.0%`** | `66.67%` | `+0.8m` |
| **Route 850** | 6 | 3 | 3 | **`50.0%`** | `100.0%` | `-43.0s` |
| **Route 824** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-130.0s` |
| **Route 921** | 32 | 10 | 14 | **`43.75%`** | `92.31%` | `+0.7m` |
| **Route 10** | 34 | 14 | 14 | **`41.18%`** | `91.67%` | `-27.9s` |
| **Route 62** | 15 | 6 | 6 | **`40.0%`** | `80.0%` | `-33.2s` |
| **Route 540** | 10 | 6 | 4 | **`40.0%`** | `100.0%` | `+1.4m` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-77.4s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+2.2m` |
| **Route 18** | 36 | 15 | 14 | **`38.89%`** | `57.14%` | `+2.2m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 785** | `+33.1 min (1983.7s)` | `+74.7 min (4482s)` | 2 | `0.0%` |
| **Route 860** | `+30.6 min (1836.5s)` | `+62.0 min (3723s)` | 2 | `50.0%` |
| **Route 134** | `+17.8 min (1070.0s)` | `+17.8 min (1070s)` | 1 | `0.0%` |
| **Route 667** | `+12.2 min (733.5s)` | `+24.4 min (1463s)` | 2 | `50.0%` |
| **Route 645** | `+8.1 min (487.1s)` | `+33.2 min (1990s)` | 6 | `44.44%` |
| **Route 790** | `+6.8 min (405.8s)` | `+20.1 min (1206s)` | 4 | `33.33%` |
| **Route 673** | `+6.7 min (400.6s)` | `+21.1 min (1266s)` | 4 | `60.0%` |
| **Route 904** | `+6.6 min (394.9s)` | `+26.9 min (1616s)` | 13 | `52.38%` |
| **Route 777** | `+6.1 min (366.7s)` | `+11.4 min (684s)` | 3 | `0.0%` |
| **Route 698** | `+6.0 min (361.8s)` | `+24.0 min (1442s)` | 9 | `66.67%` |

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
| `1325186` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325556` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325648` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325853` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325924` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326040` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326050` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326066` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326291` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326490` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326499` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326765` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326831` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327195` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317955` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-18 21:21:42` | `14.29%` | `55.31%` | 1120 | 905 | `+107.1s` |
| `2026-09-18 18:35:51` | `18.28%` | `55.26%` | 979 | 751 | `+9.8s` |
| `2026-09-18 15:26:34` | `17.53%` | `56.64%` | 884 | 708 | `+-13.0s` |
| `2026-09-18 06:08:06` | `7.84%` | `68.09%` | 51 | 47 | `+40.8s` |
| `2026-09-18 01:00:45` | `15.29%` | `66.8%` | 595 | 494 | `+67.2s` |
| `2026-09-17 22:57:58` | `14.59%` | `51.39%` | 905 | 755 | `+97.9s` |
| `2026-09-17 20:26:25` | `17.07%` | `57.79%` | 1113 | 905 | `+61.3s` |
| `2026-09-17 17:10:31` | `17.58%` | `56.41%` | 927 | 745 | `+-5.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-18T21:21:42.921721+00:00`.*
