# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Regional Transportation District** in **Denver, CO** (Denver Metropolitan Area, Colorado).
> **Transit System:** RTD | **Location:** Denver, CO | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-26T07:00:23.502000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`28.57%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `42` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `213` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `12` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 12 | 28.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route AT** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 45** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 42** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route A** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 15L** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `116042674` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116043317` | Route 31 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045113` | Route 42 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045369` | Route 43 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045856` | Route 45 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116045924` | Route 45 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116048098` | Route 76 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116050241` | Route AT | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116050780` | Route DASH | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116058082` | Route 15 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `116060294` | Route 101E | `N/A` | `SCHEDULED` | Assigned vehicle 34 is missing from active GPS transponder fleet |
| `116065497` | Route A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:23` | `28.57%` | `0.0%` | 42 | 213 | `+0.0s` |
| `2026-10-26 06:30:42` | `20.24%` | `0.0%` | 84 | 244 | `+0.0s` |
| `2026-10-26 05:00:28` | `37.09%` | `0.0%` | 213 | 204 | `+0.0s` |
| `2026-10-26 04:00:21` | `36.07%` | `0.0%` | 244 | 231 | `+0.0s` |
| `2026-10-26 03:30:41` | `35.71%` | `0.0%` | 266 | 253 | `+0.0s` |
| `2026-10-26 01:00:31` | `36.54%` | `0.0%` | 364 | 381 | `+0.0s` |
| `2026-10-26 00:30:46` | `35.25%` | `0.0%` | 383 | 406 | `+0.0s` |
| `2026-10-25 23:30:23` | `35.84%` | `0.0%` | 438 | 367 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:23.502000+00:00`.*
