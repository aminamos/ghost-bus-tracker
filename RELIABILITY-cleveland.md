# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-29T07:00:18.655000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.63%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`77.78%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `38` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `177` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+134.3s` (`+2.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+74.0s` (`+1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 7 | 18.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 5.3% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 48** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `-48.0s` |
| **Route 14** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 25** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+5.2 min` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+11.2 min` |
| **Route 3** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 51** | `+11.2 min (+669.0s)` | `+11.2 min (+669s)` | 2 | `0.0%` |
| **Route 25** | `+5.2 min (+311.0s)` | `+5.2 min (+311s)` | 2 | `0.0%` |
| **Route 41** | `+2.1 min (+126.0s)` | `+2.1 min (+126s)` | 1 | `100.0%` |
| **Route 19** | `+1.2 min (+74.0s)` | `+1.2 min (+74s)` | 2 | `100.0%` |
| **Route 6** | `+0.4 min (+23.5s)` | `+1.3 min (+76s)` | 3 | `100.0%` |
| **Route 14** | `+0.3 min (+20.0s)` | `+0.3 min (+20s)` | 3 | `100.0%` |
| **Route 26** | `+0.2 min (+10.0s)` | `+0.2 min (+10s)` | 2 | `100.0%` |

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
| `19233316` | Route 48 | `05:20:00` | `SCHEDULED` | Assigned vehicle 4101 is broadcasting off-schedule with no vehicle covering 19233316 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:18` | `2.63%` | `77.78%` | 38 | 177 | `+134.3s` |
| `2026-10-29 06:30:20` | `3.57%` | `81.82%` | 28 | 183 | `+6.2s` |
| `2026-10-29 06:00:20` | `0.0%` | `84.62%` | 32 | 194 | `+86.7s` |
| `2026-10-29 05:30:18` | `2.22%` | `77.78%` | 45 | 179 | `+131.4s` |
| `2026-10-29 05:00:19` | `2.99%` | `75.86%` | 67 | 185 | `+172.6s` |
| `2026-10-29 04:30:19` | `2.15%` | `83.33%` | 93 | 198 | `+2310.0s` |
| `2026-10-29 04:00:19` | `1.59%` | `75.38%` | 126 | 224 | `+257.4s` |
| `2026-10-29 03:30:18` | `0.68%` | `76.32%` | 147 | 222 | `+303.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:18.655000+00:00`.*
