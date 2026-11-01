# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph Transit | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:18.525000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`50.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `282` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `6` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `141` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 141 | 50.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 133 | 47.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 2997** | 21 | 0 | 21 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3014** | 20 | 0 | 20 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3017** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3019** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3022** | 133 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `479039` | Route 2992 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479040` | Route 2992 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479041` | Route 2992 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479042` | Route 2992 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479043` | Route 2992 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479044` | Route 2992 | `11:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479045` | Route 2992 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479046` | Route 2992 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479047` | Route 2992 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479048` | Route 2992 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479049` | Route 2992 | `14:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479050` | Route 2992 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479051` | Route 2992 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479052` | Route 2992 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `479053` | Route 2992 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:18` | `50.0%` | `0.0%` | 282 | 6 | `+0.0s` |
| `2026-11-01 06:30:18` | `48.96%` | `0.0%` | 288 | 6 | `+0.0s` |
| `2026-11-01 06:00:19` | `48.45%` | `0.0%` | 291 | 6 | `+0.0s` |
| `2026-11-01 05:30:18` | `49.82%` | `0.0%` | 283 | 3 | `+0.0s` |
| `2026-11-01 05:00:19` | `50.0%` | `0.0%` | 282 | 2 | `+0.0s` |
| `2026-11-01 04:30:19` | `45.66%` | `0.0%` | 311 | 25 | `+0.0s` |
| `2026-11-01 04:00:18` | `14.29%` | `0.0%` | 56 | 26 | `+0.0s` |
| `2026-11-01 03:30:18` | `21.43%` | `0.0%` | 70 | 26 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:18.525000+00:00`.*
