# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:18.879000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.78%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `45` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `126` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `8` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 8 | 17.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 42** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route A** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 0** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 12** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 169** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 76** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `116039282` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116043381` | Route 31 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045185` | Route 42 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045225` | Route 42 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045486` | Route 43 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116048554` | Route 83L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116055563` | Route DASH | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116064999` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `17.78%` | `0.0%` | 45 | 126 | `+0.0s` |
| `2026-10-28 06:30:22` | `25.24%` | `0.0%` | 103 | 176 | `+0.0s` |
| `2026-10-28 06:00:22` | `26.49%` | `0.0%` | 151 | 210 | `+0.0s` |
| `2026-10-28 05:30:27` | `34.13%` | `0.0%` | 208 | 243 | `+0.0s` |
| `2026-10-28 05:00:27` | `35.69%` | `0.0%` | 255 | 259 | `+0.0s` |
| `2026-10-28 03:30:19` | `33.43%` | `0.0%` | 332 | 323 | `+0.0s` |
| `2026-10-28 03:00:22` | `37.9%` | `0.0%` | 372 | 321 | `+0.0s` |
| `2026-10-28 02:30:18` | `34.66%` | `0.0%` | 401 | 339 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.879000+00:00`.*
