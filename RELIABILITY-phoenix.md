# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-16T07:00:20.594000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`59.32%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `60` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `281` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+345.7s` (`+5.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+49.0s` (`+0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 35 | 58.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 10 | 16.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 11.7% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 11.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 1.7% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+4.8 min` |
| **Route 16** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.3 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+10.7 min` |
| **Route 29** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-44.3s` |
| **Route 90** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 44** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-51.0s` |
| **Route 27** | 5 | 4 | 0 | **`0.0%`** | `25.0%` | `+6.0 min` |
| **Route 7** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+18.1 min` |
| **Route 35** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 32** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-28.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 106** | `+71.1 min (+4267.0s)` | `+80.4 min (+4825s)` | 1 | `0.0%` |
| **Route 61** | `+32.5 min (+1950.0s)` | `+32.5 min (+1950s)` | 1 | `0.0%` |
| **Route 60** | `+27.8 min (+1665.0s)` | `+27.8 min (+1665s)` | 1 | `0.0%` |
| **Route 7** | `+18.1 min (+1087.5s)` | `+35.5 min (+2132s)` | 2 | `50.0%` |
| **Route 17** | `+10.7 min (+644.0s)` | `+15.9 min (+954s)` | 2 | `0.0%` |
| **Route 170** | `+7.0 min (+419.0s)` | `+7.0 min (+419s)` | 1 | `0.0%` |
| **Route 27** | `+6.0 min (+361.5s)` | `+15.3 min (+921s)` | 4 | `25.0%` |
| **Route 19** | `+4.8 min (+289.0s)` | `+10.3 min (+617s)` | 3 | `0.0%` |
| **Route 16** | `+4.3 min (+255.3s)` | `+8.8 min (+527s)` | 3 | `66.67%` |
| **Route 51** | `+4.1 min (+247.0s)` | `+4.4 min (+266s)` | 2 | `100.0%` |

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
| `2026-11-16 07:00:20` | `0.0%` | `59.32%` | 60 | 281 | `+345.7s` |
| `2026-11-16 06:30:32` | `0.0%` | `67.18%` | 132 | 302 | `+267.4s` |
| `2026-11-16 06:00:24` | `4.39%` | `75.58%` | 228 | 321 | `+192.3s` |
| `2026-11-16 05:30:20` | `4.35%` | `72.2%` | 253 | 317 | `+210.9s` |
| `2026-11-16 05:00:21` | `3.25%` | `71.64%` | 277 | 334 | `+195.4s` |
| `2026-11-16 04:30:19` | `3.58%` | `74.15%` | 307 | 335 | `+211.0s` |
| `2026-11-16 04:00:19` | `2.19%` | `74.52%` | 320 | 350 | `+215.7s` |
| `2026-11-16 03:30:20` | `4.82%` | `72.52%` | 332 | 366 | `+241.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:20.594000+00:00`.*
