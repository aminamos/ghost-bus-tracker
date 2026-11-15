# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-15T07:00:18.040000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.96%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`62.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `51` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `50` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+5.4s` (`+0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+3.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 31 | 60.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 16 | 31.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 5.9% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 2.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 922** | 4 | 3 | 1 | **`25.0%`** | `66.67%` | `+0.6 min` |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 17** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-6.7s` |
| **Route 18** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.6 min` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.6 min` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-402.5s` |
| **Route 3** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+5.0 min` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-63.0s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-26.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 3** | `+5.0 min (+301.0s)` | `+6.1 min (+368s)` | 4 | `50.0%` |
| **Route 921** | `+2.8 min (+167.5s)` | `+3.8 min (+225s)` | 2 | `100.0%` |
| **Route 2** | `+2.6 min (+158.5s)` | `+4.3 min (+256s)` | 2 | `100.0%` |
| **Route 18** | `+2.6 min (+157.3s)` | `+4.5 min (+267s)` | 3 | `100.0%` |
| **Route 923** | `+1.7 min (+102.0s)` | `+2.0 min (+122s)` | 3 | `100.0%` |
| **Route 11** | `+1.2 min (+73.5s)` | `+2.4 min (+143s)` | 2 | `100.0%` |
| **Route 61** | `+1.1 min (+64.0s)` | `+1.1 min (+64s)` | 1 | `100.0%` |
| **Route 922** | `+0.6 min (+33.0s)` | `+2.5 min (+147s)` | 3 | `66.67%` |
| **Route 63** | `+0.4 min (+21.5s)` | `+1.9 min (+112s)` | 2 | `50.0%` |
| **Route 10** | `+0.1 min (+5.5s)` | `+0.1 min (+7s)` | 2 | `100.0%` |

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
| `916176` | Route 922 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:18` | `1.96%` | `62.0%` | 51 | 50 | `+5.4s` |
| `2026-11-15 06:30:18` | `0.97%` | `69.61%` | 103 | 102 | `+66.3s` |
| `2026-11-15 05:30:18` | `4.21%` | `73.17%` | 214 | 205 | `+104.7s` |
| `2026-11-15 05:00:18` | `5.24%` | `75.0%` | 267 | 253 | `+101.5s` |
| `2026-11-15 04:30:18` | `5.9%` | `73.93%` | 322 | 303 | `+128.9s` |
| `2026-11-15 04:00:18` | `8.06%` | `76.74%` | 360 | 331 | `+126.4s` |
| `2026-11-15 03:30:18` | `9.3%` | `77.5%` | 398 | 361 | `+98.5s` |
| `2026-11-15 03:00:18` | `9.45%` | `78.63%` | 434 | 393 | `+93.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:18.040000+00:00`.*
