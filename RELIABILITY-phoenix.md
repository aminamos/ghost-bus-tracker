# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-17T07:00:30.983000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.69%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.79%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `59` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `345` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+138.4s` (`+2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+51.5s` (`+0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 62.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 12 | 20.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 13.6% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 1.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 3 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 35** | 4 | 5 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 16** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+1.8 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.5 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.0 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-7.0s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+7.2 min` |
| **Route 70** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+0.0 min` |
| **Route 44** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+29.5 min` |
| **Route 50** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 44** | `+29.5 min (+1768.5s)` | `+59.9 min (+3593s)` | 3 | `50.0%` |
| **Route 17** | `+7.2 min (+435.0s)` | `+10.1 min (+607s)` | 2 | `50.0%` |
| **Route 32** | `+7.1 min (+426.0s)` | `+7.1 min (+426s)` | 2 | `0.0%` |
| **Route 13** | `+6.1 min (+368.0s)` | `+6.1 min (+368s)` | 1 | `0.0%` |
| **Route 51** | `+4.5 min (+273.0s)` | `+4.5 min (+273s)` | 1 | `100.0%` |
| **Route 27** | `+3.5 min (+210.0s)` | `+8.7 min (+524s)` | 3 | `66.67%` |
| **Route 3** | `+3.0 min (+180.5s)` | `+6.0 min (+361s)` | 2 | `50.0%` |
| **Route 90** | `+2.7 min (+162.0s)` | `+2.7 min (+162s)` | 1 | `100.0%` |
| **Route 138** | `+2.3 min (+138.0s)` | `+2.3 min (+138s)` | 1 | `100.0%` |
| **Route 16** | `+1.8 min (+109.0s)` | `+5.7 min (+344s)` | 3 | `33.33%` |

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
| `24784245` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 5321 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-17 07:00:30` | `1.69%` | `63.79%` | 59 | 345 | `+138.4s` |
| `2026-11-17 06:30:20` | `0.0%` | `72.22%` | 145 | 376 | `+228.2s` |
| `2026-11-17 06:00:24` | `4.56%` | `81.27%` | 263 | 400 | `+123.2s` |
| `2026-11-17 05:30:20` | `3.33%` | `79.66%` | 300 | 414 | `+162.1s` |
| `2026-11-17 05:00:20` | `3.09%` | `75.36%` | 356 | 448 | `+201.8s` |
| `2026-11-17 04:30:19` | `4.68%` | `75.96%` | 385 | 474 | `+179.4s` |
| `2026-11-17 04:00:19` | `3.6%` | `75.0%` | 417 | 555 | `+180.6s` |
| `2026-11-17 03:30:24` | `2.68%` | `76.57%` | 447 | 597 | `+182.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-17T07:00:30.983000+00:00`.*
