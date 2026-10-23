# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-23T07:01:24.461000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.65%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`88.89%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `43` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `187` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-22.3s` (`-0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+77.0s` (`+1.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 8 | 18.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 2.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 4.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 22** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 7 | 4 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 7 | 5 | 0 | **`0.0%`** | `66.67%` | `-199.0s` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 41** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 3** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | `+1.5 min (+88.0s)` | `+1.5 min (+88s)` | 1 | `100.0%` |
| **Route 28** | `+1.2 min (+75.0s)` | `+1.2 min (+75s)` | 1 | `100.0%` |
| **Route 6** | `+1.1 min (+68.3s)` | `+1.9 min (+113s)` | 3 | `100.0%` |
| **Route 51** | `+0.5 min (+28.0s)` | `+0.5 min (+28s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | ~690.0m | ~690.0m | **`+0.0 min`** | `98.7 / 100` |
| **Route 6** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19229211` | Route 22 | `05:40:00` | `SCHEDULED` | Assigned vehicle 3939 is broadcasting off-schedule with no vehicle covering 19229211 |
| `19234615` | Route 14 | `07:43:00` | `SCHEDULED` | Assigned vehicle 4050 is broadcasting off-schedule with no vehicle covering 19234615 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:24` | `4.65%` | `88.89%` | 43 | 187 | `-22.3s` |
| `2026-10-23 06:30:23` | `7.14%` | `75.0%` | 28 | 188 | `+56.4s` |
| `2026-10-23 06:00:20` | `0.0%` | `85.71%` | 35 | 181 | `+65.6s` |
| `2026-10-23 05:30:21` | `2.04%` | `85.71%` | 49 | 181 | `+138.1s` |
| `2026-10-23 05:15:27` | `0.0%` | `95.65%` | 54 | 184 | `+90.8s` |
| `2026-10-23 05:00:37` | `2.94%` | `95.45%` | 68 | 192 | `+96.9s` |
| `2026-10-23 04:30:36` | `4.12%` | `92.98%` | 97 | 206 | `+116.5s` |
| `2026-10-23 04:00:40` | `1.68%` | `87.27%` | 119 | 227 | `+101.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:24.461000+00:00`.*
