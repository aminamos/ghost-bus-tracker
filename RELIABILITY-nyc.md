# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-13T07:00:22.081000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`33.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`33.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `80` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `53` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `27` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+133.0s` (`+2.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 1.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 1.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 1.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 27 | 33.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GS** | 7 | 1 | 6 | **`85.71%`** | `0.0%` | `+0.0s` |
| **Route 5** | 6 | 3 | 3 | **`50.0%`** | `0.0%` | `+8.2 min` |
| **Route 6** | 11 | 7 | 4 | **`36.36%`** | `100.0%` | `+0.0s` |
| **Route 3** | 12 | 8 | 4 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 7** | 10 | 7 | 3 | **`30.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 11 | 8 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route 4** | 9 | 7 | 2 | **`22.22%`** | `0.0%` | `-92.0s` |
| **Route 2** | 13 | 11 | 2 | **`15.38%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5** | `+8.2 min (+491.0s)` | `+8.2 min (+491s)` | 3 | `0.0%` |

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
| `157350_2..N04R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013900_2..S15R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012250_3..N01R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012450_3..S06R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014250_3..N01R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014450_3..S06R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013700_4..S01X068` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013850_4..N13X156` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012300_5..N32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014200_5..S32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014300_5..N32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012050_6..N01X051` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:22` | `33.75%` | `33.33%` | 80 | 53 | `+133.0s` |
| `2026-11-13 06:30:18` | `38.1%` | `33.33%` | 84 | 52 | `+133.0s` |
| `2026-11-13 06:00:30` | `35.29%` | `33.33%` | 85 | 55 | `+133.0s` |
| `2026-11-13 05:30:18` | `38.1%` | `42.86%` | 105 | 65 | `+160.7s` |
| `2026-11-13 05:00:21` | `42.15%` | `50.0%` | 121 | 70 | `+390.9s` |
| `2026-11-13 04:30:18` | `44.68%` | `56.52%` | 141 | 78 | `+47.0s` |
| `2026-11-13 04:00:20` | `49.69%` | `69.05%` | 161 | 81 | `+7.2s` |
| `2026-11-13 03:30:23` | `44.94%` | `71.7%` | 178 | 98 | `-9.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:22.081000+00:00`.*
