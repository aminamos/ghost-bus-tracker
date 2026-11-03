# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-03T07:00:18.571000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.86%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `35` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `205` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+148.2s` (`+2.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+111.5s` (`+1.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 15 | 42.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 2.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 11.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 14** | 3 | 2 | 1 | **`33.33%`** | `50.0%` | `+5.6 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `50.0%` | `+6.1 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `50.0%` | `+2.8 min` |
| **Route 19** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+4.2 min` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `-10.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | `+6.1 min (+366.0s)` | `+10.2 min (+612s)` | 2 | `50.0%` |
| **Route 14** | `+5.6 min (+338.0s)` | `+8.1 min (+488s)` | 2 | `50.0%` |
| **Route 19** | `+4.2 min (+250.0s)` | `+4.2 min (+250s)` | 1 | `100.0%` |
| **Route 26** | `+2.8 min (+169.0s)` | `+5.3 min (+319s)` | 2 | `50.0%` |
| **Route 41** | `+1.6 min (+98.3s)` | `+2.2 min (+130s)` | 3 | `100.0%` |
| **Route 6** | `+1.3 min (+79.0s)` | `+2.2 min (+133s)` | 3 | `100.0%` |
| **Route 48** | `+1.1 min (+68.0s)` | `+1.1 min (+68s)` | 2 | `100.0%` |
| **Route 28** | `+0.2 min (+12.0s)` | `+0.2 min (+12s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | ~60.0m | ~60.0m | **`+0.0 min`** | `93.4 / 100` |
| **Route 10** | ~71.0m | ~71.0m | **`+0.0 min`** | `95.4 / 100` |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `84.6 / 100` |
| **Route 6** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19234615` | Route 14 | `07:43:00` | `SCHEDULED` | Assigned vehicle 2397 is broadcasting off-schedule with no vehicle covering 19234615 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `2.86%` | `75.0%` | 35 | 205 | `+148.2s` |
| `2026-11-03 06:30:21` | `2.04%` | `73.33%` | 49 | 202 | `-1127.5s` |
| `2026-11-03 05:30:18` | `5.94%` | `76.27%` | 101 | 208 | `-1153.6s` |
| `2026-11-03 05:00:21` | `4.62%` | `69.84%` | 130 | 239 | `+1165.1s` |
| `2026-11-03 04:30:19` | `2.68%` | `81.01%` | 149 | 230 | `+162.2s` |
| `2026-11-03 04:00:19` | `0.58%` | `75.61%` | 173 | 228 | `+192.2s` |
| `2026-11-03 03:30:19` | `1.02%` | `69.07%` | 196 | 213 | `+418.8s` |
| `2026-11-03 03:00:18` | `0.0%` | `77.66%` | 206 | 220 | `+231.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.571000+00:00`.*
