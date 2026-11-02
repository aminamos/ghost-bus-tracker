# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-02T07:00:18.334000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`20.28%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `143` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `114` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `29` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+180.0s` (`+3.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+180.0s` (`+3.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 29 | 20.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 3** | 6 | 2 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 5** | 5 | 2 | 3 | **`60.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 9 | 6 | 3 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 4** | 13 | 10 | 3 | **`23.08%`** | `0.0%` | `+0.0s` |
| **Route 6** | 60 | 49 | 11 | **`18.33%`** | `100.0%` | `+3.0 min` |
| **Route 2** | 14 | 12 | 2 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 7** | 8 | 7 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |
| **Route 6X** | 28 | 26 | 2 | **`7.14%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 6** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 49 | `100.0%` |

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
| `012550_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013450_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014550_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `157350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013900_2..S15R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012450_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012550_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014450_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014550_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012700_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013700_4..S13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014700_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012300_5..N32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014200_5..S32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014300_5..N32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-02 07:00:18` | `20.28%` | `100.0%` | 143 | 114 | `+180.0s` |
| `2026-11-02 06:30:18` | `22.82%` | `100.0%` | 149 | 115 | `+180.0s` |
| `2026-11-02 06:00:23` | `20.69%` | `100.0%` | 145 | 115 | `+180.0s` |
| `2026-11-02 05:30:21` | `21.33%` | `100.0%` | 150 | 118 | `+180.0s` |
| `2026-11-02 05:00:19` | `21.33%` | `100.0%` | 150 | 118 | `+180.0s` |
| `2026-11-02 04:30:20` | `26.44%` | `100.0%` | 174 | 128 | `+180.0s` |
| `2026-11-02 04:00:18` | `26.78%` | `100.0%` | 183 | 134 | `+180.0s` |
| `2026-11-02 03:30:23` | `24.87%` | `100.0%` | 189 | 142 | `+180.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.334000+00:00`.*
