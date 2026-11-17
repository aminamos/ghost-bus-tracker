# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-17T07:00:21.771000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`31.53%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `222` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `152` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `70` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+352.5s` (`+5.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+210.5s` (`+3.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.5% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 70 | 31.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GS** | 7 | 1 | 6 | **`85.71%`** | `0.0%` | `+0.0s` |
| **Route 5** | 8 | 2 | 6 | **`75.0%`** | `0.0%` | `+6.5 min` |
| **Route 3** | 9 | 3 | 6 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 1** | 16 | 7 | 9 | **`56.25%`** | `0.0%` | `+0.0s` |
| **Route 6** | 17 | 8 | 9 | **`52.94%`** | `0.0%` | `+0.0s` |
| **Route 2** | 23 | 12 | 11 | **`47.83%`** | `0.0%` | `+0.0s` |
| **Route 4** | 28 | 16 | 12 | **`42.86%`** | `66.67%` | `+5.7 min` |
| **Route 7** | 101 | 90 | 11 | **`10.89%`** | `0.0%` | `+0.0s` |
| **Route 7X** | 13 | 13 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5** | `+6.5 min (+389.0s)` | `+6.5 min (+389s)` | 2 | `0.0%` |
| **Route 4** | `+5.7 min (+340.3s)` | `+16.5 min (+989s)` | 16 | `66.67%` |

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
| `012400_2..N04X001` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013900_2..S15X006` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014400_2..N04X001` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012550_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013450_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014550_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `282450_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `282900_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `283450_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `283900_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `284650_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `284900_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `144100_2..N14X004` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013350_2..N14X004` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `015150_2..S15X003` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:21` | `31.53%` | `50.0%` | 222 | 152 | `+352.5s` |
| `2026-11-17 06:30:18` | `33.19%` | `42.86%` | 226 | 151 | `+350.6s` |
| `2026-11-17 06:00:21` | `22.44%` | `64.29%` | 205 | 158 | `+236.9s` |
| `2026-11-17 05:30:22` | `19.05%` | `63.64%` | 210 | 170 | `+163.3s` |
| `2026-11-17 05:00:18` | `20.0%` | `0.0%` | 215 | 172 | `-437.0s` |
| `2026-11-17 04:30:19` | `20.43%` | `0.0%` | 230 | 183 | `-165.0s` |
| `2026-11-17 04:00:18` | `20.41%` | `100.0%` | 245 | 195 | `+17.0s` |
| `2026-11-17 03:30:22` | `19.77%` | `0.0%` | 263 | 211 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:21.771000+00:00`.*
