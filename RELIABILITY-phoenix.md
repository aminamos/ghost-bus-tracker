# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-26T07:00:23.399000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.75%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `50` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `268` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+174.8s` (`+2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+71.5s` (`+1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 33 | 66.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 12.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 16.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 2.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 4.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 43** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+27.2 min` |
| **Route 27** | 4 | 3 | 0 | **`0.0%`** | `66.67%` | `+5.3 min` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 3** | 2 | 3 | 0 | **`0.0%`** | `0.0%` | `+2.1 min` |
| **Route 7** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `+6.0 min` |
| **Route 19** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.8 min` |
| **Route 29** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+3.5 min` |
| **Route 50** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-42.7s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 43** | `+27.2 min (+1634.5s)` | `+52.3 min (+3138s)` | 2 | `50.0%` |
| **Route 12** | `+9.0 min (+542.0s)` | `+9.0 min (+542s)` | 1 | `0.0%` |
| **Route 51** | `+8.2 min (+495.0s)` | `+8.2 min (+495s)` | 1 | `0.0%` |
| **Route 7** | `+6.0 min (+358.5s)` | `+8.2 min (+492s)` | 3 | `50.0%` |
| **Route 27** | `+5.3 min (+319.7s)` | `+12.1 min (+726s)` | 3 | `66.67%` |
| **Route 77** | `+4.8 min (+285.0s)` | `+4.8 min (+285s)` | 1 | `100.0%` |
| **Route 17** | `+3.8 min (+228.0s)` | `+5.7 min (+344s)` | 2 | `50.0%` |
| **Route 29** | `+3.5 min (+212.0s)` | `+9.6 min (+575s)` | 3 | `66.67%` |
| **Route 41** | `+3.5 min (+211.5s)` | `+4.5 min (+267s)` | 2 | `100.0%` |
| **Route 3** | `+2.1 min (+126.0s)` | `+5.8 min (+350s)` | 3 | `0.0%` |

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
| `2026-10-26 07:00:23` | `0.0%` | `68.75%` | 50 | 268 | `+174.8s` |
| `2026-10-26 06:30:41` | `0.0%` | `69.84%` | 128 | 293 | `+199.5s` |
| `2026-10-26 05:00:28` | `2.6%` | `72.41%` | 269 | 330 | `+210.0s` |
| `2026-10-26 04:00:20` | `1.94%` | `72.19%` | 310 | 348 | `+254.6s` |
| `2026-10-26 03:30:41` | `4.4%` | `67.77%` | 318 | 366 | `+259.6s` |
| `2026-10-26 01:00:30` | `2.36%` | `69.51%` | 381 | 380 | `+264.8s` |
| `2026-10-26 00:30:46` | `3.83%` | `73.24%` | 392 | 353 | `+251.2s` |
| `2026-10-25 23:30:23` | `3.3%` | `71.31%` | 394 | 356 | `+190.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:23.399000+00:00`.*
