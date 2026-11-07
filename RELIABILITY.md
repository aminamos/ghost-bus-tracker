# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-07T07:00:18.275000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`54.72%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `53` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `53` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+15.3s` (`+0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 29 | 54.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 21 | 39.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 5.7% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.0 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.0 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.5 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.3 min` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+2.7 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-41.0s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `20.0%` | `+0.7 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-71.7s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-105.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 925** | `+3.7 min (+220.5s)` | `+5.5 min (+328s)` | 2 | `50.0%` |
| **Route 2** | `+2.7 min (+164.0s)` | `+7.0 min (+417s)` | 2 | `0.0%` |
| **Route 923** | `+2.2 min (+132.5s)` | `+4.4 min (+265s)` | 1 | `100.0%` |
| **Route 18** | `+1.9 min (+113.5s)` | `+3.1 min (+188s)` | 2 | `100.0%` |
| **Route 922** | `+1.7 min (+101.5s)` | `+4.4 min (+266s)` | 4 | `100.0%` |
| **Route 17** | `+1.3 min (+76.0s)` | `+2.5 min (+150s)` | 3 | `100.0%` |
| **Route 11** | `+1.0 min (+62.5s)` | `+3.9 min (+231s)` | 2 | `50.0%` |
| **Route 10** | `+1.0 min (+59.5s)` | `+3.9 min (+235s)` | 2 | `50.0%` |
| **Route 64** | `+0.9 min (+55.5s)` | `+3.9 min (+236s)` | 1 | `50.0%` |
| **Route 3** | `+0.7 min (+44.0s)` | `+8.3 min (+496s)` | 5 | `20.0%` |

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
| `2026-11-07 07:00:18` | `0.0%` | `54.72%` | 53 | 53 | `+15.3s` |
| `2026-11-07 06:30:18` | `0.0%` | `64.81%` | 108 | 108 | `+16.9s` |
| `2026-11-07 06:00:18` | `4.12%` | `65.03%` | 170 | 163 | `+4.9s` |
| `2026-11-07 05:30:18` | `3.98%` | `62.21%` | 226 | 217 | `+37.3s` |
| `2026-11-07 05:00:18` | `4.23%` | `58.02%` | 284 | 262 | `+42.2s` |
| `2026-11-07 04:30:18` | `5.4%` | `59.44%` | 352 | 323 | `+51.5s` |
| `2026-11-07 04:00:18` | `7.14%` | `62.15%` | 392 | 354 | `+59.5s` |
| `2026-11-07 03:30:19` | `8.24%` | `60.05%` | 449 | 403 | `+40.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:18.275000+00:00`.*
