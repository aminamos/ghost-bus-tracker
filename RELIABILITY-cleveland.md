# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-04T07:00:20.142000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.94%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`84.62%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `34` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `201` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+225.7s` (`+3.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+122.0s` (`+2.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 11 | 32.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 2.9% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 41** | 3 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 10** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+3.2 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 6** | 4 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 51** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 19** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 48** | `+19.4 min (+1161.0s)` | `+19.4 min (+1161s)` | 1 | `0.0%` |
| **Route 14** | `+10.2 min (+612.0s)` | `+10.2 min (+612s)` | 2 | `0.0%` |
| **Route 19** | `+4.2 min (+251.0s)` | `+4.2 min (+251s)` | 2 | `100.0%` |
| **Route 10** | `+3.2 min (+191.5s)` | `+4.5 min (+269s)` | 3 | `100.0%` |
| **Route 6** | `+2.1 min (+129.0s)` | `+2.2 min (+131s)` | 3 | `100.0%` |
| **Route 1** | `+1.6 min (+99.0s)` | `+1.6 min (+99s)` | 1 | `100.0%` |
| **Route 41** | `+0.8 min (+49.3s)` | `+2.0 min (+122s)` | 4 | `100.0%` |
| **Route 28** | `+0.2 min (+11.0s)` | `+0.2 min (+11s)` | 1 | `100.0%` |
| **Route 51** | `+0.2 min (+11.0s)` | `+0.2 min (+11s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `54.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19233600` | Route 15 | `07:45:00` | `SCHEDULED` | Assigned vehicle 4184 is broadcasting off-schedule with no vehicle covering 19233600 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:20` | `2.94%` | `84.62%` | 34 | 201 | `+225.7s` |
| `2026-11-04 06:30:22` | `2.08%` | `88.89%` | 48 | 187 | `+102.1s` |
| `2026-11-04 06:00:18` | `6.15%` | `83.33%` | 65 | 193 | `+157.0s` |
| `2026-11-04 05:30:18` | `4.17%` | `83.93%` | 96 | 199 | `+2400.2s` |
| `2026-11-04 05:00:17` | `2.42%` | `84.48%` | 124 | 227 | `+150.6s` |
| `2026-11-04 04:30:17` | `1.36%` | `87.32%` | 147 | 228 | `+146.6s` |
| `2026-11-04 04:00:22` | `0.59%` | `75.34%` | 169 | 228 | `+125.6s` |
| `2026-11-04 03:30:20` | `1.01%` | `73.12%` | 198 | 198 | `+115.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:20.142000+00:00`.*
