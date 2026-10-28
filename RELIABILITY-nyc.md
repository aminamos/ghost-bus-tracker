# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:18.694000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`33.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `87` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `29` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 29 | 33.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5** | 6 | 1 | 5 | **`83.33%`** | `0.0%` | `+0.0s` |
| **Route 3** | 8 | 4 | 4 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 11 | 6 | 5 | **`45.45%`** | `0.0%` | `+0.0s` |
| **Route 4** | 14 | 9 | 5 | **`35.71%`** | `0.0%` | `+0.0s` |
| **Route 1** | 9 | 6 | 3 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 6** | 24 | 19 | 5 | **`20.83%`** | `0.0%` | `+0.0s` |
| **Route 2** | 14 | 12 | 2 | **`14.29%`** | `0.0%` | `+0.0s` |

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
| `019250_6..N04X001` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020300_6..S04X101` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `021250_6..N04X001` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018550_1..S15X009` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019450_1..N15R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020550_1..S15X009` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019900_2..S08X027` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018450_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018550_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020450_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020550_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014700_4..S13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018700_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019700_4..S13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `33.33%` | `0.0%` | 87 | 58 | `+0.0s` |
| `2026-10-28 06:30:21` | `34.12%` | `0.0%` | 85 | 56 | `+0.0s` |
| `2026-10-28 06:00:20` | `34.09%` | `0.0%` | 88 | 58 | `+0.0s` |
| `2026-10-28 05:30:24` | `32.5%` | `0.0%` | 80 | 54 | `+0.0s` |
| `2026-10-28 05:00:24` | `31.4%` | `0.0%` | 86 | 59 | `+0.0s` |
| `2026-10-28 04:30:27` | `33.68%` | `0.0%` | 95 | 63 | `+0.0s` |
| `2026-10-28 04:00:28` | `33.67%` | `0.0%` | 98 | 65 | `+0.0s` |
| `2026-10-28 03:30:18` | `38.1%` | `0.0%` | 126 | 78 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.694000+00:00`.*
