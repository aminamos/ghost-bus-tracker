# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.703000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.88%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`85.11%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `77` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `39` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `13` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+112.8s` (`+1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+70.0s` (`+1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 40 | 51.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 5.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 2.6% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 16.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 721** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+0.3 min` |
| **Route 511** | 7 | 2 | 3 | **`42.86%`** | `0.0%` | `-480.0s` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `66.67%` | `+0.2 min` |
| **Route 002** | 15 | 9 | 3 | **`20.0%`** | `83.33%` | `+4.6 min` |
| **Route 004** | 15 | 8 | 3 | **`20.0%`** | `88.89%` | `+3.7 min` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+1.7 min` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-33.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 002** | `+4.6 min (+275.0s)` | `+16.5 min (+988s)` | 9 | `83.33%` |
| **Route 523** | `+4.4 min (+265.0s)` | `+4.4 min (+265s)` | 1 | `100.0%` |
| **Route 004** | `+3.7 min (+224.3s)` | `+14.4 min (+867s)` | 8 | `88.89%` |
| **Route 052** | `+3.7 min (+224.0s)` | `+3.7 min (+224s)` | 1 | `100.0%` |
| **Route 909** | `+3.5 min (+210.0s)` | `+3.5 min (+210s)` | 1 | `100.0%` |
| **Route 507** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |
| **Route 005** | `+1.7 min (+104.2s)` | `+9.1 min (+547s)` | 5 | `60.0%` |
| **Route 901** | `+1.5 min (+91.5s)` | `+3.5 min (+209s)` | 2 | `100.0%` |
| **Route 903** | `+1.2 min (+73.0s)` | `+1.3 min (+76s)` | 2 | `100.0%` |
| **Route 008** | `+0.9 min (+53.0s)` | `+3.8 min (+226s)` | 6 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `71.4 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `79.0 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `80.7 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.5 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.3 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.8 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `95.2 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.1 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32763447` | Route 721 | `24:37:00` | `SCHEDULED` | Assigned vehicle 2845 is missing from active GPS transponder fleet |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760607` | Route 009 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760606` | Route 009 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760608` | Route 009 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756142` | Route 511 | `26:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756140` | Route 511 | `25:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32756141` | Route 511 | `26:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `16.88%` | `85.11%` | 77 | 39 | `+112.8s` |
| `2026-11-21 06:30:31` | `14.17%` | `82.98%` | 127 | 78 | `+135.6s` |
| `2026-11-21 06:00:18` | `12.12%` | `86.71%` | 198 | 115 | `+106.9s` |
| `2026-11-21 05:30:18` | `12.35%` | `79.44%` | 251 | 123 | `+171.5s` |
| `2026-11-21 05:00:24` | `14.19%` | `83.81%` | 296 | 139 | `+129.6s` |
| `2026-11-21 04:30:20` | `16.36%` | `77.74%` | 330 | 156 | `+152.2s` |
| `2026-11-21 04:00:18` | `15.35%` | `81.13%` | 443 | 234 | `+134.7s` |
| `2026-11-21 03:30:19` | `15.99%` | `79.86%` | 544 | 264 | `+108.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.703000+00:00`.*
