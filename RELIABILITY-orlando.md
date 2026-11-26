# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Central Florida Regional Transportation Authority** in **Orlando, FL** (Orlando Metropolitan Area, Florida).
> **Transit System:** LYNX | **Location:** Orlando, FL | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-26T06:00:17.815000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`42.86%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `14` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+460.4s` (`+7.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+412.0s` (`+6.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 6 | 42.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 50.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 7.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17567** | 5 | 4 | 0 | **`0.0%`** | `40.0%` | `+5.7 min` |
| **Route 17585** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.6 min` |
| **Route 17579** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+5.2 min` |
| **Route 17604** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17583** | `+32.8 min (+1968.0s)` | `+32.8 min (+1968s)` | 1 | `0.0%` |
| **Route 17574** | `+13.9 min (+836.0s)` | `+13.9 min (+836s)` | 1 | `0.0%` |
| **Route 17567** | `+5.7 min (+340.2s)` | `+12.4 min (+742s)` | 4 | `40.0%` |
| **Route 17585** | `+5.6 min (+333.5s)` | `+9.1 min (+545s)` | 2 | `50.0%` |
| **Route 17579** | `+5.2 min (+309.5s)` | `+7.9 min (+472s)` | 2 | `50.0%` |
| **Route 17604** | `+4.5 min (+271.5s)` | `+7.6 min (+456s)` | 2 | `50.0%` |
| **Route 17608** | `+1.9 min (+112.0s)` | `+1.9 min (+112s)` | 1 | `100.0%` |

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
| `2026-11-26 06:00:17` | `0.0%` | `42.86%` | 14 | 13 | `+460.4s` |
| `2026-11-26 05:00:17` | `3.51%` | `72.73%` | 57 | 42 | `+257.8s` |
| `2026-11-26 04:30:19` | `2.3%` | `76.47%` | 87 | 52 | `+217.2s` |
| `2026-11-26 03:00:17` | `0.0%` | `81.55%` | 233 | 103 | `+169.3s` |
| `2026-11-26 02:30:18` | `0.72%` | `86.64%` | 279 | 107 | `+146.1s` |
| `2026-11-26 01:00:17` | `0.63%` | `83.47%` | 475 | 158 | `+199.0s` |
| `2026-11-25 23:00:18` | `1.87%` | `87.59%` | 747 | 211 | `+152.9s` |
| `2026-11-25 22:30:18` | `2.45%` | `89.01%` | 774 | 209 | `+131.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-26T06:00:17.815000+00:00`.*
