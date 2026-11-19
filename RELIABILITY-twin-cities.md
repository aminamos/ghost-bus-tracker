# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-19T07:00:18.637000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.5%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `56` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `56` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+42.4s` (`+0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+20.5s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 35 | 62.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 16 | 28.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 5 | 8.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.5 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+1.6 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-49.0s` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+1.3 min` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.9 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-105.0s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `40.0%` | `+1.2 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-105.3s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+14.7 min (+879.0s)` | `+14.7 min (+879s)` | 1 | `0.0%` |
| **Route 924** | `+4.4 min (+265.2s)` | `+7.8 min (+467s)` | 4 | `50.0%` |
| **Route 923** | `+3.3 min (+195.7s)` | `+6.9 min (+415s)` | 2 | `66.67%` |
| **Route 18** | `+2.9 min (+176.0s)` | `+4.5 min (+273s)` | 2 | `100.0%` |
| **Route 925** | `+2.6 min (+158.5s)` | `+4.1 min (+247s)` | 2 | `100.0%` |
| **Route 921** | `+2.2 min (+134.0s)` | `+4.3 min (+256s)` | 2 | `100.0%` |
| **Route 11** | `+1.6 min (+94.5s)` | `+4.4 min (+266s)` | 2 | `50.0%` |
| **Route 17** | `+1.3 min (+77.0s)` | `+4.0 min (+240s)` | 3 | `66.67%` |
| **Route 3** | `+1.2 min (+72.2s)` | `+5.0 min (+303s)` | 5 | `40.0%` |
| **Route 5** | `+1.0 min (+61.5s)` | `+1.8 min (+108s)` | 2 | `100.0%` |

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
| `2026-11-19 07:00:18` | `0.0%` | `62.5%` | 56 | 56 | `+42.4s` |
| `2026-11-19 06:30:18` | `0.0%` | `70.0%` | 110 | 110 | `+27.5s` |
| `2026-11-19 05:00:18` | `5.24%` | `58.94%` | 286 | 263 | `+9.3s` |
| `2026-11-19 04:30:18` | `5.68%` | `58.64%` | 352 | 324 | `+12.7s` |
| `2026-11-19 04:00:18` | `7.75%` | `59.72%` | 400 | 360 | `+19.8s` |
| `2026-11-19 03:30:18` | `8.5%` | `59.75%` | 447 | 400 | `+8.0s` |
| `2026-11-19 03:00:18` | `8.75%` | `64.1%` | 480 | 431 | `+17.6s` |
| `2026-11-19 02:30:17` | `9.07%` | `63.79%` | 529 | 465 | `+22.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-19T07:00:18.637000+00:00`.*
