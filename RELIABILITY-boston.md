# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:17.804000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`90.38%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `239` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `24` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `216` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 216 | 90.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 16** | 215 | 0 | 215 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-B** | 2 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-D** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-C** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78928368` | Route 16 | `12:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928297` | Route 16 | `19:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928261` | Route 16 | `09:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78615122` | Route 16 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78929089` | Route 16 | `07:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928260` | Route 16 | `10:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928311` | Route 16 | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928313` | Route 16 | `18:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928429` | Route 16 | `13:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928330` | Route 16 | `22:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928416` | Route 16 | `09:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928354` | Route 16 | `23:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928281` | Route 16 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78615117` | Route 16 | `05:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78928284` | Route 16 | `20:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:17` | `90.38%` | `0.0%` | 239 | 24 | `+0.0s` |
| `2026-11-27 06:30:17` | `70.68%` | `0.0%` | 307 | 74 | `+0.0s` |
| `2026-11-27 06:00:17` | `48.65%` | `0.0%` | 444 | 166 | `+0.0s` |
| `2026-11-27 05:30:17` | `0.46%` | `0.0%` | 432 | 235 | `+0.0s` |
| `2026-11-27 05:00:17` | `0.54%` | `0.0%` | 560 | 256 | `+0.0s` |
| `2026-11-27 04:30:18` | `0.16%` | `0.0%` | 615 | 268 | `+0.0s` |
| `2026-11-27 04:00:17` | `1.13%` | `0.0%` | 622 | 271 | `+0.0s` |
| `2026-11-27 03:30:18` | `7.47%` | `0.0%` | 669 | 289 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:17.804000+00:00`.*
