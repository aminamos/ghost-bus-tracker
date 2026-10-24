# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-24T06:30:20.697000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.9%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`65.22%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `29` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `150` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+180.9s` (`+3.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+132.0s` (`+2.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 15 | 51.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 10.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 10.3% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 6.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 6.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 22** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 41** | 4 | 3 | 0 | **`0.0%`** | `33.33%` | `-281.3s` |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-51.0s` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.2 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.7 min` |
| **Route 1** | 3 | 2 | 0 | **`0.0%`** | `50.0%` | `-113.5s` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `66.67%` | `+4.8 min` |
| **Route 6** | 4 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.2 min` |
| **Route 51** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+22.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 51** | `+22.3 min (+1337.0s)` | `+22.3 min (+1337s)` | 1 | `0.0%` |
| **Route 19** | `+11.2 min (+671.0s)` | `+11.2 min (+671s)` | 1 | `0.0%` |
| **Route 48** | `+4.8 min (+285.0s)` | `+7.2 min (+432s)` | 2 | `66.67%` |
| **Route 3** | `+4.6 min (+275.0s)` | `+4.6 min (+275s)` | 2 | `100.0%` |
| **Route 25** | `+2.2 min (+134.0s)` | `+3.2 min (+194s)` | 2 | `100.0%` |
| **Route 26** | `+2.2 min (+132.0s)` | `+3.2 min (+195s)` | 2 | `100.0%` |
| **Route 14** | `+1.7 min (+102.0s)` | `+2.2 min (+132s)` | 2 | `100.0%` |
| **Route 6** | `+0.9 min (+55.5s)` | `+2.2 min (+135s)` | 3 | `100.0%` |
| **Route 28** | `+0.2 min (+11.0s)` | `+0.2 min (+11s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~1356.0m | ~1356.0m | **`+0.0 min`** | `99.1 / 100` |
| **Route 48** | ~60.0m | ~60.0m | **`+0.0 min`** | `98.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19229265` | Route 22 | `07:40:00` | `SCHEDULED` | Assigned vehicle 2429 is broadcasting off-schedule with no vehicle covering 19229265 |
| `19229211` | Route 22 | `05:40:00` | `SCHEDULED` | Assigned vehicle 2453 is broadcasting off-schedule with no vehicle covering 19229211 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:20` | `6.9%` | `65.22%` | 29 | 150 | `+180.9s` |
| `2026-10-24 05:30:19` | `0.0%` | `80.65%` | 48 | 163 | `+173.1s` |
| `2026-10-24 05:00:22` | `2.9%` | `83.87%` | 69 | 163 | `+147.5s` |
| `2026-10-24 04:30:20` | `4.08%` | `87.93%` | 98 | 171 | `+161.3s` |
| `2026-10-24 04:00:20` | `1.6%` | `79.66%` | 125 | 194 | `+189.7s` |
| `2026-10-24 03:30:28` | `2.01%` | `84.93%` | 149 | 201 | `+248.2s` |
| `2026-10-24 03:00:19` | `0.57%` | `81.01%` | 174 | 203 | `+266.4s` |
| `2026-10-24 02:30:22` | `0.52%` | `84.95%` | 192 | 191 | `+185.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:20.697000+00:00`.*
