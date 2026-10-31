# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T07:00:27.885000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`29.21%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `89` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `63` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `26` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 26 | 29.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5** | 4 | 1 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 6 | 2 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 1** | 10 | 6 | 4 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 11 | 7 | 4 | **`36.36%`** | `0.0%` | `+0.0s` |
| **Route 2** | 15 | 10 | 5 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 4** | 15 | 12 | 3 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 27 | 24 | 3 | **`11.11%`** | `0.0%` | `+0.0s` |

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
| `018600_1..S03X015` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019200_1..N03R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020600_1..S03X015` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `021200_1..N03R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `017350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019650_2..S08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `021350_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018300_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018500_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020300_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `020500_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `018850_4..N13X049` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `019400_4..S13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:27` | `29.21%` | `0.0%` | 89 | 63 | `+0.0s` |
| `2026-10-31 06:30:19` | `26.44%` | `0.0%` | 87 | 64 | `+0.0s` |
| `2026-10-31 06:00:19` | `28.41%` | `0.0%` | 88 | 63 | `+0.0s` |
| `2026-10-31 05:30:20` | `33.33%` | `0.0%` | 102 | 68 | `+0.0s` |
| `2026-10-31 05:00:29` | `24.24%` | `0.0%` | 99 | 75 | `+0.0s` |
| `2026-10-31 04:30:21` | `27.68%` | `0.0%` | 112 | 81 | `+0.0s` |
| `2026-10-31 04:00:18` | `25.44%` | `0.0%` | 114 | 85 | `+0.0s` |
| `2026-10-31 03:30:17` | `33.33%` | `0.0%` | 144 | 96 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:27.885000+00:00`.*
