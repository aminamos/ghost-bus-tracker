# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.242000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.38%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.97%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `52` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `23` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `8` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+36.0s` (`+0.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+8.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 22 | 42.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 13.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 3.8% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 8 | 15.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 004** | 15 | 6 | 5 | **`33.33%`** | `88.89%` | `+1.4 min` |
| **Route 002** | 14 | 5 | 3 | **`21.43%`** | `88.89%` | `+2.3 min` |
| **Route 009** | 6 | 3 | 0 | **`0.0%`** | `66.67%` | `-57.7s` |
| **Route 008** | 10 | 5 | 0 | **`0.0%`** | `44.44%` | `-66.4s` |
| **Route 511** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | `+2.3 min (+138.6s)` | `+13.0 min (+780s)` | 5 | `88.89%` |
| **Route 004** | `+1.4 min (+83.9s)` | `+5.5 min (+330s)` | 6 | `88.89%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `82.3 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.6 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.1 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.0 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.8 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32754185` | Route 004 | `23:57:00` | `SCHEDULED` | Assigned vehicle 3044 is broadcasting off-schedule with no vehicle covering 32754185 |
| `32753579` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754190` | Route 004 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754188` | Route 004 | `25:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754197` | Route 004 | `26:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753581` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753578` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754189` | Route 004 | `25:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `15.38%` | `70.97%` | 52 | 23 | `+36.0s` |
| `2026-11-09 06:30:22` | `12.0%` | `63.16%` | 75 | 44 | `+24.8s` |
| `2026-11-09 06:00:19` | `9.84%` | `73.74%` | 122 | 77 | `+48.5s` |
| `2026-11-09 05:30:19` | `11.18%` | `72.46%` | 170 | 87 | `+45.2s` |
| `2026-11-09 05:00:20` | `13.74%` | `78.36%` | 211 | 104 | `+37.2s` |
| `2026-11-09 04:30:19` | `15.48%` | `77.89%` | 239 | 107 | `+72.5s` |
| `2026-11-09 04:00:18` | `18.18%` | `79.34%` | 275 | 120 | `+73.2s` |
| `2026-11-09 03:30:18` | `20.86%` | `74.78%` | 302 | 127 | `+100.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.242000+00:00`.*
