# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-19T07:00:19.974000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`86.17%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `405` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `52` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `349` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-55.3s` (`-0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-9.5s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 4 | 1.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 349 | 86.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5** | 72 | 2 | 69 | **`95.83%`** | `50.0%` | `-122.5s` |
| **Route 1** | 88 | 3 | 84 | **`95.45%`** | `50.0%` | `-34.0s` |
| **Route 17** | 76 | 3 | 71 | **`93.42%`** | `100.0%` | `-9.5s` |
| **Route 6** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 13** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 5** | ~15.0m | ~15.0m | **`+0.0 min`** | `86.4 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `96.2 / 100` |
| **Route 17** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `30799874` | Route 5 | `24:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799880` | Route 5 | `23:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799883` | Route 5 | `21:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799887` | Route 5 | `18:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799891` | Route 5 | `16:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799901` | Route 5 | `14:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799877` | Route 5 | `24:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799879` | Route 5 | `22:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799882` | Route 5 | `20:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799886` | Route 5 | `17:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799894` | Route 5 | `15:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799899` | Route 5 | `13:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799919` | Route 5 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799939` | Route 5 | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799890` | Route 5 | `15:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-19 07:00:19` | `86.17%` | `66.67%` | 405 | 52 | `-55.3s` |
| `2026-11-19 06:30:19` | `80.41%` | `58.33%` | 434 | 79 | `-66.6s` |
| `2026-11-19 06:00:20` | `77.78%` | `72.22%` | 450 | 90 | `-33.6s` |
| `2026-11-19 05:30:25` | `8.26%` | `55.56%` | 109 | 99 | `-20.4s` |
| `2026-11-19 05:00:19` | `9.85%` | `60.0%` | 132 | 117 | `+184.7s` |
| `2026-11-19 04:30:19` | `12.41%` | `37.5%` | 145 | 127 | `-98.1s` |
| `2026-11-19 04:00:21` | `13.5%` | `36.36%` | 163 | 139 | `-88.6s` |
| `2026-11-19 03:30:18` | `15.25%` | `30.77%` | 177 | 149 | `-103.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T07:00:19.974000+00:00`.*
