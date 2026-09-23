# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit (Bus, METRO Light Rail & BRT) | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-23T12:33:17.717094+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.94%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.59%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `964` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `818` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `144` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+82.3s` (`1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 495 | 51.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 245 | 25.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 56 | 5.8% |
| 🔴 **Severe Delay** | Over 15m late | 21 | 2.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 144 | 14.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 156** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `-158.0s` |
| **Route 17** | 27 | 10 | 12 | **`44.44%`** | `80.0%` | `+1.7m` |
| **Route 10** | 23 | 10 | 10 | **`43.48%`** | `88.89%` | `-15.9s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `+0.1m` |
| **Route 11** | 25 | 11 | 10 | **`40.0%`** | `100.0%` | `-19.0s` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `100.0%` | `+0.9m` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.2m` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.7m` |
| **Route 921** | 21 | 7 | 8 | **`38.1%`** | `76.92%` | `+2.8m` |
| **Route 25** | 8 | 5 | 3 | **`37.5%`** | `60.0%` | `+4.7m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 363** | `+47.2 min (2835.0s)` | `+63.8 min (3829s)` | 2 | `0.0%` |
| **Route 72** | `+20.9 min (1256.1s)` | `+88.4 min (5303s)` | 4 | `57.14%` |
| **Route 46** | `+18.8 min (1129.4s)` | `+65.5 min (3930s)` | 4 | `50.0%` |
| **Route 667** | `+16.3 min (976.0s)` | `+24.8 min (1487s)` | 2 | `0.0%` |
| **Route 784** | `+15.4 min (927.0s)` | `+55.5 min (3330s)` | 4 | `33.33%` |
| **Route 645** | `+12.5 min (750.6s)` | `+33.8 min (2027s)` | 6 | `37.5%` |
| **Route 698** | `+11.5 min (690.8s)` | `+28.7 min (1723s)` | 8 | `44.44%` |
| **Route 673** | `+10.2 min (612.0s)` | `+24.4 min (1467s)` | 6 | `28.57%` |
| **Route 882** | `+8.5 min (509.0s)` | `+8.5 min (509s)` | 1 | `0.0%` |
| **Route 781** | `+6.5 min (388.1s)` | `+52.6 min (3155s)` | 8 | `85.71%` |

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
| `1324979` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326157` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326163` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326407` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326506` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326753` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326907` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326971` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327017` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1327118` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317986` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318400` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318512` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318761` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319114` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-23 12:33:17` | `14.94%` | `60.59%` | 964 | 818 | `+82.3s` |
| `2026-09-23 06:58:05` | `0.0%` | `80.0%` | 5 | 5 | `+16.6s` |
| `2026-09-22 23:04:38` | `13.54%` | `51.67%` | 886 | 720 | `+81.8s` |
| `2026-09-22 20:19:25` | `16.97%` | `58.02%` | 1155 | 910 | `+57.0s` |
| `2026-09-22 17:26:26` | `18.48%` | `57.47%` | 958 | 743 | `+26.2s` |
| `2026-09-22 12:43:14` | `15.64%` | `59.95%` | 959 | 803 | `+72.9s` |
| `2026-09-22 07:02:34` | `0.0%` | `75.0%` | 5 | 4 | `+-5.5s` |
| `2026-09-22 01:41:09` | `16.23%` | `66.51%` | 530 | 430 | `+65.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-23T12:33:17.717094+00:00`.*
