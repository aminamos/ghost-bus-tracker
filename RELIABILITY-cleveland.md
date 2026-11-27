# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-27T07:00:19.472000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`93.76%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`76.92%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `497` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `128` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `466` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+61.7s` (`+1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+67.0s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 10 | 2.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 466 | 93.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 1 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 15** | 130 | 1 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 40 | 0 | 40 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 146 | 0 | 145 | **`99.32%`** | `0.0%` | `+0.0s` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.2 min` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+2.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 22** | `+2.9 min (+173.0s)` | `+5.4 min (+323s)` | 2 | `50.0%` |
| **Route 1** | `+2.5 min (+151.0s)` | `+2.5 min (+151s)` | 1 | `100.0%` |
| **Route 41** | `+2.2 min (+134.0s)` | `+2.2 min (+134s)` | 2 | `100.0%` |
| **Route 19** | `+1.2 min (+73.0s)` | `+1.2 min (+73s)` | 2 | `100.0%` |
| **Route 3** | `+1.1 min (+67.0s)` | `+1.1 min (+67s)` | 1 | `100.0%` |
| **Route 6** | `+0.7 min (+42.3s)` | `+2.2 min (+132s)` | 3 | `100.0%` |
| **Route 10** | `+0.2 min (+15.0s)` | `+0.2 min (+15s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 6** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19370483` | Route 15 | `07:45:00` | `SCHEDULED` | Assigned vehicle 4044 is broadcasting off-schedule with no vehicle covering 19370483 |
| `19370470` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233417` | Route 8 | `05:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233420` | Route 8 | `06:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233421` | Route 8 | `07:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233424` | Route 8 | `08:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233425` | Route 8 | `09:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233428` | Route 8 | `10:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233429` | Route 8 | `11:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233432` | Route 8 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233433` | Route 8 | `13:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233436` | Route 8 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233437` | Route 8 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233440` | Route 8 | `16:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233441` | Route 8 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-27 07:00:19` | `93.76%` | `76.92%` | 497 | 128 | `+61.7s` |
| `2026-11-27 06:30:19` | `91.54%` | `71.43%` | 508 | 136 | `+128.6s` |
| `2026-11-27 06:00:18` | `88.78%` | `85.71%` | 526 | 146 | `+116.3s` |
| `2026-11-27 05:30:19` | `85.43%` | `88.37%` | 549 | 151 | `+121.6s` |
| `2026-11-27 05:00:17` | `5.08%` | `83.72%` | 118 | 172 | `+142.1s` |
| `2026-11-27 04:30:19` | `6.34%` | `87.5%` | 142 | 169 | `+112.7s` |
| `2026-11-27 04:00:17` | `7.06%` | `79.25%` | 170 | 196 | `+149.3s` |
| `2026-11-27 03:30:19` | `7.69%` | `79.69%` | 182 | 169 | `+161.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-27T07:00:19.472000+00:00`.*
