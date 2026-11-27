# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-27T07:00:18.069000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.04%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `46` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `46` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+102.8s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+53.0s` (`+0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 29 | 63.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 19.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 17.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-235.7s` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 22** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `+2.8 min` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+2.5 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+2.8 min` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 63** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-161.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 2** | `+9.7 min (+582.0s)` | `+9.7 min (+582s)` | 1 | `0.0%` |
| **Route 54** | `+9.4 min (+567.0s)` | `+9.4 min (+567s)` | 1 | `0.0%` |
| **Route 924** | `+4.5 min (+268.3s)` | `+11.9 min (+714s)` | 3 | `66.67%` |
| **Route 323** | `+3.8 min (+229.0s)` | `+3.8 min (+229s)` | 1 | `100.0%` |
| **Route 923** | `+3.7 min (+220.7s)` | `+5.4 min (+324s)` | 3 | `33.33%` |
| **Route 18** | `+3.0 min (+180.0s)` | `+4.2 min (+255s)` | 3 | `100.0%` |
| **Route 22** | `+2.8 min (+169.0s)` | `+9.2 min (+551s)` | 3 | `33.33%` |
| **Route 4** | `+2.8 min (+165.3s)` | `+5.8 min (+345s)` | 3 | `66.67%` |
| **Route 724** | `+2.7 min (+162.0s)` | `+2.7 min (+162s)` | 1 | `100.0%` |
| **Route 922** | `+2.6 min (+154.5s)` | `+4.2 min (+254s)` | 2 | `100.0%` |

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
| `2026-11-27 07:00:18` | `0.0%` | `63.04%` | 46 | 46 | `+102.8s` |
| `2026-11-27 06:30:18` | `0.0%` | `72.04%` | 93 | 93 | `+81.3s` |
| `2026-11-27 06:00:17` | `2.13%` | `68.12%` | 141 | 138 | `+69.7s` |
| `2026-11-27 05:30:18` | `5.11%` | `68.86%` | 176 | 167 | `+66.6s` |
| `2026-11-27 05:00:17` | `4.82%` | `71.43%` | 228 | 217 | `+58.3s` |
| `2026-11-27 04:30:18` | `5.51%` | `73.15%` | 272 | 257 | `+64.9s` |
| `2026-11-27 04:00:17` | `6.31%` | `78.37%` | 301 | 282 | `+53.0s` |
| `2026-11-27 03:30:18` | `8.16%` | `75.0%` | 331 | 304 | `+47.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:18.069000+00:00`.*
