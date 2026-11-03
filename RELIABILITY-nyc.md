# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-03T07:00:18.737000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.83%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `208` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `173` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `35` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+180.0s` (`+3.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+180.0s` (`+3.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 35 | 16.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GS** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 11 | 7 | 4 | **`36.36%`** | `0.0%` | `+0.0s` |
| **Route 1** | 10 | 7 | 3 | **`30.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 9 | 7 | 2 | **`22.22%`** | `0.0%` | `+0.0s` |
| **Route 6** | 53 | 45 | 8 | **`15.09%`** | `100.0%` | `+3.0 min` |
| **Route 2** | 14 | 12 | 2 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 6X** | 24 | 22 | 2 | **`8.33%`** | `0.0%` | `+0.0s` |
| **Route 7** | 67 | 62 | 5 | **`7.46%`** | `0.0%` | `+0.0s` |
| **Route 7X** | 9 | 9 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 6** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 45 | `100.0%` |

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
| `013450_3..S06R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014250_3..N01R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013700_4..S01X068` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013850_4..N13X156` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014200_5..S32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014300_5..N32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012050_6..N01X051` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013950_6..S01X053` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `16.83%` | `100.0%` | 208 | 173 | `+180.0s` |
| `2026-11-03 06:30:25` | `20.47%` | `100.0%` | 215 | 171 | `+180.0s` |
| `2026-11-03 06:00:18` | `18.57%` | `100.0%` | 210 | 171 | `+180.0s` |
| `2026-11-03 05:30:18` | `20.09%` | `100.0%` | 229 | 183 | `+180.0s` |
| `2026-11-03 05:00:24` | `20.0%` | `100.0%` | 235 | 188 | `+180.0s` |
| `2026-11-03 04:30:21` | `21.29%` | `100.0%` | 249 | 196 | `+180.0s` |
| `2026-11-03 04:00:19` | `22.78%` | `100.0%` | 259 | 200 | `+180.0s` |
| `2026-11-03 03:30:20` | `23.19%` | `100.0%` | 276 | 212 | `+180.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.737000+00:00`.*
