# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-12T07:00:20.041000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.73%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `63` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `362` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+179.5s` (`+3.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+41.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 37 | 58.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 11 | 17.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 13 | 20.6% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+0.1 min` |
| **Route 16** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+4.6 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-66.7s` |
| **Route 32** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.5 min` |
| **Route 3** | 4 | 3 | 0 | **`0.0%`** | `25.0%` | `+20.3 min` |
| **Route 51** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+8.6 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.3 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+5.3 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 3** | `+20.3 min (+1215.5s)` | `+48.6 min (+2919s)` | 3 | `25.0%` |
| **Route FBUZ** | `+9.6 min (+573.0s)` | `+9.6 min (+573s)` | 1 | `0.0%` |
| **Route 51** | `+8.6 min (+513.0s)` | `+9.1 min (+546s)` | 2 | `0.0%` |
| **Route 7** | `+6.1 min (+364.7s)` | `+10.0 min (+602s)` | 3 | `33.33%` |
| **Route 17** | `+5.3 min (+315.3s)` | `+10.2 min (+614s)` | 3 | `66.67%` |
| **Route 16** | `+4.6 min (+275.5s)` | `+6.2 min (+371s)` | 3 | `50.0%` |
| **Route S** | `+4.0 min (+240.0s)` | `+14.0 min (+840s)` | 2 | `0.0%` |
| **Route 32** | `+3.5 min (+209.0s)` | `+4.2 min (+249s)` | 2 | `100.0%` |
| **Route 41** | `+3.3 min (+200.0s)` | `+6.2 min (+371s)` | 2 | `50.0%` |
| **Route B** | `+3.2 min (+190.0s)` | `+8.0 min (+480s)` | 6 | `66.67%` |

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
| `2026-11-12 07:00:20` | `0.0%` | `58.73%` | 63 | 362 | `+179.5s` |
| `2026-11-12 06:30:19` | `0.0%` | `72.0%` | 150 | 391 | `+172.7s` |
| `2026-11-12 06:00:20` | `2.22%` | `76.14%` | 270 | 410 | `+145.8s` |
| `2026-11-12 05:30:19` | `3.47%` | `80.39%` | 317 | 428 | `+166.8s` |
| `2026-11-12 05:00:20` | `3.8%` | `77.4%` | 368 | 471 | `+145.4s` |
| `2026-11-12 04:30:20` | `5.06%` | `76.27%` | 395 | 489 | `+155.8s` |
| `2026-11-12 04:00:20` | `4.21%` | `80.0%` | 428 | 537 | `+162.2s` |
| `2026-11-12 03:30:19` | `2.83%` | `79.42%` | 460 | 566 | `+195.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:20.041000+00:00`.*
