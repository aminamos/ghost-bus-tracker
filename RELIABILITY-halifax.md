# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-24T07:00:19.158000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `358` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `358` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 358 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 107 | 0 | 107 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10C** | 46 | 0 | 46 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10B** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 72** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 135** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4650041` | Route 10C | `14:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649422` | Route 1 | `24:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649416` | Route 1 | `22:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649408` | Route 1 | `21:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649399` | Route 1 | `19:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649390` | Route 1 | `18:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649378` | Route 1 | `16:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649367` | Route 1 | `14:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649357` | Route 1 | `12:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658309` | Route 72 | `20:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658307` | Route 72 | `18:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658303` | Route 72 | `17:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658299` | Route 72 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4658294` | Route 72 | `12:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649406` | Route 1 | `20:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:19` | `100.0%` | `0.0%` | 358 | 0 | `+0.0s` |
| `2026-11-24 06:30:21` | `100.0%` | `0.0%` | 358 | 0 | `+0.0s` |
| `2026-11-24 06:00:18` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-11-24 05:30:18` | `20.0%` | `75.0%` | 5 | 4 | `+5.5s` |
| `2026-11-24 05:00:19` | `10.0%` | `63.64%` | 30 | 22 | `-12.6s` |
| `2026-11-24 04:30:19` | `7.81%` | `80.0%` | 64 | 43 | `-22.5s` |
| `2026-11-24 04:00:19` | `8.82%` | `88.51%` | 102 | 58 | `+6.2s` |
| `2026-11-24 03:30:23` | `9.63%` | `87.29%` | 135 | 69 | `+10.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:19.158000+00:00`.*
