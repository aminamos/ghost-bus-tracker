# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-29T07:00:18.860000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`12.5%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`89.36%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `72` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `39` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `9` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+49.6s` (`+0.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+47.0s` (`+0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 42 | 58.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 5.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 1.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 9 | 12.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `62.5%` | `+0.8 min` |
| **Route 002** | 14 | 8 | 3 | **`21.43%`** | `100.0%` | `+1.7 min` |
| **Route 004** | 14 | 7 | 3 | **`21.43%`** | `100.0%` | `+1.8 min` |
| **Route 008** | 10 | 6 | 0 | **`0.0%`** | `87.5%` | `-33.0s` |
| **Route 721** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 511** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 005** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 056** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0 min` |
| **Route 901** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.0 min` |
| **Route 903** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 901** | `+3.0 min (+183.0s)` | `+5.0 min (+298s)` | 2 | `100.0%` |
| **Route 523** | `+2.6 min (+158.0s)` | `+2.6 min (+158s)` | 1 | `100.0%` |
| **Route 004** | `+1.8 min (+106.1s)` | `+4.3 min (+257s)` | 7 | `100.0%` |
| **Route 002** | `+1.7 min (+104.2s)` | `+3.4 min (+204s)` | 8 | `100.0%` |
| **Route 918A** | `+1.5 min (+88.0s)` | `+1.5 min (+88s)` | 1 | `100.0%` |
| **Route 009** | `+0.8 min (+48.0s)` | `+8.5 min (+508s)` | 4 | `62.5%` |
| **Route 005** | `+0.5 min (+30.8s)` | `+0.8 min (+51s)` | 5 | `100.0%` |
| **Route 721** | `+0.4 min (+23.5s)` | `+1.1 min (+64s)` | 2 | `100.0%` |
| **Route 903** | `+0.4 min (+23.0s)` | `+1.1 min (+66s)` | 2 | `100.0%` |
| **Route 056** | `+0.0 min (+0.5s)` | `+0.1 min (+5s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `83.4 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `89.2 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `93.6 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.6 / 100` |
| **Route 009** | ~29.0m | ~29.0m | **`+0.0 min`** | `96.2 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.0 / 100` |
| **Route 721** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.8 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 005** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.4 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32904645` | Route 004 | `26:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904644` | Route 004 | `25:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32904646` | Route 004 | `26:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760330` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760331` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760714` | Route 009 | `26:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760713` | Route 009 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760712` | Route 009 | `25:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32760332` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:18` | `12.5%` | `89.36%` | 72 | 39 | `+49.6s` |
| `2026-10-29 06:30:24` | `12.9%` | `85.11%` | 124 | 76 | `+105.0s` |
| `2026-10-29 06:00:24` | `12.24%` | `83.33%` | 196 | 110 | `+153.2s` |
| `2026-10-29 05:30:20` | `14.94%` | `79.05%` | 261 | 123 | `+158.8s` |
| `2026-10-29 05:00:23` | `17.26%` | `77.14%` | 307 | 133 | `+183.4s` |
| `2026-10-29 04:30:23` | `20.4%` | `75.57%` | 353 | 153 | `+206.2s` |
| `2026-10-29 04:00:21` | `18.98%` | `75.0%` | 469 | 234 | `+200.6s` |
| `2026-10-29 03:30:18` | `21.27%` | `72.5%` | 583 | 261 | `+219.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:18.860000+00:00`.*
