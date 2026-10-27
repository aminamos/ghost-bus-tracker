# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-27T07:00:22.659000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.5%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`87.5%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `40` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `158` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `3` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-220.2s` (`-3.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+15.5s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 7 | 17.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 2.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 3 | 7.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 22** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 14** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 41** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 48** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 26** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 6** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | `+1.2 min (+74.0s)` | `+1.2 min (+74s)` | 1 | `100.0%` |
| **Route 3** | `+1.2 min (+74.0s)` | `+1.2 min (+74s)` | 1 | `100.0%` |
| **Route 6** | `+0.3 min (+18.0s)` | `+1.3 min (+77s)` | 2 | `100.0%` |
| **Route 14** | `+0.3 min (+16.0s)` | `+0.3 min (+16s)` | 3 | `100.0%` |
| **Route 28** | `+0.2 min (+15.0s)` | `+0.2 min (+15s)` | 1 | `100.0%` |
| **Route 10** | `+0.1 min (+5.0s)` | `+0.1 min (+5s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 6** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19229211` | Route 22 | `05:40:00` | `SCHEDULED` | Assigned vehicle 2432 is broadcasting off-schedule with no vehicle covering 19229211 |
| `19229401` | Route 51 | `26:34:00` | `SCHEDULED` | Assigned vehicle 4181 is missing from active GPS transponder fleet |
| `19229265` | Route 22 | `07:40:00` | `SCHEDULED` | Assigned vehicle 4253 is broadcasting off-schedule with no vehicle covering 19229265 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 07:00:22` | `7.5%` | `87.5%` | 40 | 158 | `-220.2s` |
| `2026-10-27 06:30:22` | `6.9%` | `82.61%` | 29 | 165 | `+36.6s` |
| `2026-10-27 05:30:23` | `2.04%` | `82.14%` | 49 | 194 | `+137.0s` |
| `2026-10-27 05:00:20` | `1.54%` | `65.52%` | 65 | 193 | `+2604.8s` |
| `2026-10-27 04:30:19` | `2.06%` | `88.14%` | 97 | 207 | `+117.7s` |
| `2026-10-27 04:00:21` | `0.81%` | `83.05%` | 124 | 230 | `+148.3s` |
| `2026-10-27 03:30:21` | `1.38%` | `80.0%` | 145 | 227 | `+170.3s` |
| `2026-10-27 03:00:24` | `1.17%` | `77.92%` | 171 | 231 | `+159.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T07:00:22.659000+00:00`.*
