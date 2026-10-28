# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:18.595000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`15.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`78.18%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `73` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `40` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `11` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+194.8s` (`+3.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+62.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 43 | 58.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 8.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 4.1% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 4.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 15.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 009** | 11 | 4 | 4 | **`36.36%`** | `66.67%` | `+0.5 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.3 min` |
| **Route 002** | 15 | 9 | 3 | **`20.0%`** | `77.78%` | `+3.7 min` |
| **Route 008** | 11 | 6 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 721** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 056** | 2 | 3 | 0 | **`0.0%`** | `50.0%` | `-115.0s` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `80.0%` | `+0.2 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.1 min` |
| **Route 511** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+21.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 509A** | `+53.6 min (+3215.0s)` | `+53.6 min (+3215s)` | 1 | `0.0%` |
| **Route 511** | `+21.2 min (+1269.5s)` | `+38.9 min (+2334s)` | 2 | `50.0%` |
| **Route 007** | `+10.9 min (+654.0s)` | `+10.9 min (+654s)` | 1 | `0.0%` |
| **Route 715** | `+8.3 min (+498.0s)` | `+8.3 min (+498s)` | 1 | `0.0%` |
| **Route 055** | `+5.0 min (+298.0s)` | `+5.0 min (+298s)` | 1 | `100.0%` |
| **Route 002** | `+3.7 min (+224.7s)` | `+16.4 min (+986s)` | 9 | `77.78%` |
| **Route 721** | `+2.0 min (+120.0s)` | `+3.7 min (+223s)` | 2 | `100.0%` |
| **Route 004** | `+1.3 min (+79.8s)` | `+2.8 min (+168s)` | 7 | `100.0%` |
| **Route 008** | `+1.2 min (+70.2s)` | `+4.7 min (+284s)` | 6 | `100.0%` |
| **Route 918A** | `+0.7 min (+44.0s)` | `+0.7 min (+44s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `81.3 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.2 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `91.1 / 100` |
| **Route 721** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.7 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.5 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `95.5 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.4 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.6 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `33907387` | Route 914 | `23:00:00` | `SCHEDULED` | Assigned vehicle 3437 is broadcasting off-schedule with no vehicle covering 33907387 |
| `32760711` | Route 009 | `25:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760712` | Route 009 | `25:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760713` | Route 009 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760714` | Route 009 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:18` | `15.07%` | `78.18%` | 73 | 40 | `+194.8s` |
| `2026-10-28 06:30:22` | `14.29%` | `78.49%` | 126 | 73 | `+34.7s` |
| `2026-10-28 06:00:24` | `13.66%` | `89.1%` | 205 | 111 | `+60.0s` |
| `2026-10-28 05:30:30` | `16.98%` | `87.5%` | 265 | 122 | `+59.9s` |
| `2026-10-28 05:00:30` | `18.67%` | `92.37%` | 316 | 134 | `+91.0s` |
| `2026-10-28 03:30:19` | `17.48%` | `83.78%` | 572 | 265 | `+87.0s` |
| `2026-10-28 03:00:27` | `20.4%` | `78.98%` | 652 | 266 | `+80.5s` |
| `2026-10-28 02:30:19` | `23.76%` | `77.28%` | 707 | 279 | `+156.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:18.595000+00:00`.*
