# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-10T07:00:18.515000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.94%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`86.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `524` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `182` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `487` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+104.5s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+62.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 13 | 2.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 487 | 92.9% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 79 | 0 | 79 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 50 | 0 | 50 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 16 | 0 | 16 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 130 | 1 | 128 | **`98.46%`** | `100.0%` | `+0.1 min` |
| **Route 14** | 148 | 1 | 145 | **`97.97%`** | `100.0%` | `+1.5 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+2.2 min` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.2 min` |
| **Route 41** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 26** | `+6.7 min (+401.0s)` | `+9.2 min (+551s)` | 2 | `50.0%` |
| **Route 19** | `+4.2 min (+254.0s)` | `+4.2 min (+254s)` | 2 | `100.0%` |
| **Route 28** | `+2.2 min (+132.0s)` | `+2.2 min (+132s)` | 1 | `100.0%` |
| **Route 14** | `+1.5 min (+88.0s)` | `+1.5 min (+88s)` | 1 | `100.0%` |
| **Route 41** | `+1.2 min (+74.0s)` | `+2.2 min (+132s)` | 3 | `100.0%` |
| **Route 6** | `+0.9 min (+54.0s)` | `+1.0 min (+60s)` | 3 | `100.0%` |
| **Route 51** | `+0.2 min (+12.0s)` | `+0.2 min (+12s)` | 1 | `100.0%` |
| **Route 15** | `+0.1 min (+3.0s)` | `+0.1 min (+3s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | ~2.0m | ~2.0m | **`+0.0 min`** | `56.7 / 100` |

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
| `2026-11-10 07:00:18` | `92.94%` | `86.67%` | 524 | 182 | `+104.5s` |
| `2026-11-10 06:30:18` | `91.04%` | `83.33%` | 536 | 190 | `+95.7s` |
| `2026-11-10 06:00:17` | `89.13%` | `79.17%` | 552 | 186 | `+152.0s` |
| `2026-11-10 05:30:20` | `82.99%` | `80.0%` | 588 | 194 | `+114.9s` |
| `2026-11-10 05:00:18` | `9.45%` | `82.35%` | 127 | 212 | `+160.5s` |
| `2026-11-10 04:30:19` | `10.32%` | `86.57%` | 155 | 214 | `+138.1s` |
| `2026-11-10 04:00:18` | `10.66%` | `77.22%` | 197 | 230 | `+233.7s` |
| `2026-11-10 03:30:18` | `12.04%` | `80.85%` | 216 | 212 | `+148.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:18.515000+00:00`.*
