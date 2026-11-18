# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-18T06:30:18.476000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.92%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.19%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `109` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `108` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+15.7s` (`+0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-31.5s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 65 | 59.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 36 | 33.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 7 | 6.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 0.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 18** | 5 | 4 | 1 | **`20.0%`** | `50.0%` | `+1.1 min` |
| **Route 10** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `-53.3s` |
| **Route 11** | 4 | 4 | 0 | **`0.0%`** | `75.0%` | `+1.8 min` |
| **Route 14** | 4 | 4 | 0 | **`0.0%`** | `25.0%` | `-115.5s` |
| **Route 17** | 5 | 4 | 0 | **`0.0%`** | `60.0%` | `-23.2s` |
| **Route 2** | 3 | 3 | 0 | **`0.0%`** | `33.33%` | `-111.0s` |
| **Route 22** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `-31.5s` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `-74.4s` |
| **Route 323** | 3 | 2 | 0 | **`0.0%`** | `66.67%` | `+5.4 min` |
| **Route 36** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 54** | `+7.1 min (+426.0s)` | `+13.2 min (+795s)` | 2 | `50.0%` |
| **Route 323** | `+5.4 min (+325.7s)` | `+13.5 min (+811s)` | 2 | `66.67%` |
| **Route 904** | `+3.5 min (+207.0s)` | `+10.1 min (+604s)` | 2 | `0.0%` |
| **Route 9** | `+2.8 min (+165.5s)` | `+3.0 min (+182s)` | 2 | `100.0%` |
| **Route 921** | `+2.1 min (+128.2s)` | `+4.8 min (+290s)` | 3 | `100.0%` |
| **Route 901** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 922** | `+1.8 min (+110.5s)` | `+10.1 min (+606s)` | 5 | `66.67%` |
| **Route 11** | `+1.8 min (+110.0s)` | `+6.3 min (+378s)` | 4 | `75.0%` |
| **Route 71** | `+1.8 min (+108.0s)` | `+1.8 min (+108s)` | 1 | `100.0%` |
| **Route 923** | `+1.8 min (+106.2s)` | `+5.5 min (+330s)` | 3 | `60.0%` |

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
| `920257` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 06:30:18` | `0.92%` | `60.19%` | 109 | 108 | `+15.7s` |
| `2026-11-18 05:00:18` | `5.09%` | `58.62%` | 275 | 261 | `+13.3s` |
| `2026-11-18 04:30:18` | `5.88%` | `60.62%` | 340 | 320 | `+34.8s` |
| `2026-11-18 04:00:17` | `6.94%` | `56.79%` | 389 | 361 | `+32.4s` |
| `2026-11-18 03:30:18` | `7.8%` | `58.85%` | 436 | 401 | `+5.4s` |
| `2026-11-18 03:00:18` | `8.18%` | `63.93%` | 477 | 438 | `+23.9s` |
| `2026-11-18 02:00:18` | `7.87%` | `66.28%` | 559 | 513 | `+15.3s` |
| `2026-11-18 01:30:18` | `7.72%` | `63.98%` | 609 | 559 | `+18.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T06:30:18.476000+00:00`.*
