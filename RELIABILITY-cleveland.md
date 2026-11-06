# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-06T07:00:18.164000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.75%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `524` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `206` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `486` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+137.8s` (`+2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+86.5s` (`+1.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 11 | 2.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 2 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 0.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 486 | 92.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `100.0%` | `+2.0 min` |
| **Route 14** | 149 | 2 | 144 | **`96.64%`** | `50.0%` | `+5.5 min` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+5.8 min` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `66.67%` | `+2.8 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 19** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `-62.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 48** | `+5.8 min (+350.0s)` | `+5.8 min (+350s)` | 2 | `0.0%` |
| **Route 14** | `+5.5 min (+330.5s)` | `+7.6 min (+458s)` | 2 | `50.0%` |
| **Route 10** | `+2.8 min (+169.3s)` | `+7.2 min (+429s)` | 2 | `66.67%` |
| **Route 28** | `+2.5 min (+147.0s)` | `+4.2 min (+252s)` | 1 | `100.0%` |
| **Route 15** | `+2.0 min (+123.0s)` | `+2.0 min (+123s)` | 1 | `100.0%` |
| **Route 6** | `+2.0 min (+119.0s)` | `+4.2 min (+250s)` | 3 | `100.0%` |
| **Route 1** | `+1.7 min (+103.0s)` | `+1.7 min (+103s)` | 1 | `100.0%` |
| **Route 41** | `+0.4 min (+26.5s)` | `+0.5 min (+27s)` | 2 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 14** | ~19.0m | ~19.0m | **`+0.0 min`** | `88.8 / 100` |
| **Route 10** | ~60.0m | ~60.0m | **`+0.0 min`** | `99.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19234727` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19234728` | Route 14 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233420` | Route 8 | `06:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233424` | Route 8 | `08:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233428` | Route 8 | `10:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233432` | Route 8 | `12:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233436` | Route 8 | `14:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233440` | Route 8 | `16:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233444` | Route 8 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233448` | Route 8 | `20:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233418` | Route 8 | `05:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233422` | Route 8 | `07:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233426` | Route 8 | `09:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233430` | Route 8 | `11:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19233434` | Route 8 | `13:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-06 07:00:18` | `92.75%` | `68.75%` | 524 | 206 | `+137.8s` |
| `2026-11-06 06:30:19` | `90.35%` | `86.67%` | 539 | 216 | `+193.9s` |
| `2026-11-06 06:00:18` | `87.48%` | `72.41%` | 559 | 212 | `+248.9s` |
| `2026-11-06 05:30:19` | `82.0%` | `83.05%` | 589 | 222 | `+1278.9s` |
| `2026-11-06 05:00:18` | `8.27%` | `81.03%` | 133 | 225 | `+166.0s` |
| `2026-11-06 04:30:19` | `8.92%` | `80.82%` | 157 | 230 | `+172.3s` |
| `2026-11-06 04:00:22` | `11.29%` | `73.68%` | 186 | 230 | `+277.2s` |
| `2026-11-06 03:30:20` | `11.96%` | `75.82%` | 209 | 205 | `+202.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-06T07:00:18.164000+00:00`.*
