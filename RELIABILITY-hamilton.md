# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:18.233000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.48%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `177` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `8` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `169` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+166.0s` (`+2.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+166.0s` (`+2.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 169 | 95.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5795** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 73 | 1 | 72 | **`98.63%`** | `100.0%` | `+2.8 min` |
| **Route 5783** | 60 | 1 | 59 | **`98.33%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | `+2.8 min (+166.0s)` | `+2.8 min (+166s)` | 1 | `100.0%` |

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
| `2197823` | Route 5807 | `24:46:00` | `SCHEDULED` | Assigned vehicle 11517 is missing from active GPS transponder fleet |
| `2194132` | Route 5795 | `13:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194144` | Route 5795 | `17:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194118` | Route 5795 | `19:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194146` | Route 5795 | `20:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194149` | Route 5795 | `22:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194152` | Route 5795 | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194129` | Route 5795 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194122` | Route 5795 | `09:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194125` | Route 5795 | `10:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194133` | Route 5795 | `12:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194131` | Route 5795 | `11:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194136` | Route 5795 | `14:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194139` | Route 5795 | `16:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194134` | Route 5795 | `13:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:18` | `95.48%` | `100.0%` | 177 | 8 | `+166.0s` |
| `2026-11-08 06:30:20` | `82.04%` | `100.0%` | 206 | 38 | `+15.7s` |
| `2026-11-08 06:00:18` | `71.43%` | `100.0%` | 238 | 68 | `+61.8s` |
| `2026-11-08 05:30:20` | `67.06%` | `92.86%` | 255 | 81 | `+64.9s` |
| `2026-11-08 05:00:18` | `8.51%` | `93.33%` | 94 | 87 | `+27.4s` |
| `2026-11-08 04:30:25` | `11.43%` | `92.5%` | 105 | 93 | `+22.4s` |
| `2026-11-08 04:00:20` | `12.84%` | `95.79%` | 109 | 93 | `+51.2s` |
| `2026-11-08 03:30:18` | `17.39%` | `0.0%` | 115 | 94 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.233000+00:00`.*
