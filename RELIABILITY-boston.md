# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-26T07:00:18.196000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`84.54%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `97` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `29` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `82` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 82 | 84.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route Green-E** | 6 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Red** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Green-D** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route Mattapan** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
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
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854470` | Route 220 | `18:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854550` | Route 220 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854570` | Route 220 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854590` | Route 220 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181027` | Route 171 | `03:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854464` | Route 220 | `15:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854576` | Route 220 | `17:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854596` | Route 220 | `22:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854542` | Route 220 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854530` | Route 220 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854450` | Route 220 | `08:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:18` | `84.54%` | `0.0%` | 97 | 29 | `+0.0s` |
| `2026-10-26 06:30:35` | `90.05%` | `0.0%` | 211 | 32 | `+0.0s` |
| `2026-10-26 06:00:26` | `80.95%` | `0.0%` | 231 | 45 | `+0.0s` |
| `2026-10-26 05:30:18` | `67.84%` | `0.0%` | 283 | 76 | `+0.0s` |
| `2026-10-26 05:00:21` | `43.91%` | `0.0%` | 419 | 173 | `+0.0s` |
| `2026-10-26 04:30:29` | `29.72%` | `0.0%` | 609 | 241 | `+0.0s` |
| `2026-10-26 04:00:18` | `23.78%` | `0.0%` | 740 | 258 | `+0.0s` |
| `2026-10-26 03:30:33` | `22.19%` | `0.0%` | 793 | 276 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:18.196000+00:00`.*
