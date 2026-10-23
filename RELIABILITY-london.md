# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **London Transit Commission** in **London, ON** (City of London, Ontario).
> **Transit System:** LTC | **Location:** London, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-23T07:01:26.862000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2251` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2251` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+0.0s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2251 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 13** | 139 | 0 | 139 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 36** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 16** | 128 | 0 | 128 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 128 | 0 | 128 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 04** | 125 | 0 | 125 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 02** | 115 | 0 | 115 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 108 | 0 | 108 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 25** | 106 | 0 | 106 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| *All active tracked routes currently operating within nominal bounds* | - | - | - | - |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| *Insufficient route frequency data in current snapshot* | - | - | - | - |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2385319` | Route 01 | `06:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385327` | Route 01 | `08:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385340` | Route 01 | `10:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385336` | Route 01 | `11:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385345` | Route 01 | `13:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385350` | Route 01 | `15:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385361` | Route 01 | `16:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385364` | Route 01 | `18:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385366` | Route 01 | `20:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385317` | Route 01 | `06:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385321` | Route 01 | `07:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385339` | Route 01 | `09:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385335` | Route 01 | `11:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385344` | Route 01 | `12:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385352` | Route 01 | `14:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:26` | `100.0%` | `0.0%` | 2251 | 0 | `+0.0s` |
| `2026-10-23 06:30:26` | `100.0%` | `0.0%` | 1 | 1 | `+0.0s` |
| `2026-10-23 06:00:22` | `20.0%` | `100.0%` | 5 | 5 | `+25.2s` |
| `2026-10-23 05:30:23` | `8.33%` | `72.73%` | 12 | 10 | `+43.9s` |
| `2026-10-23 05:15:29` | `9.09%` | `88.89%` | 33 | 23 | `+27.3s` |
| `2026-10-23 05:00:43` | `8.7%` | `92.31%` | 46 | 30 | `+37.0s` |
| `2026-10-23 04:30:38` | `18.89%` | `86.36%` | 90 | 42 | `-19.3s` |
| `2026-10-23 04:00:42` | `27.46%` | `83.67%` | 142 | 59 | `+34.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:26.862000+00:00`.*
