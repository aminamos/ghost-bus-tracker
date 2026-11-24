# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-24T07:00:18.753000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.59%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.42%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `526` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `206` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `487` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+2070.5s` (`+34.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+115.0s` (`+1.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 13 | 2.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 0.8% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 487 | 92.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `100.0%` | `+1.9 min` |
| **Route 14** | 150 | 2 | 144 | **`96.0%`** | `33.33%` | `+206.0 min` |
| **Route 6** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+0.7 min` |
| **Route 48** | 4 | 2 | 0 | **`0.0%`** | `66.67%` | `+4.7 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.8 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 14** | `+206.0 min (+12359.0s)` | `+607.1 min (+36426s)` | 2 | `33.33%` |
| **Route 48** | `+4.7 min (+280.7s)` | `+10.3 min (+617s)` | 2 | `66.67%` |
| **Route 51** | `+4.4 min (+263.0s)` | `+6.1 min (+368s)` | 1 | `50.0%` |
| **Route 10** | `+4.2 min (+251.0s)` | `+6.2 min (+370s)` | 3 | `50.0%` |
| **Route 26** | `+2.0 min (+122.0s)` | `+2.0 min (+122s)` | 2 | `100.0%` |
| **Route 15** | `+1.9 min (+115.0s)` | `+1.9 min (+115s)` | 1 | `100.0%` |
| **Route 19** | `+1.1 min (+69.0s)` | `+1.1 min (+69s)` | 1 | `100.0%` |
| **Route 41** | `+0.8 min (+46.7s)` | `+1.8 min (+108s)` | 3 | `100.0%` |
| **Route 6** | `+0.7 min (+44.0s)` | `+0.7 min (+44s)` | 3 | `100.0%` |
| **Route 28** | `+0.2 min (+11.0s)` | `+0.2 min (+11s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 14** | ~19.0m | ~19.0m | **`+40.2 min`** | `0.0 / 100` |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `63.7 / 100` |
| **Route 48** | ~60.0m | ~60.0m | **`+0.0 min`** | `98.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19233729` | Route 6 | `06:25:00` | `SCHEDULED` | Assigned vehicle 4127 is broadcasting off-schedule with no vehicle covering 19233729 |
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

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:18` | `92.59%` | `68.42%` | 526 | 206 | `+2070.5s` |
| `2026-11-24 06:30:20` | `90.35%` | `75.86%` | 539 | 224 | `+1305.7s` |
| `2026-11-24 06:00:18` | `88.15%` | `81.48%` | 557 | 210 | `+1333.8s` |
| `2026-11-24 05:30:18` | `81.56%` | `81.97%` | 591 | 221 | `+628.1s` |
| `2026-11-24 05:00:19` | `7.81%` | `83.64%` | 128 | 242 | `+1166.7s` |
| `2026-11-24 04:30:19` | `7.59%` | `83.33%` | 158 | 241 | `+513.6s` |
| `2026-11-24 04:00:19` | `10.94%` | `80.0%` | 192 | 240 | `+489.7s` |
| `2026-11-24 03:30:21` | `12.21%` | `78.02%` | 213 | 225 | `+374.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:18.753000+00:00`.*
