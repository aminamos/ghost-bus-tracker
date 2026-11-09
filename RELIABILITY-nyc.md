# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.238000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.95%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `95` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `77` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `18` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 18 | 18.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 3** | 6 | 2 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 5** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 11 | 8 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route 4** | 13 | 10 | 3 | **`23.08%`** | `0.0%` | `+0.0s` |
| **Route 1** | 9 | 7 | 2 | **`22.22%`** | `0.0%` | `+0.0s` |
| **Route 2** | 14 | 12 | 2 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 7** | 38 | 36 | 2 | **`5.26%`** | `0.0%` | `+0.0s` |

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
| `013450_1..N20R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `015200_1..S20X001` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `157350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013900_2..S15R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012450_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012550_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014450_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014550_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012700_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013700_4..S01X015` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014700_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014200_5..S32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014300_5..N32R` | Route 5 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013250_6..N01R` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013950_6..S01X011` | Route 6 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `18.95%` | `0.0%` | 95 | 77 | `+0.0s` |
| `2026-11-09 06:30:20` | `21.65%` | `0.0%` | 97 | 75 | `+0.0s` |
| `2026-11-09 06:00:18` | `21.21%` | `0.0%` | 99 | 78 | `+0.0s` |
| `2026-11-09 05:30:18` | `25.47%` | `0.0%` | 106 | 79 | `+0.0s` |
| `2026-11-09 05:00:18` | `23.15%` | `0.0%` | 108 | 83 | `+0.0s` |
| `2026-11-09 04:30:19` | `25.0%` | `0.0%` | 124 | 93 | `+0.0s` |
| `2026-11-09 04:00:19` | `28.79%` | `33.33%` | 132 | 94 | `+446.0s` |
| `2026-11-09 03:30:18` | `28.15%` | `60.0%` | 135 | 97 | `+250.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.238000+00:00`.*
