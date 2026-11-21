# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.655000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`90.65%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`87.5%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `353` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `159` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `320` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+655.6s` (`+10.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+123.5s` (`+2.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 14 | 4.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 320 | 90.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 15** | 77 | 1 | 77 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 11** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 15 | 0 | 15 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 14** | 92 | 2 | 90 | **`97.83%`** | `100.0%` | `+1.6 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `-18.0s` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 66** | `+74.7 min (+4484.5s)` | `+104.7 min (+6283s)` | 2 | `0.0%` |
| **Route 10** | `+3.1 min (+184.0s)` | `+4.9 min (+292s)` | 2 | `100.0%` |
| **Route 28** | `+2.2 min (+134.0s)` | `+2.2 min (+134s)` | 1 | `100.0%` |
| **Route 1** | `+2.2 min (+134.0s)` | `+4.2 min (+254s)` | 1 | `100.0%` |
| **Route 6** | `+2.2 min (+131.0s)` | `+2.3 min (+140s)` | 3 | `100.0%` |
| **Route 14** | `+1.6 min (+99.0s)` | `+1.6 min (+99s)` | 2 | `100.0%` |
| **Route 41** | `+1.5 min (+90.3s)` | `+2.2 min (+132s)` | 3 | `100.0%` |
| **Route 19** | `+1.2 min (+74.0s)` | `+1.2 min (+74s)` | 1 | `100.0%` |
| **Route 51** | `+1.1 min (+63.0s)` | `+1.1 min (+63s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 66** | ~60.0m | ~60.0m | **`+0.1 min`** | `50.0 / 100` |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `53.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19234615` | Route 14 | `07:43:00` | `SCHEDULED` | Assigned vehicle 4113 is broadcasting off-schedule with no vehicle covering 19234615 |
| `19233600` | Route 15 | `07:45:00` | `SCHEDULED` | Assigned vehicle 4194 is broadcasting off-schedule with no vehicle covering 19233600 |
| `19234727` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19234728` | Route 14 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235445` | Route 8 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235449` | Route 8 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235453` | Route 8 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235457` | Route 8 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235461` | Route 8 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235465` | Route 8 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235469` | Route 8 | `19:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235443` | Route 8 | `06:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235447` | Route 8 | `08:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235451` | Route 8 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235455` | Route 8 | `12:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `90.65%` | `87.5%` | 353 | 159 | `+655.6s` |
| `2026-11-21 06:30:23` | `86.41%` | `70.0%` | 368 | 166 | `+328.7s` |
| `2026-11-21 06:00:18` | `83.55%` | `70.0%` | 389 | 170 | `+280.2s` |
| `2026-11-21 05:30:18` | `77.8%` | `72.41%` | 419 | 189 | `+179.4s` |
| `2026-11-21 05:00:19` | `9.92%` | `78.85%` | 131 | 207 | `+191.0s` |
| `2026-11-21 04:30:18` | `8.92%` | `82.43%` | 157 | 219 | `+184.3s` |
| `2026-11-21 04:00:18` | `11.4%` | `64.77%` | 193 | 241 | `+253.8s` |
| `2026-11-21 03:30:18` | `13.11%` | `76.4%` | 206 | 219 | `+182.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.655000+00:00`.*
