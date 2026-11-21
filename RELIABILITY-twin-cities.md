# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-21T07:00:18.226000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.67%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.79%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `58` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+81.0s` (`+1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+33.0s` (`+0.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 61.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 16 | 26.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 5.0% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 1.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 1.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `+1.5 min` |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.0 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-78.5s` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-81.5s` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+6.2 min` |
| **Route 2** | 4 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.9 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-8.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `20.0%` | `+2.1 min` |
| **Route 36** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.5 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-167.7s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+17.7 min (+1060.0s)` | `+17.7 min (+1060s)` | 1 | `0.0%` |
| **Route 18** | `+6.2 min (+374.0s)` | `+16.2 min (+974s)` | 3 | `66.67%` |
| **Route 2** | `+4.9 min (+295.3s)` | `+10.9 min (+654s)` | 3 | `66.67%` |
| **Route 36** | `+3.5 min (+209.5s)` | `+7.5 min (+453s)` | 2 | `50.0%` |
| **Route 925** | `+2.9 min (+173.0s)` | `+4.4 min (+266s)` | 2 | `100.0%` |
| **Route 922** | `+2.7 min (+159.5s)` | `+4.0 min (+238s)` | 4 | `100.0%` |
| **Route 3** | `+2.1 min (+126.2s)` | `+11.0 min (+662s)` | 5 | `20.0%` |
| **Route 923** | `+1.9 min (+117.0s)` | `+3.1 min (+185s)` | 2 | `100.0%` |
| **Route 62** | `+1.7 min (+101.5s)` | `+4.1 min (+247s)` | 1 | `100.0%` |
| **Route 17** | `+1.5 min (+89.0s)` | `+1.8 min (+109s)` | 2 | `100.0%` |

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
| `743006` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `1.67%` | `63.79%` | 60 | 58 | `+81.0s` |
| `2026-11-21 06:00:18` | `2.37%` | `65.03%` | 169 | 163 | `+2.5s` |
| `2026-11-21 05:30:17` | `4.39%` | `59.91%` | 228 | 217 | `+30.5s` |
| `2026-11-21 05:00:18` | `5.54%` | `59.22%` | 271 | 255 | `+15.0s` |
| `2026-11-21 04:30:18` | `6.51%` | `57.91%` | 338 | 316 | `+33.9s` |
| `2026-11-21 04:00:17` | `7.69%` | `61.28%` | 390 | 359 | `+40.2s` |
| `2026-11-21 03:30:17` | `9.17%` | `60.91%` | 436 | 394 | `+36.8s` |
| `2026-11-21 03:00:17` | `9.54%` | `63.28%` | 482 | 433 | `+36.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.226000+00:00`.*
