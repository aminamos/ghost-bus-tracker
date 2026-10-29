# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-29T07:00:19.168000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `259` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `2` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `259` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 259 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 108 | 0 | 108 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5803** | 15 | 0 | 15 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2201350` | Route 5803 | `17:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201288` | Route 5803 | `18:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201355` | Route 5803 | `19:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201292` | Route 5803 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201359` | Route 5803 | `20:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201296` | Route 5803 | `21:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201363` | Route 5803 | `22:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201298` | Route 5803 | `22:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201365` | Route 5803 | `23:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201300` | Route 5803 | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201367` | Route 5803 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201302` | Route 5803 | `24:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201369` | Route 5803 | `24:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2201286` | Route 5803 | `18:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200271` | Route 5795 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-29 07:00:19` | `100.0%` | `0.0%` | 259 | 2 | `+0.0s` |
| `2026-10-29 06:30:24` | `99.23%` | `0.0%` | 261 | 2 | `+0.0s` |
| `2026-10-29 06:00:24` | `96.63%` | `100.0%` | 267 | 11 | `+36.0s` |
| `2026-10-29 05:30:19` | `84.04%` | `100.0%` | 307 | 48 | `+2.5s` |
| `2026-10-29 05:00:20` | `75.6%` | `92.31%` | 336 | 76 | `+2.5s` |
| `2026-10-29 04:30:20` | `72.24%` | `100.0%` | 353 | 86 | `+10.5s` |
| `2026-10-29 04:00:20` | `13.46%` | `100.0%` | 104 | 89 | `+43.2s` |
| `2026-10-29 03:30:18` | `16.22%` | `91.67%` | 111 | 90 | `+70.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:19.168000+00:00`.*
