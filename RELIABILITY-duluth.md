# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Duluth Transit Authority** in **Duluth, MN** (Duluth–Superior Metropolitan Area, Minnesota).
> **Transit System:** Duluth | **Location:** Duluth, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:17:47.681000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`94.44%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `36` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `36` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+109.3s` (`+1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+75.0s` (`+1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 34 | 94.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 5.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 112** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 110** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 101** | 7 | 7 | 0 | **`0.0%`** | `85.71%` | `+2.4 min` |
| **Route 103** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |
| **Route 106** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 102** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 108** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.6 min` |
| **Route 104** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 107** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 105** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 210** | `+4.4 min (+263.0s)` | `+4.4 min (+263s)` | 1 | `100.0%` |
| **Route 108** | `+3.6 min (+216.0s)` | `+5.5 min (+330s)` | 2 | `50.0%` |
| **Route 109** | `+2.5 min (+150.0s)` | `+2.5 min (+150s)` | 1 | `100.0%` |
| **Route 101** | `+2.4 min (+144.4s)` | `+6.2 min (+375s)` | 7 | `85.71%` |
| **Route 112** | `+2.1 min (+127.5s)` | `+4.2 min (+255s)` | 2 | `100.0%` |
| **Route 102** | `+1.9 min (+114.0s)` | `+4.5 min (+270s)` | 5 | `100.0%` |
| **Route 103** | `+1.8 min (+109.8s)` | `+3.5 min (+210s)` | 5 | `100.0%` |
| **Route 106** | `+1.5 min (+90.0s)` | `+1.8 min (+105s)` | 2 | `100.0%` |
| **Route 107** | `+1.4 min (+82.5s)` | `+2.8 min (+165s)` | 2 | `100.0%` |
| **Route 110** | `+1.1 min (+65.0s)` | `+1.2 min (+75s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 101** | ~14.5m | ~14.5m | **`+0.0 min`** | `85.2 / 100` |
| **Route 101** | ~15.0m | ~15.0m | **`+0.0 min`** | `87.6 / 100` |
| **Route 102** | ~15.0m | ~15.0m | **`+0.0 min`** | `88.3 / 100` |
| **Route 107** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.4 / 100` |
| **Route 103** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.0 / 100` |
| **Route 102** | ~15.0m | ~15.0m | **`+0.0 min`** | `96.6 / 100` |
| **Route 103** | ~46.0m | ~46.0m | **`+0.0 min`** | `97.7 / 100` |
| **Route 110** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.2 / 100` |
| **Route 104** | ~29.0m | ~29.0m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:47.681000+00:00`.*
