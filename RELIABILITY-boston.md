# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:18.066000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.73%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `264` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `10` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `258` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 258 | 97.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 96** | 44 | 0 | 44 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 95** | 33 | 0 | 33 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 94** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 112** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78267299` | Route 96 | `11:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260688` | Route 101 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78267077` | Route 101 | `06:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260696` | Route 101 | `11:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78267323` | Route 96 | `05:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260639` | Route 101 | `05:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260664` | Route 101 | `07:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260947` | Route 94 | `18:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78260938` | Route 94 | `12:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259904` | Route 95 | `09:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `97.73%` | `0.0%` | 264 | 10 | `+0.0s` |
| `2026-10-28 06:30:18` | `97.17%` | `0.0%` | 353 | 18 | `+0.0s` |
| `2026-10-28 06:00:18` | `92.47%` | `0.0%` | 372 | 38 | `+0.0s` |
| `2026-10-28 05:30:20` | `76.82%` | `0.0%` | 440 | 101 | `+0.0s` |
| `2026-10-28 05:00:20` | `55.78%` | `0.0%` | 597 | 209 | `+0.0s` |
| `2026-10-28 04:30:19` | `39.73%` | `0.0%` | 818 | 289 | `+0.0s` |
| `2026-10-28 04:00:19` | `32.92%` | `0.0%` | 969 | 325 | `+0.0s` |
| `2026-10-28 03:30:18` | `31.43%` | `0.0%` | 1015 | 344 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.066000+00:00`.*
