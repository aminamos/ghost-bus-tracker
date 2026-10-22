# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** Cleveland | **Location:** Cleveland, OH | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:17:49.145000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.23%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.78%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `436` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `317` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+289.4s` (`+4.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+156.0s` (`+2.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 169 | 38.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 1.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 41 | 9.4% |
| 🔴 **Severe Delay** | Over 15m late | 8 | 1.8% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 0.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 26** | 19 | 10 | 1 | **`5.26%`** | `40.0%` | `+8.6 min` |
| **Route 19** | 20 | 10 | 0 | **`0.0%`** | `81.82%` | `+2.8 min` |
| **Route 14** | 20 | 10 | 0 | **`0.0%`** | `85.71%` | `+2.2 min` |
| **Route 31** | 6 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.7 min` |
| **Route 15** | 20 | 10 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 41** | 24 | 15 | 0 | **`0.0%`** | `72.73%` | `+3.0 min` |
| **Route 10** | 20 | 10 | 0 | **`0.0%`** | `53.85%` | `+16.2 min` |
| **Route 3** | 12 | 6 | 0 | **`0.0%`** | `83.33%` | `+1.8 min` |
| **Route 1** | 12 | 6 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 28** | 12 | 6 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 66** | `+24.1 min (+1445.2s)` | `+129.3 min (+7759s)` | 6 | `66.67%` |
| **Route 10** | `+16.2 min (+971.5s)` | `+157.6 min (+9457s)` | 10 | `53.85%` |
| **Route 22** | `+8.8 min (+527.0s)` | `+22.7 min (+1362s)` | 10 | `40.0%` |
| **Route 26** | `+8.6 min (+515.9s)` | `+22.6 min (+1359s)` | 10 | `40.0%` |
| **Route 78** | `+6.7 min (+403.8s)` | `+13.9 min (+835s)` | 4 | `50.0%` |
| **Route 48** | `+6.6 min (+396.0s)` | `+17.5 min (+1048s)` | 4 | `66.67%` |
| **Route 9** | `+5.8 min (+347.1s)` | `+12.7 min (+761s)` | 7 | `55.56%` |
| **Route 50** | `+5.3 min (+320.9s)` | `+10.7 min (+642s)` | 4 | `57.14%` |
| **Route 71** | `+5.0 min (+300.6s)` | `+11.6 min (+698s)` | 5 | `60.0%` |
| **Route 18** | `+4.9 min (+293.5s)` | `+11.7 min (+699s)` | 3 | `75.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 66** | ~15.0m | ~15.0m | **`+2.1 min`** | `0.0 / 100` |
| **Route 10** | ~15.0m | ~15.0m | **`+1.6 min`** | `0.0 / 100` |
| **Route 22** | ~15.0m | ~15.0m | **`+0.0 min`** | `46.2 / 100` |
| **Route 26** | ~16.0m | ~16.0m | **`+0.0 min`** | `52.7 / 100` |
| **Route 10** | ~27.0m | ~27.0m | **`+0.0 min`** | `70.0 / 100` |
| **Route 22** | ~15.0m | ~15.0m | **`+0.0 min`** | `59.6 / 100` |
| **Route 26** | ~16.0m | ~16.0m | **`+0.0 min`** | `66.4 / 100` |
| **Route 51** | ~6.0m | ~6.0m | **`+0.0 min`** | `56.4 / 100` |
| **Route 78** | ~30.0m | ~30.0m | **`+0.0 min`** | `80.8 / 100` |
| **Route 14** | ~16.0m | ~16.0m | **`+0.0 min`** | `76.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19228648` | Route 26 | `14:38:00` | `SCHEDULED` | Assigned vehicle 2455 is broadcasting off-schedule with no vehicle covering 19228648 |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:49.145000+00:00`.*
