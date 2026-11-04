# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-04T07:00:21.823000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+53.4s` (`+0.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 88.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 4.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 4.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 4.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 7 | 4 | 1 | **`14.29%`** | `100.0%` | `+0.4 min` |
| **Route 77** | 6 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `+0.4 min` |
| **Route 9899** | 5 | 4 | 0 | **`0.0%`** | `80.0%` | `+2.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 9899** | `+2.4 min (+143.8s)` | `+5.8 min (+349s)` | 4 | `80.0%` |
| **Route 1** | `+1.1 min (+63.0s)` | `+1.1 min (+63s)` | 1 | `100.0%` |
| **Route 77** | `+0.6 min (+36.3s)` | `+1.6 min (+96s)` | 4 | `100.0%` |
| **Route 20** | `+0.4 min (+24.7s)` | `+2.8 min (+169s)` | 4 | `100.0%` |
| **Route 107** | `+0.4 min (+22.2s)` | `+3.4 min (+204s)` | 2 | `83.33%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 107** | ~6.0m | ~6.0m | **`+0.0 min`** | `76.3 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `86.0 / 100` |
| **Route 20** | ~11.0m | ~11.0m | **`+0.0 min`** | `90.2 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `92.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2024938` | Route 20 | `02:03:00` | `SCHEDULED` | Assigned vehicle C2003 is broadcasting off-schedule with no vehicle covering 2024938 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:21` | `4.0%` | `91.67%` | 25 | 15 | `+53.4s` |
| `2026-11-04 06:00:18` | `2.22%` | `90.91%` | 45 | 29 | `+65.3s` |
| `2026-11-04 05:30:18` | `5.97%` | `93.65%` | 67 | 45 | `+49.4s` |
| `2026-11-04 05:00:18` | `7.29%` | `85.39%` | 96 | 64 | `+51.5s` |
| `2026-11-04 04:30:18` | `9.52%` | `87.72%` | 126 | 76 | `+58.4s` |
| `2026-11-04 04:00:26` | `6.62%` | `88.65%` | 151 | 86 | `+38.3s` |
| `2026-11-04 03:30:22` | `6.74%` | `86.14%` | 178 | 97 | `+53.2s` |
| `2026-11-04 03:00:27` | `8.33%` | `87.7%` | 204 | 114 | `+50.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:21.823000+00:00`.*
