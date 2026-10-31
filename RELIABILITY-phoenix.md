# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-31T07:00:32.058000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`51.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `61` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `347` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+458.4s` (`+7.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+163.0s` (`+2.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 31 | 50.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 13.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 13 | 21.3% |
| 🔴 **Severe Delay** | Over 15m late | 8 | 13.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 1.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-38.8s` |
| **Route 35** | 3 | 4 | 0 | **`0.0%`** | `66.67%` | `+3.8 min` |
| **Route 16** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+8.9 min` |
| **Route 27** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.6 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+38.5 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+15.8 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-97.0s` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+1.4 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+5.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 106** | `+77.9 min (+4676.0s)` | `+77.9 min (+4676s)` | 1 | `0.0%` |
| **Route 10** | `+56.5 min (+3390.0s)` | `+56.5 min (+3390s)` | 1 | `0.0%` |
| **Route 41** | `+38.5 min (+2310.0s)` | `+77.0 min (+4620s)` | 2 | `50.0%` |
| **Route 28** | `+36.4 min (+2184.0s)` | `+36.4 min (+2184s)` | 1 | `0.0%` |
| **Route 17** | `+15.8 min (+947.0s)` | `+16.6 min (+993s)` | 3 | `0.0%` |
| **Route 51** | `+13.1 min (+786.0s)` | `+13.1 min (+786s)` | 1 | `0.0%` |
| **Route 72** | `+12.4 min (+746.0s)` | `+12.4 min (+746s)` | 1 | `0.0%` |
| **Route S** | `+11.0 min (+660.0s)` | `+11.0 min (+660s)` | 1 | `0.0%` |
| **Route 16** | `+8.9 min (+536.0s)` | `+18.4 min (+1102s)` | 3 | `33.33%` |
| **Route 29** | `+7.3 min (+435.3s)` | `+20.3 min (+1218s)` | 3 | `66.67%` |

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
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:32` | `0.0%` | `51.67%` | 61 | 347 | `+458.4s` |
| `2026-10-31 06:30:20` | `0.67%` | `63.45%` | 150 | 379 | `+323.0s` |
| `2026-10-31 06:00:20` | `4.09%` | `70.87%` | 269 | 396 | `+227.7s` |
| `2026-10-31 05:30:20` | `4.53%` | `73.01%` | 309 | 407 | `+244.1s` |
| `2026-10-31 04:30:22` | `3.19%` | `68.49%` | 407 | 466 | `+222.0s` |
| `2026-10-31 04:00:20` | `3.19%` | `70.15%` | 439 | 511 | `+208.9s` |
| `2026-10-31 03:30:18` | `3.61%` | `72.37%` | 443 | 540 | `+220.6s` |
| `2026-10-31 03:00:18` | `2.69%` | `69.71%` | 483 | 585 | `+246.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:32.058000+00:00`.*
