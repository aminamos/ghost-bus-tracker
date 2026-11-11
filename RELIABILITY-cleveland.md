# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-11T07:00:22.757000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`93.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`91.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `522` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `206` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `487` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+116.3s` (`+1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+66.0s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 11 | 2.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 487 | 93.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `0.0%` | `+10.2 min` |
| **Route 14** | 148 | 1 | 145 | **`97.97%`** | `100.0%` | `+3.6 min` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.1 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `-48.0s` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 15** | `+10.2 min (+614.0s)` | `+10.2 min (+614s)` | 1 | `0.0%` |
| **Route 14** | `+3.6 min (+218.0s)` | `+3.6 min (+218s)` | 1 | `100.0%` |
| **Route 10** | `+1.9 min (+113.5s)` | `+4.6 min (+278s)` | 2 | `100.0%` |
| **Route 6** | `+1.8 min (+105.0s)` | `+2.1 min (+128s)` | 3 | `100.0%` |
| **Route 19** | `+1.1 min (+68.0s)` | `+1.1 min (+68s)` | 2 | `100.0%` |
| **Route 41** | `+0.6 min (+35.0s)` | `+1.1 min (+64s)` | 2 | `100.0%` |
| **Route 51** | `+0.5 min (+27.0s)` | `+0.5 min (+27s)` | 1 | `100.0%` |
| **Route 28** | `+0.2 min (+10.0s)` | `+0.2 min (+10s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `75.8 / 100` |

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
| `2026-11-11 07:00:22` | `93.3%` | `91.67%` | 522 | 206 | `+116.3s` |
| `2026-11-11 06:30:18` | `91.39%` | `88.0%` | 534 | 212 | `+107.4s` |
| `2026-11-11 06:00:22` | `88.29%` | `83.33%` | 555 | 209 | `+162.8s` |
| `2026-11-11 05:30:19` | `82.03%` | `80.0%` | 590 | 220 | `+1298.5s` |
| `2026-11-11 05:00:19` | `8.33%` | `80.7%` | 132 | 232 | `+1376.7s` |
| `2026-11-11 04:30:18` | `8.28%` | `82.67%` | 157 | 230 | `+969.7s` |
| `2026-11-11 04:00:18` | `10.88%` | `71.43%` | 193 | 228 | `+1032.4s` |
| `2026-11-11 03:30:22` | `11.98%` | `74.73%` | 217 | 209 | `+806.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-11T07:00:22.757000+00:00`.*
