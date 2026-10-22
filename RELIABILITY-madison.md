# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (City of Madison)** in **Madison, WI** (Madison Metropolitan Area, Wisconsin).
> **Transit System:** Madison | **Location:** Madison, WI | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:54.750000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`51.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.93%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `226` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `92` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `116` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+68.1s` (`+1.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+15.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 82 | 36.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 18 | 8.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 3.1% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.4% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 116 | 51.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.9% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route S** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+21.7 min` |
| **Route P** | 3 | 2 | 2 | **`66.67%`** | `0.0%` | `-82.0s` |
| **Route W** | 3 | 2 | 2 | **`66.67%`** | `100.0%` | `+2.4 min` |
| **Route A** | 20 | 11 | 13 | **`65.0%`** | `100.0%` | `+1.6 min` |
| **Route 80** | 27 | 9 | 16 | **`59.26%`** | `45.45%` | `-76.1s` |
| **Route O** | 12 | 3 | 7 | **`58.33%`** | `100.0%` | `+2.2 min` |
| **Route F** | 9 | 5 | 5 | **`55.56%`** | `75.0%` | `+2.2 min` |
| **Route H** | 9 | 5 | 5 | **`55.56%`** | `100.0%` | `+2.3 min` |
| **Route J** | 9 | 4 | 5 | **`55.56%`** | `50.0%` | `+3.7 min` |
| **Route C** | 19 | 9 | 10 | **`52.63%`** | `77.78%` | `+1.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route S** | `+21.7 min (+1301.0s)` | `+21.7 min (+1301s)` | 1 | `0.0%` |
| **Route 38** | `+4.5 min (+268.2s)` | `+12.9 min (+777s)` | 4 | `25.0%` |
| **Route J** | `+3.7 min (+220.5s)` | `+11.0 min (+658s)` | 4 | `50.0%` |
| **Route W** | `+2.4 min (+141.0s)` | `+2.4 min (+141s)` | 2 | `100.0%` |
| **Route H** | `+2.3 min (+140.5s)` | `+4.3 min (+257s)` | 5 | `100.0%` |
| **Route F** | `+2.2 min (+133.0s)` | `+5.2 min (+314s)` | 5 | `75.0%` |
| **Route O** | `+2.2 min (+132.6s)` | `+4.5 min (+272s)` | 3 | `100.0%` |
| **Route A** | `+1.6 min (+97.1s)` | `+4.3 min (+256s)` | 11 | `100.0%` |
| **Route D** | `+1.3 min (+77.5s)` | `+9.7 min (+581s)` | 12 | `75.0%` |
| **Route C** | `+1.3 min (+77.4s)` | `+6.7 min (+403s)` | 9 | `77.78%` |

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
| `511020` | Route D | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3808020` | Route E | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2484020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3327020` | Route L | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1513020` | Route C | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3631020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `420020` | Route 84 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `695020` | Route P | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3666020` | Route 38 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `88020` | Route H | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1667020` | Route C | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2880020` | Route R | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2633020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `121020` | Route B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3930020` | Route O | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:54.750000+00:00`.*
