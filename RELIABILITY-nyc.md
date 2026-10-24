# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T07:00:35.054000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`41.03%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `78` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `46` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `32` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+0.0s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 32 | 41.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route GS** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 4 | 1 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 7 | 3 | 4 | **`57.14%`** | `0.0%` | `+0.0s` |
| **Route 1** | 9 | 5 | 4 | **`44.44%`** | `0.0%` | `+0.0s` |
| **Route 4** | 17 | 10 | 7 | **`41.18%`** | `0.0%` | `+0.0s` |
| **Route 6** | 11 | 8 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route 2** | 15 | 12 | 3 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 8 | 7 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| *All active tracked routes currently operating within nominal bounds* | - | - | - | - |

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
| `018750_1..S04R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019200_1..N04R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020750_1..S04R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `021200_1..N04R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019650_2..S08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018300_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018500_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020300_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020500_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014750_4..N01X098` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018400_4..S01X052` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018750_4..N01X098` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019950_4..N01X052` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 07:00:35` | `41.03%` | `0.0%` | 78 | 46 | `+0.0s` |
| `2026-10-24 06:30:21` | `42.86%` | `0.0%` | 77 | 44 | `+0.0s` |
| `2026-10-24 06:00:33` | `42.86%` | `0.0%` | 77 | 44 | `+0.0s` |
| `2026-10-24 05:30:20` | `39.29%` | `0.0%` | 84 | 51 | `+0.0s` |
| `2026-10-24 05:00:23` | `43.75%` | `0.0%` | 96 | 54 | `+0.0s` |
| `2026-10-24 04:30:21` | `39.6%` | `0.0%` | 101 | 61 | `+0.0s` |
| `2026-10-24 04:00:22` | `39.05%` | `0.0%` | 105 | 64 | `+0.0s` |
| `2026-10-24 03:30:34` | `39.68%` | `0.0%` | 126 | 76 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T07:00:35.054000+00:00`.*
