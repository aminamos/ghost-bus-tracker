# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:18.864000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`29.03%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `62` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `102` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 18 | 29.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 103W** | 4 | 1 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 101E** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 101C** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 101T** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 31** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 7 | 4 | 3 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route A** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 0** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `116034572` | Route 103W | `N/A` | `SCHEDULED` | Assigned vehicle 77 is missing from active GPS transponder fleet |
| `116034638` | Route 103W | `N/A` | `SCHEDULED` | Assigned vehicle 76 is missing from active GPS transponder fleet |
| `116034705` | Route 103W | `N/A` | `SCHEDULED` | Assigned vehicle 75 is missing from active GPS transponder fleet |
| `116041929` | Route 22 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116042594` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116043222` | Route 31 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116044096` | Route 36 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116048352` | Route 83L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116057916` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116057954` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116057990` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116061091` | Route 101T | `N/A` | `SCHEDULED` | Assigned vehicle 61 is missing from active GPS transponder fleet |
| `116061132` | Route 101E | `N/A` | `SCHEDULED` | Assigned vehicle 32 is missing from active GPS transponder fleet |
| `116061133` | Route 101E | `N/A` | `SCHEDULED` | Assigned vehicle 34 is missing from active GPS transponder fleet |
| `116061155` | Route 101C | `N/A` | `SCHEDULED` | Assigned vehicle 11 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:18` | `29.03%` | `0.0%` | 62 | 102 | `+0.0s` |
| `2026-11-01 06:30:19` | `27.2%` | `0.0%` | 125 | 146 | `+0.0s` |
| `2026-11-01 06:00:21` | `29.31%` | `0.0%` | 174 | 183 | `+0.0s` |
| `2026-11-01 05:30:19` | `34.86%` | `0.0%` | 218 | 205 | `+0.0s` |
| `2026-11-01 05:00:21` | `36.26%` | `0.0%` | 262 | 238 | `+0.0s` |
| `2026-11-01 04:30:19` | `36.33%` | `0.0%` | 278 | 246 | `+0.0s` |
| `2026-11-01 04:00:18` | `36.49%` | `0.0%` | 296 | 257 | `+0.0s` |
| `2026-11-01 03:30:18` | `36.84%` | `0.0%` | 323 | 263 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:18.864000+00:00`.*
