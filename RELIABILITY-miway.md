# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-23T07:01:26.919000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`87.36%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `174` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `22` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `152` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 152 | 87.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 103** | 43 | 0 | 43 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 59 | 2 | 57 | **`96.61%`** | `0.0%` | `+0.0s` |
| **Route 7** | 54 | 2 | 52 | **`96.3%`** | `0.0%` | `+0.0s` |
| **Route 1** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `30492776` | Route 103 | `09:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492781` | Route 103 | `11:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492786` | Route 103 | `13:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492792` | Route 103 | `16:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492772` | Route 103 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492796` | Route 103 | `17:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492802` | Route 103 | `19:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492807` | Route 103 | `21:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492810` | Route 103 | `23:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492812` | Route 103 | `24:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492778` | Route 103 | `10:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492783` | Route 103 | `12:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492788` | Route 103 | `14:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492773` | Route 103 | `08:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30492775` | Route 103 | `08:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:26` | `87.36%` | `0.0%` | 174 | 22 | `+0.0s` |
| `2026-10-23 06:30:26` | `78.76%` | `0.0%` | 193 | 40 | `+0.0s` |
| `2026-10-23 06:00:22` | `72.38%` | `100.0%` | 210 | 56 | `+128.0s` |
| `2026-10-23 05:30:23` | `64.1%` | `75.0%` | 234 | 79 | `+105.2s` |
| `2026-10-23 05:15:29` | `62.55%` | `80.0%` | 243 | 86 | `-18.2s` |
| `2026-10-23 05:00:43` | `61.29%` | `85.71%` | 248 | 90 | `-4.0s` |
| `2026-10-23 04:30:38` | `0.98%` | `100.0%` | 102 | 100 | `-21.3s` |
| `2026-10-23 04:00:42` | `1.68%` | `66.67%` | 119 | 116 | `-8.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:26.919000+00:00`.*
