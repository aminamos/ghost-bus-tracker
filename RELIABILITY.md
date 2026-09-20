# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-09-20T12:45:08.515793+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.49%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`76.49%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `513` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `404` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `100` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+116.4s` (`1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+81.0s` (`1.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 309 | 60.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 38 | 7.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 53 | 10.3% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 100 | 19.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 9 | 1.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 17 | 5 | 9 | **`52.94%`** | `75.0%` | `+3.1m` |
| **Route 67** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `+1.7m` |
| **Route 645** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+4.5m` |
| **Route 36** | 11 | 6 | 5 | **`45.45%`** | `80.0%` | `+2.1m` |
| **Route 538** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-50.2s` |
| **Route 540** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.4m` |
| **Route 10** | 12 | 4 | 5 | **`41.67%`** | `71.43%` | `+3.9m` |
| **Route 64** | 12 | 4 | 5 | **`41.67%`** | `80.0%` | `+2.0m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.4m` |
| **Route 65** | 5 | 2 | 2 | **`40.0%`** | `100.0%` | `+1.0m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 904** | `+6.8 min (405.4s)` | `+23.1 min (1388s)` | 7 | `30.77%` |
| **Route 5** | `+4.7 min (282.2s)` | `+7.7 min (460s)` | 3 | `75.0%` |
| **Route 645** | `+4.5 min (268.0s)` | `+4.5 min (268s)` | 1 | `100.0%` |
| **Route 10** | `+3.9 min (231.9s)` | `+6.0 min (362s)` | 4 | `71.43%` |
| **Route 14** | `+3.9 min (231.9s)` | `+12.2 min (733s)` | 6 | `62.5%` |
| **Route 901** | `+3.9 min (231.4s)` | `+10.0 min (600s)` | 7 | `71.43%` |
| **Route 925** | `+3.8 min (229.9s)` | `+15.8 min (945s)` | 12 | `75.0%` |
| **Route 4** | `+3.7 min (224.5s)` | `+18.6 min (1114s)` | 6 | `87.5%` |
| **Route 902** | `+3.3 min (200.0s)` | `+4.0 min (240s)` | 3 | `100.0%` |
| **Route 923** | `+3.2 min (194.0s)` | `+17.1 min (1024s)` | 7 | `76.92%` |

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
| `1324989` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325055` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326045` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326067` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327070` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317773` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318517` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319316` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349352` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349985` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350173` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1351059` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1353787` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1354193` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331478` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-20 12:45:08` | `19.49%` | `76.49%` | 513 | 404 | `+116.4s` |
| `2026-09-20 07:50:25` | `0.0%` | `100.0%` | 4 | 4 | `+68.2s` |
| `2026-09-20 02:21:35` | `16.33%` | `70.92%` | 447 | 368 | `+162.2s` |
| `2026-09-19 23:49:14` | `13.98%` | `71.89%` | 615 | 523 | `+139.8s` |
| `2026-09-19 21:56:09` | `17.13%` | `67.68%` | 759 | 622 | `+110.3s` |
| `2026-09-19 17:35:31` | `21.22%` | `71.71%` | 787 | 617 | `+125.3s` |
| `2026-09-19 14:34:03` | `21.62%` | `72.91%` | 717 | 561 | `+80.6s` |
| `2026-09-19 13:42:25` | `23.87%` | `74.32%` | 683 | 518 | `+82.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-20T12:45:08.515793+00:00`.*
