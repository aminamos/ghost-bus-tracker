# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T17:57:47.972278+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.16%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `943` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `748` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `116` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+38.7s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-6.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 435 | 46.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 253 | 26.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 56 | 5.9% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 116 | 12.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 79 | 8.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 8 | 3 | 5 | **`62.5%`** | `100.0%` | `+2.1 min` |
| **Route 537** | 4 | 1 | 2 | **`50.0%`** | `50.0%` | `-11.5s` |
| **Route 36** | 10 | 5 | 4 | **`40.0%`** | `33.33%` | `+1.3 min` |
| **Route 721** | 10 | 4 | 4 | **`40.0%`** | `50.0%` | `+3.8 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.2 min` |
| **Route 827** | 5 | 3 | 2 | **`40.0%`** | `66.67%` | `-4.3s` |
| **Route 540** | 11 | 5 | 4 | **`36.36%`** | `42.86%` | `-35.7s` |
| **Route 67** | 12 | 6 | 4 | **`33.33%`** | `50.0%` | `+1.0 min` |
| **Route 18** | 38 | 18 | 12 | **`31.58%`** | `76.92%` | `+0.2 min` |
| **Route 9** | 13 | 9 | 4 | **`30.77%`** | `88.89%` | `+2.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 805** | `+43.2 min (+2591.7s)` | `+105.6 min (+6338s)` | 3 | `0.0%` |
| **Route 781** | `+4.9 min (+295.5s)` | `+9.3 min (+556s)` | 2 | `50.0%` |
| **Route 227** | `+4.0 min (+242.7s)` | `+11.4 min (+682s)` | 2 | `66.67%` |
| **Route 698** | `+3.9 min (+235.5s)` | `+8.6 min (+515s)` | 2 | `50.0%` |
| **Route 721** | `+3.8 min (+230.7s)` | `+16.0 min (+959s)` | 4 | `50.0%` |
| **Route 904** | `+3.5 min (+210.5s)` | `+7.3 min (+437s)` | 7 | `84.62%` |
| **Route 225** | `+2.9 min (+174.3s)` | `+7.2 min (+430s)` | 2 | `66.67%` |
| **Route 725** | `+2.8 min (+168.8s)` | `+6.8 min (+411s)` | 2 | `50.0%` |
| **Route 542** | `+2.3 min (+136.7s)` | `+5.2 min (+312s)` | 4 | `83.33%` |
| **Route 723** | `+2.2 min (+129.3s)` | `+9.8 min (+590s)` | 2 | `66.67%` |

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
| `1324974` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325632` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325813` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325980` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326096` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318288` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365064` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365582` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365792` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366126` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332584` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332687` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333002` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333141` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 17:57:47` | `12.3%` | `58.16%` | 943 | 748 | `+38.7s` |
| `2026-10-05 17:20:37` | `12.38%` | `58.27%` | 945 | 762 | `+20.1s` |
| `2026-10-05 16:34:15` | `12.45%` | `58.06%` | 932 | 751 | `+17.6s` |
| `2026-10-05 12:15:23` | `10.84%` | `63.85%` | 950 | 805 | `+30.8s` |
| `2026-10-05 12:14:27` | `11.02%` | `64.16%` | 944 | 798 | `+31.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T17:57:47.972278+00:00`.*
