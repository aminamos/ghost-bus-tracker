# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T17:20:37.771374+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.38%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.27%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `945` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `762` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `117` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+20.1s` (`+0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-10.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 444 | 47.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 263 | 27.8% |
| 🟡 **Minor Delay** | +5m to +15m late | 51 | 5.4% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 117 | 12.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 66 | 7.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 6 | 3 | 3 | **`50.0%`** | `33.33%` | `-45.3s` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `75.0%` | `+0.9 min` |
| **Route 540** | 10 | 5 | 4 | **`40.0%`** | `33.33%` | `-45.8s` |
| **Route 721** | 10 | 4 | 4 | **`40.0%`** | `50.0%` | `+6.0 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.2 min` |
| **Route 537** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `+1.3 min` |
| **Route 18** | 38 | 20 | 13 | **`34.21%`** | `60.0%` | `+0.1 min` |
| **Route 924** | 39 | 18 | 13 | **`33.33%`** | `36.0%` | `-22.4s` |
| **Route 36** | 12 | 6 | 4 | **`33.33%`** | `62.5%` | `+2.4 min` |
| **Route 67** | 12 | 6 | 4 | **`33.33%`** | `25.0%` | `-66.1s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 805** | `+14.2 min (+850.3s)` | `+54.5 min (+3272s)` | 3 | `16.67%` |
| **Route 721** | `+6.0 min (+360.8s)` | `+16.6 min (+996s)` | 4 | `50.0%` |
| **Route 75** | `+3.0 min (+178.2s)` | `+8.6 min (+514s)` | 2 | `20.0%` |
| **Route 901** | `+2.8 min (+167.1s)` | `+9.0 min (+540s)` | 7 | `71.43%` |
| **Route 904** | `+2.5 min (+150.6s)` | `+5.1 min (+304s)` | 8 | `85.71%` |
| **Route 36** | `+2.4 min (+145.2s)` | `+12.3 min (+739s)` | 6 | `62.5%` |
| **Route 542** | `+2.4 min (+142.8s)` | `+6.1 min (+368s)` | 4 | `83.33%` |
| **Route 923** | `+2.3 min (+136.2s)` | `+10.3 min (+620s)` | 10 | `65.0%` |
| **Route 9** | `+2.0 min (+122.9s)` | `+12.0 min (+718s)` | 7 | `55.56%` |
| **Route 11** | `+2.0 min (+119.8s)` | `+16.4 min (+984s)` | 13 | `55.56%` |

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
| `1325320` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325632` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325819` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325994` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326661` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326757` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365597` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365892` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366126` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366842` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332041` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333002` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333141` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1333276` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1010482` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T17:20:37.771374+00:00`.*
