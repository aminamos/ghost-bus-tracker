# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Bi-State Development)** in **St. Louis, MO** (St. Louis Metropolitan Area, Missouri).
> **Transit System:** Metro Transit | **Location:** St. Louis, MO | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-02T07:00:18.454000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`70.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `31` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `17` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+168.0s` (`+2.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+150.0s` (`+2.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 7 | 22.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 3.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 6.5% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 14 | 45.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19778** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 19768** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route UNKNOWN** | 14 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 19757** | `+8.0 min (+480.0s)` | `+8.0 min (+480s)` | 1 | `0.0%` |
| **Route 19749** | `+6.0 min (+360.0s)` | `+6.0 min (+360s)` | 1 | `0.0%` |
| **Route 19792** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |
| **Route 19777** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 19781** | `+3.0 min (+180.0s)` | `+3.0 min (+180s)` | 1 | `100.0%` |
| **Route 19778** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |
| **Route 19768** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 2 | `100.0%` |
| **Route 19789** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

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
| `2026-11-02 07:00:18` | `0.0%` | `70.0%` | 31 | 17 | `+168.0s` |
| `2026-11-02 06:30:18` | `0.0%` | `83.87%` | 52 | 36 | `+60.0s` |
| `2026-11-02 06:00:23` | `0.0%` | `81.4%` | 73 | 54 | `+87.9s` |
| `2026-11-02 05:30:22` | `0.0%` | `87.5%` | 67 | 60 | `+96.2s` |
| `2026-11-02 05:00:19` | `0.0%` | `78.95%` | 69 | 66 | `+178.9s` |
| `2026-11-02 04:30:21` | `0.0%` | `84.31%` | 72 | 63 | `+122.4s` |
| `2026-11-02 04:00:18` | `0.0%` | `82.26%` | 80 | 74 | `+85.2s` |
| `2026-11-02 03:30:25` | `0.0%` | `81.67%` | 76 | 73 | `+99.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.454000+00:00`.*
