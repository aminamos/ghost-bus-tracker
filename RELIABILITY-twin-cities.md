# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T12:15:23.596368+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.84%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.85%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `950` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `805` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `103` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+30.8s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+1.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 514 | 54.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 237 | 24.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 50 | 5.3% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 103 | 10.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 42 | 4.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 215** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `+0.9 min` |
| **Route 537** | 4 | 1 | 2 | **`50.0%`** | `100.0%` | `-0.5s` |
| **Route 765** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.7 min` |
| **Route 36** | 11 | 3 | 5 | **`45.45%`** | `83.33%` | `+1.4 min` |
| **Route 540** | 11 | 4 | 5 | **`45.45%`** | `83.33%` | `+1.4 min` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `75.0%` | `+2.9 min` |
| **Route 542** | 8 | 3 | 3 | **`37.5%`** | `100.0%` | `+1.4 min` |
| **Route 67** | 11 | 5 | 4 | **`36.36%`** | `57.14%` | `+0.4 min` |
| **Route 18** | 24 | 13 | 8 | **`33.33%`** | `87.5%` | `+1.8 min` |
| **Route 25** | 9 | 5 | 3 | **`33.33%`** | `66.67%` | `+3.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 71** | `+14.3 min (+858.1s)` | `+64.7 min (+3880s)` | 5 | `28.57%` |
| **Route 294** | `+9.5 min (+569.0s)` | `+9.5 min (+569s)` | 1 | `0.0%` |
| **Route 784** | `+7.1 min (+428.7s)` | `+22.9 min (+1376s)` | 3 | `33.33%` |
| **Route 467** | `+6.1 min (+366.7s)` | `+7.6 min (+457s)` | 3 | `33.33%` |
| **Route 698** | `+5.2 min (+314.1s)` | `+10.3 min (+620s)` | 8 | `37.5%` |
| **Route 134** | `+4.4 min (+266.0s)` | `+4.4 min (+266s)` | 1 | `100.0%` |
| **Route 355** | `+3.6 min (+213.4s)` | `+5.2 min (+310s)` | 5 | `80.0%` |
| **Route 25** | `+3.5 min (+207.8s)` | `+7.0 min (+418s)` | 5 | `66.67%` |
| **Route 716** | `+3.3 min (+199.0s)` | `+7.4 min (+444s)` | 1 | `66.67%` |
| **Route 5** | `+3.2 min (+191.8s)` | `+8.0 min (+481s)` | 3 | `80.0%` |

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
| `1326407` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365633` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366088` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366792` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331609` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332184` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332665` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1012205` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1012594` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1132723` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1134267` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360917` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360919` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361436` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361731` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 12:15:23` | `10.84%` | `63.85%` | 950 | 805 | `+30.8s` |
| `2026-10-05 12:14:27` | `11.02%` | `64.16%` | 944 | 798 | `+31.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T12:15:23.596368+00:00`.*
