# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-11T07:00:19.171000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.93%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `61` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `358` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+186.0s` (`+3.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+59.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 39 | 63.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 16.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 9 | 14.8% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 4.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 4 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 35** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+2.9 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 27** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 3** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+17.0 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-42.5s` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 70** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+17.2 min` |
| **Route 50** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.5 min` |
| **Route 0** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 70** | `+17.2 min (+1031.3s)` | `+54.4 min (+3264s)` | 3 | `33.33%` |
| **Route 3** | `+17.0 min (+1018.0s)` | `+33.9 min (+2036s)` | 2 | `50.0%` |
| **Route 51** | `+10.7 min (+640.0s)` | `+10.7 min (+640s)` | 1 | `0.0%` |
| **Route 32** | `+10.3 min (+618.0s)` | `+10.3 min (+618s)` | 1 | `0.0%` |
| **Route FBUZ** | `+7.8 min (+468.0s)` | `+7.8 min (+468s)` | 1 | `0.0%` |
| **Route 72** | `+6.2 min (+373.0s)` | `+11.8 min (+706s)` | 2 | `50.0%` |
| **Route 8** | `+5.1 min (+305.0s)` | `+5.1 min (+305s)` | 1 | `0.0%` |
| **Route 50** | `+3.5 min (+211.0s)` | `+4.6 min (+278s)` | 2 | `100.0%` |
| **Route 17** | `+3.0 min (+180.0s)` | `+4.0 min (+243s)` | 2 | `100.0%` |
| **Route 35** | `+2.9 min (+172.2s)` | `+21.4 min (+1286s)` | 5 | `60.0%` |

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
| `2026-11-11 07:00:19` | `0.0%` | `63.93%` | 61 | 358 | `+186.0s` |
| `2026-11-11 06:30:19` | `0.67%` | `72.3%` | 149 | 395 | `+139.8s` |
| `2026-11-11 06:00:25` | `4.56%` | `76.89%` | 263 | 420 | `+151.3s` |
| `2026-11-11 05:30:20` | `2.87%` | `79.02%` | 314 | 446 | `+178.5s` |
| `2026-11-11 05:00:20` | `3.54%` | `74.01%` | 367 | 490 | `+182.1s` |
| `2026-11-11 04:30:20` | `4.55%` | `74.6%` | 396 | 518 | `+184.7s` |
| `2026-11-11 04:00:19` | `4.83%` | `79.19%` | 414 | 574 | `+165.1s` |
| `2026-11-11 03:00:20` | `3.84%` | `77.95%` | 469 | 638 | `+192.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-11T07:00:19.171000+00:00`.*
