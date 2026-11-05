# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-05T07:00:17.987000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.21%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `526` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `194` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `485` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+193.0s` (`+3.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+87.5s` (`+1.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 12 | 2.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 0.8% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 485 | 92.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `100.0%` | `+0.7 min` |
| **Route 14** | 148 | 2 | 143 | **`96.62%`** | `0.0%` | `+5.0 min` |
| **Route 10** | 5 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 19** | 3 | 2 | 0 | **`0.0%`** | `50.0%` | `+3.1 min` |
| **Route 3** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.0 min` |
| **Route 41** | 3 | 4 | 0 | **`0.0%`** | `66.67%` | `+2.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 48** | `+14.5 min (+871.0s)` | `+22.9 min (+1372s)` | 2 | `0.0%` |
| **Route 14** | `+5.0 min (+303.0s)` | `+5.0 min (+303s)` | 2 | `0.0%` |
| **Route 19** | `+3.1 min (+184.0s)` | `+5.3 min (+319s)` | 2 | `50.0%` |
| **Route 41** | `+2.8 min (+169.7s)` | `+6.1 min (+366s)` | 4 | `66.67%` |
| **Route 6** | `+2.8 min (+167.7s)` | `+4.2 min (+249s)` | 3 | `100.0%` |
| **Route 1** | `+1.7 min (+100.0s)` | `+1.7 min (+100s)` | 1 | `100.0%` |
| **Route 3** | `+1.0 min (+62.0s)` | `+1.0 min (+62s)` | 1 | `100.0%` |
| **Route 15** | `+0.7 min (+42.0s)` | `+0.7 min (+42s)` | 1 | `100.0%` |
| **Route 10** | `+0.3 min (+16.0s)` | `+1.1 min (+69s)` | 3 | `100.0%` |
| **Route 28** | `+0.0 min (+2.0s)` | `+0.0 min (+2s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `0.0 / 100` |
| **Route 6** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
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
| `19233438` | Route 8 | `15:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-05 07:00:17` | `92.21%` | `66.67%` | 526 | 194 | `+193.0s` |
| `2026-11-05 06:30:18` | `90.52%` | `78.57%` | 538 | 185 | `+240.6s` |
| `2026-11-05 06:00:18` | `87.66%` | `67.86%` | 559 | 196 | `+2957.8s` |
| `2026-11-05 05:30:19` | `82.79%` | `76.79%` | 587 | 205 | `+132.1s` |
| `2026-11-05 05:00:18` | `2.46%` | `77.59%` | 122 | 228 | `+235.2s` |
| `2026-11-05 04:30:18` | `2.19%` | `73.61%` | 137 | 226 | `+165.9s` |
| `2026-11-05 04:00:19` | `0.59%` | `74.68%` | 170 | 233 | `+185.9s` |
| `2026-11-05 03:30:19` | `0.0%` | `78.72%` | 190 | 207 | `+160.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-05T07:00:17.987000+00:00`.*
