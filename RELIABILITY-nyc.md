# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:16:51.247000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`41.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.26%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `263` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `154` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `109` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+28.0s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-1.0s` (`-0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 63 | 24.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 19 | 7.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 1.5% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 109 | 41.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GS** | 16 | 1 | 15 | **`93.75%`** | `100.0%` | `+0.2 min` |
| **Route 6X** | 8 | 2 | 6 | **`75.0%`** | `100.0%` | `+2.4 min` |
| **Route 6** | 43 | 22 | 21 | **`48.84%`** | `77.78%` | `+2.6 min` |
| **Route 1** | 32 | 20 | 12 | **`37.5%`** | `100.0%` | `+0.7 min` |
| **Route 7X** | 8 | 5 | 3 | **`37.5%`** | `0.0%` | `+0.0s` |
| **Route 7** | 27 | 17 | 10 | **`37.04%`** | `0.0%` | `+0.0s` |
| **Route 3** | 28 | 18 | 10 | **`35.71%`** | `77.78%` | `+0.2 min` |
| **Route 4** | 33 | 22 | 11 | **`33.33%`** | `60.0%` | `+0.6 min` |
| **Route 5** | 34 | 23 | 11 | **`32.35%`** | `60.0%` | `+0.2 min` |
| **Route 2** | 34 | 24 | 10 | **`29.41%`** | `41.67%` | `-63.2s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 6** | `+2.6 min (+153.7s)` | `+7.7 min (+462s)` | 22 | `77.78%` |
| **Route 6X** | `+2.4 min (+145.0s)` | `+2.4 min (+145s)` | 2 | `100.0%` |
| **Route 1** | `+0.7 min (+39.8s)` | `+4.0 min (+238s)` | 20 | `100.0%` |
| **Route 4** | `+0.6 min (+35.4s)` | `+8.7 min (+522s)` | 22 | `60.0%` |
| **Route GS** | `+0.2 min (+14.0s)` | `+0.2 min (+14s)` | 1 | `100.0%` |
| **Route 5** | `+0.2 min (+11.8s)` | `+6.9 min (+416s)` | 23 | `60.0%` |
| **Route 3** | `+0.2 min (+10.1s)` | `+3.8 min (+227s)` | 18 | `77.78%` |

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
| `091850_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `091950_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `092350_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `092600_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `092850_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `093150_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `093350_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `093650_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `093850_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `094150_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `094350_1..S15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `094650_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `091250_2..N01R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `092150_2..S01R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `092650_2..N01R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 19:16:51` | `41.44%` | `73.26%` | 263 | 154 | `+28.0s` |
| `2026-10-22 19:00:19` | `43.41%` | `0.0%` | 258 | 146 | `+0.0s` |
| `2026-10-22 18:55:46` | `42.19%` | `0.0%` | 256 | 148 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:16:51.247000+00:00`.*
