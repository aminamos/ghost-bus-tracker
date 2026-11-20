# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-20T06:30:18.265000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.22%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `107` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `107` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+27.6s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-2.0s` (`-0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 73 | 68.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 29 | 27.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 4.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-22.0s` |
| **Route 11** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+2.2 min` |
| **Route 14** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-24.2s` |
| **Route 17** | 5 | 4 | 0 | **`0.0%`** | `60.0%` | `-32.6s` |
| **Route 18** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+1.5 min` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.8 min` |
| **Route 22** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `-73.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-38.0s` |
| **Route 323** | 3 | 2 | 0 | **`0.0%`** | `66.67%` | `-12.7s` |
| **Route 36** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 923** | `+4.8 min (+285.8s)` | `+12.7 min (+760s)` | 3 | `60.0%` |
| **Route 925** | `+3.6 min (+215.8s)` | `+8.0 min (+477s)` | 3 | `75.0%` |
| **Route 54** | `+2.4 min (+146.0s)` | `+4.5 min (+270s)` | 2 | `100.0%` |
| **Route 11** | `+2.2 min (+130.8s)` | `+5.1 min (+308s)` | 4 | `50.0%` |
| **Route 9** | `+2.0 min (+122.0s)` | `+3.6 min (+215s)` | 2 | `100.0%` |
| **Route 2** | `+1.8 min (+105.7s)` | `+4.7 min (+284s)` | 3 | `100.0%` |
| **Route 68** | `+1.6 min (+96.8s)` | `+4.4 min (+266s)` | 3 | `75.0%` |
| **Route 18** | `+1.5 min (+89.0s)` | `+4.1 min (+248s)` | 5 | `80.0%` |
| **Route 922** | `+1.2 min (+72.0s)` | `+8.9 min (+533s)` | 5 | `50.0%` |
| **Route 901** | `+1.0 min (+60.0s)` | `+1.0 min (+60s)` | 1 | `100.0%` |

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
| `2026-11-20 06:30:18` | `0.0%` | `68.22%` | 107 | 107 | `+27.6s` |
| `2026-11-20 05:30:18` | `3.81%` | `58.8%` | 236 | 216 | `+7.2s` |
| `2026-11-20 05:00:18` | `4.98%` | `57.71%` | 281 | 253 | `-2.5s` |
| `2026-11-20 04:30:17` | `5.37%` | `63.64%` | 354 | 319 | `+17.4s` |
| `2026-11-20 04:00:18` | `7.21%` | `61.24%` | 402 | 356 | `+26.6s` |
| `2026-11-20 03:30:18` | `8.65%` | `63.08%` | 451 | 390 | `+15.7s` |
| `2026-11-20 03:00:18` | `8.17%` | `64.35%` | 502 | 432 | `+24.1s` |
| `2026-11-20 02:30:18` | `8.29%` | `63.7%` | 531 | 460 | `+24.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T06:30:18.265000+00:00`.*
