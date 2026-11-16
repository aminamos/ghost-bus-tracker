# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-16T07:00:20.949000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.44%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `365` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `12` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `352` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-236.0s` (`-3.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-236.0s` (`-3.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 352 | 96.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 74 | 1 | 72 | **`97.3%`** | `0.0%` | `+0.0s` |
| **Route 1** | 88 | 3 | 85 | **`96.59%`** | `0.0%` | `-236.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `30799543` | Route 17 | `24:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799620` | Route 17 | `25:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799677` | Route 17 | `04:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799704` | Route 17 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799706` | Route 17 | `03:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799829` | Route 17 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799738` | Route 17 | `15:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799826` | Route 17 | `11:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799827` | Route 17 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799824` | Route 17 | `14:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799828` | Route 17 | `15:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799740` | Route 17 | `14:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799736` | Route 17 | `16:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799732` | Route 17 | `17:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30799729` | Route 17 | `19:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:20` | `96.44%` | `0.0%` | 365 | 12 | `-236.0s` |
| `2026-11-16 06:30:33` | `94.89%` | `100.0%` | 372 | 18 | `+89.5s` |
| `2026-11-16 06:00:19` | `92.45%` | `66.67%` | 384 | 29 | `+29.7s` |
| `2026-11-16 05:30:20` | `6.82%` | `25.0%` | 44 | 41 | `-124.0s` |
| `2026-11-16 05:00:21` | `8.2%` | `25.0%` | 61 | 56 | `-57.2s` |
| `2026-11-16 04:30:19` | `9.33%` | `28.57%` | 75 | 67 | `+146.3s` |
| `2026-11-16 03:30:18` | `12.15%` | `50.0%` | 107 | 92 | `-88.4s` |
| `2026-11-16 03:00:33` | `13.93%` | `44.44%` | 122 | 104 | `-65.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:20.949000+00:00`.*
