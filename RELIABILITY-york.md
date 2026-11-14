# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-14T07:00:19.567000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.3%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+83.3s` (`+1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+5.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 21 | 84.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 4.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 4.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 8.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 2 | **`28.57%`** | `100.0%` | `+1.2 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `+0.1 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.6 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+2.6 min (+157.6s)` | `+11.8 min (+711s)` | 4 | `80.0%` |
| **Route 1** | `+2.5 min (+153.0s)` | `+2.5 min (+153s)` | 1 | `100.0%` |
| **Route 77** | `+1.6 min (+96.8s)` | `+3.5 min (+213s)` | 4 | `100.0%` |
| **Route 20** | `+1.2 min (+70.2s)` | `+4.5 min (+273s)` | 4 | `100.0%` |
| **Route 107** | `+0.1 min (+7.0s)` | `+2.2 min (+134s)` | 2 | `83.33%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `73.6 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `84.0 / 100` |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `81.7 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `86.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024940` | Route 20 | `02:47:00` | `SCHEDULED` | Assigned vehicle C2616 is broadcasting off-schedule with no vehicle covering 2024940 |
| `2025027` | Route 20 | `02:04:00` | `SCHEDULED` | Assigned vehicle C2616 is broadcasting off-schedule with no vehicle covering 2025027 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:19` | `8.0%` | `91.3%` | 25 | 15 | `+83.3s` |
| `2026-11-14 06:30:22` | `2.94%` | `87.88%` | 34 | 19 | `+84.2s` |
| `2026-11-14 06:00:21` | `6.67%` | `88.1%` | 45 | 27 | `+96.6s` |
| `2026-11-14 05:30:18` | `5.88%` | `87.5%` | 68 | 45 | `+107.6s` |
| `2026-11-14 05:00:28` | `5.21%` | `82.42%` | 96 | 63 | `+109.1s` |
| `2026-11-14 04:30:18` | `4.88%` | `81.2%` | 123 | 75 | `+87.8s` |
| `2026-11-14 04:00:24` | `5.84%` | `85.52%` | 154 | 88 | `+69.2s` |
| `2026-11-14 03:30:18` | `7.73%` | `91.02%` | 181 | 99 | `+83.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:19.567000+00:00`.*
