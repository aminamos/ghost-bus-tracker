# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T07:00:30.412000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`24.24%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `66` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `50` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `16` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+305.0s` (`+5.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+305.0s` (`+5.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 1.5% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 16 | 24.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5** | 4 | 1 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 9 | 6 | 3 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 6** | 11 | 8 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route 4** | 15 | 12 | 3 | **`20.0%`** | `0.0%` | `+5.1 min` |
| **Route 2** | 10 | 8 | 2 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 16 | 14 | 2 | **`12.5%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 4** | `+5.1 min (+305.0s)` | `+5.1 min (+305s)` | 12 | `0.0%` |

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
| `157350_2..N04X004` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014600_2..S15X005` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012700_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013700_4..S13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014700_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012300_5..N32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014200_5..S32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014300_5..N32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013250_6..N01R` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013950_6..S01R` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `015250_6..N01R` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013050_7..N` | Route 7 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 07:00:30` | `24.24%` | `0.0%` | 66 | 50 | `+305.0s` |
| `2026-11-20 06:30:18` | `23.94%` | `0.0%` | 71 | 54 | `+305.0s` |
| `2026-11-20 06:00:20` | `21.05%` | `0.0%` | 76 | 60 | `+305.0s` |
| `2026-11-20 05:30:18` | `26.09%` | `0.0%` | 92 | 68 | `+305.0s` |
| `2026-11-20 05:00:19` | `25.49%` | `0.0%` | 102 | 76 | `+305.0s` |
| `2026-11-20 04:30:18` | `32.09%` | `0.0%` | 134 | 91 | `+305.0s` |
| `2026-11-20 04:00:18` | `33.55%` | `0.0%` | 155 | 103 | `+305.0s` |
| `2026-11-20 03:30:20` | `30.77%` | `0.0%` | 169 | 117 | `+305.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T07:00:30.412000+00:00`.*
