# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-02T07:00:18.454000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `351` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `335` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+3382.0s` (`+56.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+3382.0s` (`+56.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 335 | 95.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 74 | 1 | 72 | **`97.3%`** | `0.0%` | `+0.0s` |
| **Route 1** | 88 | 3 | 85 | **`96.59%`** | `0.0%` | `+56.4 min` |
| **Route 7** | 55 | 1 | 53 | **`96.36%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+56.4 min (+3382.0s)` | `+56.4 min (+3382s)` | 3 | `0.0%` |

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
| `30801045` | Route 103 | `24:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801044` | Route 103 | `22:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801078` | Route 103 | `06:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801074` | Route 103 | `08:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801056` | Route 103 | `19:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801057` | Route 103 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801054` | Route 103 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801053` | Route 103 | `13:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801059` | Route 103 | `21:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801098` | Route 103 | `16:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801043` | Route 103 | `18:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801041` | Route 103 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801071` | Route 103 | `07:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801052` | Route 103 | `11:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30801068` | Route 103 | `09:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-02 07:00:18` | `95.44%` | `0.0%` | 351 | 14 | `+3382.0s` |
| `2026-11-02 06:30:18` | `94.66%` | `0.0%` | 356 | 18 | `+3446.0s` |
| `2026-11-02 06:00:24` | `92.62%` | `0.0%` | 366 | 27 | `+3560.0s` |
| `2026-11-02 05:30:22` | `6.82%` | `0.0%` | 44 | 41 | `+3581.4s` |
| `2026-11-02 05:00:19` | `8.47%` | `0.0%` | 59 | 54 | `+3569.2s` |
| `2026-11-02 04:30:21` | `9.46%` | `0.0%` | 74 | 65 | `+3515.1s` |
| `2026-11-02 04:00:18` | `13.48%` | `0.0%` | 89 | 77 | `+3537.2s` |
| `2026-11-02 03:30:25` | `14.68%` | `0.0%` | 109 | 91 | `+3482.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.454000+00:00`.*
