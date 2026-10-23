# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-23T07:01:27.550000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`19.57%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `46` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `123` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `9` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 9 | 19.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 42** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 43** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route A** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 15** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 0** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `116032091` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116039282` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045189` | Route 42 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045225` | Route 42 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045486` | Route 43 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116048554` | Route 83L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116050293` | Route AT | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116055563` | Route DASH | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116064999` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:27` | `19.57%` | `0.0%` | 46 | 123 | `+0.0s` |
| `2026-10-23 06:30:27` | `24.53%` | `0.0%` | 106 | 175 | `+0.0s` |
| `2026-10-23 06:00:23` | `27.78%` | `0.0%` | 144 | 199 | `+0.0s` |
| `2026-10-23 05:30:24` | `34.45%` | `0.0%` | 209 | 232 | `+0.0s` |
| `2026-10-23 05:15:29` | `33.9%` | `0.0%` | 236 | 246 | `+0.0s` |
| `2026-10-23 05:00:41` | `37.85%` | `0.0%` | 251 | 247 | `+0.0s` |
| `2026-10-23 04:30:39` | `35.25%` | `0.0%` | 278 | 266 | `+0.0s` |
| `2026-10-23 04:00:43` | `37.29%` | `0.0%` | 303 | 280 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:27.550000+00:00`.*
