# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Massachusetts Bay Transportation Authority** in **Boston, MA** (Greater Boston, Massachusetts).
> **Transit System:** MBTA | **Location:** Boston, MA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-21T22:30:35.263000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1734` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `763` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `285` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 285 | 16.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 11 | 0.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 426** | 51 | 2 | 47 | **`92.16%`** | `0.0%` | `+0.0s` |
| **Route 220** | 75 | 4 | 68 | **`90.67%`** | `0.0%` | `+0.0s` |
| **Route 428** | 6 | 1 | 5 | **`83.33%`** | `0.0%` | `+0.0s` |
| **Route 18** | 10 | 1 | 8 | **`80.0%`** | `0.0%` | `+0.0s` |
| **Route 93** | 28 | 3 | 22 | **`78.57%`** | `0.0%` | `+0.0s` |
| **Route 238** | 27 | 4 | 21 | **`77.78%`** | `0.0%` | `+0.0s` |
| **Route 455** | 40 | 7 | 31 | **`77.5%`** | `0.0%` | `+0.0s` |
| **Route 85** | 36 | 6 | 27 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 236** | 15 | 3 | 11 | **`73.33%`** | `0.0%` | `+0.0s` |
| **Route 424** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |

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
| `78516989` | Route 455 | `17:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854536` | Route 220 | `07:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `FBWMLConstruction-859852-2037` | Route CR-NewBedford | `18:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78174197` | Route 85 | `15:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78174241` | Route 85 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78174184` | Route 85 | `09:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78853939` | Route 238 | `06:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181673` | Route 9 | `19:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516718` | Route 426 | `14:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854606` | Route 220 | `25:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78181983` | Route 18 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78517106` | Route 455 | `08:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854460` | Route 220 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78854468` | Route 220 | `17:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `78516625` | Route 426 | `08:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-21 22:30:35` | `16.44%` | `0.0%` | 1734 | 763 | `+0.0s` |
| `2026-10-21 22:00:35` | `13.58%` | `0.0%` | 1790 | 794 | `+0.0s` |
| `2026-10-21 21:30:35` | `12.76%` | `0.0%` | 1841 | 807 | `+0.0s` |
| `2026-10-21 21:00:36` | `13.86%` | `0.0%` | 1811 | 805 | `+0.0s` |
| `2026-10-21 20:30:35` | `14.54%` | `0.0%` | 1816 | 800 | `+0.0s` |
| `2026-10-21 20:00:35` | `14.19%` | `0.0%` | 1790 | 799 | `+0.0s` |
| `2026-10-21 19:30:38` | `15.39%` | `0.0%` | 1748 | 765 | `+0.0s` |
| `2026-10-21 19:00:50` | `16.61%` | `0.0%` | 1710 | 755 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-21T22:30:35.263000+00:00`.*
