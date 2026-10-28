# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-28T07:00:18.308000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.43%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `43` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `174` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `4` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-40.4s` (`-0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+88.0s` (`+1.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 5 | 11.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 2.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 2.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 4 | 9.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 51** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 48** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 6 | 4 | 0 | **`0.0%`** | `33.33%` | `-173.3s` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | `+1.5 min (+88.0s)` | `+1.5 min (+88s)` | 1 | `100.0%` |
| **Route 6** | `+1.1 min (+67.5s)` | `+2.2 min (+131s)` | 3 | `100.0%` |
| **Route 28** | `+0.2 min (+14.0s)` | `+0.2 min (+14s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | ~690.0m | ~690.0m | **`+0.0 min`** | `98.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19233316` | Route 48 | `05:20:00` | `SCHEDULED` | Assigned vehicle 2409 is broadcasting off-schedule with no vehicle covering 19233316 |
| `19229211` | Route 22 | `05:40:00` | `SCHEDULED` | Assigned vehicle 2453 is broadcasting off-schedule with no vehicle covering 19229211 |
| `19229401` | Route 51 | `26:34:00` | `SCHEDULED` | Assigned vehicle 4158 is missing from active GPS transponder fleet |
| `19234615` | Route 14 | `07:43:00` | `SCHEDULED` | Assigned vehicle 4254 is broadcasting off-schedule with no vehicle covering 19234615 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `9.3%` | `71.43%` | 43 | 174 | `-40.4s` |
| `2026-10-28 06:30:19` | `10.0%` | `86.36%` | 30 | 183 | `+54.9s` |
| `2026-10-28 06:00:19` | `0.0%` | `78.57%` | 34 | 193 | `+134.4s` |
| `2026-10-28 05:30:22` | `8.16%` | `80.0%` | 49 | 188 | `+116.2s` |
| `2026-10-28 05:00:23` | `1.54%` | `90.91%` | 65 | 191 | `+98.7s` |
| `2026-10-28 04:30:21` | `2.06%` | `84.75%` | 97 | 208 | `+227.1s` |
| `2026-10-28 04:00:22` | `1.67%` | `83.02%` | 120 | 242 | `+156.3s` |
| `2026-10-28 03:30:18` | `1.34%` | `78.95%` | 149 | 233 | `+328.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.308000+00:00`.*
