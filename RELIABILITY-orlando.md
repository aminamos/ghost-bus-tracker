# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Central Florida Regional Transportation Authority** in **Orlando, FL** (Orlando Metropolitan Area, Florida).
> **Transit System:** LYNX | **Location:** Orlando, FL | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-04T06:00:18.339000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.54%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `13` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `13` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+404.5s` (`+6.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+224.0s` (`+3.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 8 | 61.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 30.8% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 7.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17567** | 4 | 4 | 0 | **`0.0%`** | `25.0%` | `+10.3 min` |
| **Route 17585** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 17608** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+8.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17572** | `+14.0 min (+842.0s)` | `+14.0 min (+842s)` | 1 | `0.0%` |
| **Route 17567** | `+10.3 min (+618.5s)` | `+18.5 min (+1110s)` | 4 | `25.0%` |
| **Route 17608** | `+8.3 min (+501.0s)` | `+11.8 min (+708s)` | 2 | `50.0%` |
| **Route 17579** | `+3.7 min (+224.0s)` | `+3.7 min (+224s)` | 1 | `100.0%` |
| **Route 17614** | `+3.7 min (+222.0s)` | `+3.7 min (+222s)` | 1 | `100.0%` |
| **Route 17574** | `+3.7 min (+220.0s)` | `+3.7 min (+220s)` | 1 | `100.0%` |
| **Route 17585** | `+1.6 min (+95.0s)` | `+2.4 min (+142s)` | 2 | `100.0%` |
| **Route 17604** | `+1.4 min (+85.0s)` | `+1.4 min (+85s)` | 1 | `100.0%` |

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
| `2026-11-04 06:00:18` | `0.0%` | `61.54%` | 13 | 13 | `+404.5s` |
| `2026-11-04 05:30:17` | `0.0%` | `58.33%` | 36 | 29 | `+378.8s` |
| `2026-11-04 05:00:17` | `0.0%` | `71.43%` | 56 | 44 | `+255.8s` |
| `2026-11-04 04:30:17` | `1.15%` | `76.74%` | 87 | 52 | `+213.2s` |
| `2026-11-04 02:30:18` | `0.36%` | `90.58%` | 277 | 107 | `+111.0s` |
| `2026-11-04 01:30:18` | `0.0%` | `89.63%` | 406 | 134 | `+126.8s` |
| `2026-11-04 01:00:18` | `0.21%` | `86.78%` | 472 | 154 | `+171.1s` |
| `2026-11-04 00:30:18` | `1.11%` | `83.3%` | 541 | 173 | `+204.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T06:00:18.339000+00:00`.*
