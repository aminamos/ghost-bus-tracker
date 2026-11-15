# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Transportation Authority** in **New York, NY** (New York Metropolitan Area).
> **Transit System:** MTA | **Location:** New York, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:18.880000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`28.12%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `96` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `69` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `27` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 27 | 28.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 6 | 2 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 1** | 11 | 7 | 4 | **`36.36%`** | `0.0%` | `+0.0s` |
| **Route 4** | 16 | 11 | 5 | **`31.25%`** | `0.0%` | `+0.0s` |
| **Route 6** | 11 | 8 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route 2** | 15 | 11 | 4 | **`26.67%`** | `0.0%` | `+0.0s` |
| **Route 7** | 33 | 30 | 3 | **`9.09%`** | `0.0%` | `+0.0s` |

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
| `012600_1..S03X048` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013200_1..N03R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014600_1..S03X048` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `015200_1..N03R` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `001950_2..S08X035` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `157150_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013950_2..S08X035` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `015150_2..N08R` | Route 2 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012300_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012500_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014300_3..S88R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `014500_3..N90R` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `148850_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `012850_4..N13R` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `013400_4..S13X002` | Route 4 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:18` | `28.12%` | `0.0%` | 96 | 69 | `+0.0s` |
| `2026-11-15 06:30:18` | `26.0%` | `0.0%` | 100 | 74 | `+0.0s` |
| `2026-11-15 06:00:30` | `26.42%` | `0.0%` | 106 | 78 | `+0.0s` |
| `2026-11-15 05:30:19` | `28.21%` | `50.0%` | 117 | 84 | `+420.5s` |
| `2026-11-15 05:00:19` | `29.37%` | `57.14%` | 126 | 89 | `+146.7s` |
| `2026-11-15 04:30:21` | `28.17%` | `44.0%` | 142 | 102 | `+357.7s` |
| `2026-11-15 04:00:19` | `31.69%` | `0.0%` | 142 | 97 | `+0.0s` |
| `2026-11-15 03:30:18` | `32.19%` | `0.0%` | 146 | 99 | `-391.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:18.880000+00:00`.*
