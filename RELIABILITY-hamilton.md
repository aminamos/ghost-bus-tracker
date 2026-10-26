# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-26T07:00:23.030000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `461` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `461` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 461 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5783** | 131 | 0 | 131 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 108 | 0 | 108 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 106 | 0 | 106 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5828** | 56 | 0 | 56 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2197978` | Route 5808 | `25:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197975` | Route 5808 | `24:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197972` | Route 5808 | `22:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198060` | Route 5808 | `21:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198055` | Route 5808 | `20:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197970` | Route 5808 | `19:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198050` | Route 5808 | `17:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198031` | Route 5808 | `16:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198039` | Route 5808 | `14:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198017` | Route 5808 | `13:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198008` | Route 5808 | `11:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197999` | Route 5808 | `10:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197985` | Route 5808 | `08:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198038` | Route 5808 | `17:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2198046` | Route 5808 | `16:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:23` | `100.0%` | `0.0%` | 461 | 1 | `+0.0s` |
| `2026-10-26 06:30:42` | `100.0%` | `0.0%` | 461 | 1 | `+0.0s` |
| `2026-10-26 05:30:34` | `100.0%` | `0.0%` | 461 | 1 | `+0.0s` |
| `2026-10-26 05:00:27` | `99.78%` | `0.0%` | 463 | 2 | `+0.0s` |
| `2026-10-26 04:30:46` | `94.88%` | `60.0%` | 488 | 26 | `+94.0s` |
| `2026-10-26 04:00:20` | `4.48%` | `100.0%` | 67 | 63 | `+81.5s` |
| `2026-10-26 03:30:40` | `5.15%` | `86.96%` | 97 | 87 | `+115.2s` |
| `2026-10-26 01:00:30` | `29.25%` | `95.0%` | 147 | 99 | `+87.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:23.030000+00:00`.*
