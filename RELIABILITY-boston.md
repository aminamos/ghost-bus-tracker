# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-13T07:00:18.616000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`86.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `178` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `57` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `154` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 154 | 86.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 220** | 81 | 0 | 81 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 137** | 59 | 0 | 59 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 131** | 10 | 0 | 10 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 116** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route Green-D** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 104** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 23** | 4 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `78259714` | Route 137 | `16:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853217` | Route 220 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262963` | Route 137 | `20:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262908` | Route 137 | `04:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853134` | Route 220 | `24:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78262964` | Route 137 | `21:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259704` | Route 137 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853096` | Route 220 | `05:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259694` | Route 137 | `06:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853131` | Route 220 | `23:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259709` | Route 137 | `07:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853201` | Route 220 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853187` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259734` | Route 137 | `12:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78259700` | Route 137 | `12:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-13 07:00:18` | `86.52%` | `0.0%` | 178 | 57 | `+0.0s` |
| `2026-11-13 06:30:17` | `58.91%` | `0.0%` | 258 | 121 | `+0.0s` |
| `2026-11-13 06:00:18` | `37.07%` | `0.0%` | 410 | 217 | `+0.0s` |
| `2026-11-13 05:30:18` | `23.6%` | `0.0%` | 623 | 300 | `+0.0s` |
| `2026-11-13 05:00:18` | `19.14%` | `0.0%` | 768 | 307 | `+0.0s` |
| `2026-11-13 04:30:18` | `17.94%` | `0.0%` | 825 | 330 | `+0.0s` |
| `2026-11-13 04:00:18` | `18.86%` | `0.0%` | 843 | 346 | `+0.0s` |
| `2026-11-13 03:30:18` | `23.13%` | `0.0%` | 882 | 365 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-13T07:00:18.616000+00:00`.*
