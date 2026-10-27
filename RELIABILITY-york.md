# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **York Region Transit** in **York Region, ON** (Regional Municipality of York, Ontario).
> **Transit System:** YRT | **Location:** York Region, ON | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-27T05:00:23.046000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.22%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`90.91%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `45` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `28` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+14.0s` (`+0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 40 | 88.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 8.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 4** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.9 min` |
| **Route 9899** | 8 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 20** | 9 | 5 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 107** | 6 | 2 | 0 | **`0.0%`** | `83.33%` | `-19.5s` |
| **Route 77** | 8 | 4 | 0 | **`0.0%`** | `87.5%` | `+0.3 min` |
| **Route 601** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-53.5s` |
| **Route 1** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 605** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `-9.3s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 4** | `+0.9 min (+56.0s)` | `+0.9 min (+56s)` | 1 | `100.0%` |
| **Route 1** | `+0.8 min (+45.7s)` | `+1.8 min (+105s)` | 2 | `100.0%` |
| **Route 9899** | `+0.7 min (+41.5s)` | `+3.7 min (+220s)` | 4 | `100.0%` |
| **Route 91** | `+0.6 min (+38.0s)` | `+0.6 min (+38s)` | 2 | `100.0%` |
| **Route 20** | `+0.6 min (+34.8s)` | `+2.6 min (+158s)` | 5 | `100.0%` |
| **Route 77** | `+0.3 min (+17.4s)` | `+2.8 min (+165s)` | 4 | `87.5%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 107** | ~2.0m | ~2.0m | **`+0.0 min`** | `45.6 / 100` |
| **Route 77** | ~10.0m | ~10.0m | **`+0.0 min`** | `88.5 / 100` |
| **Route 9899** | ~17.5m | ~17.5m | **`+0.0 min`** | `92.5 / 100` |
| **Route 20** | ~10.0m | ~10.0m | **`+0.0 min`** | `91.6 / 100` |
| **Route 601** | ~19.0m | ~19.0m | **`+0.0 min`** | `97.0 / 100` |
| **Route 1** | ~27.5m | ~27.5m | **`+0.0 min`** | `97.3 / 100` |
| **Route 605** | ~14.5m | ~14.5m | **`+0.0 min`** | `96.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2009918` | Route 4 | `00:27:00` | `SCHEDULED` | Assigned vehicle C1609 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 05:00:23` | `2.22%` | `90.91%` | 45 | 28 | `+14.0s` |
| `2026-10-27 04:30:20` | `5.88%` | `81.25%` | 68 | 45 | `+45.5s` |
| `2026-10-27 04:00:58` | `4.17%` | `85.87%` | 96 | 61 | `+44.4s` |
| `2026-10-27 03:30:24` | `5.56%` | `86.55%` | 126 | 73 | `+39.9s` |
| `2026-10-27 02:30:20` | `5.62%` | `89.88%` | 178 | 94 | `+31.8s` |
| `2026-10-27 01:30:23` | `5.8%` | `89.57%` | 224 | 119 | `+52.4s` |
| `2026-10-27 00:30:55` | `7.86%` | `86.05%` | 280 | 152 | `+46.9s` |
| `2026-10-26 23:00:23` | `5.58%` | `84.32%` | 466 | 281 | `+46.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T05:00:23.046000+00:00`.*
