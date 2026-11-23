# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:18.676000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `199` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `199` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 199 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5783** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5794** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 55 | 0 | 55 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2200211` | Route 5794 | `16:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200183` | Route 5794 | `09:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200190` | Route 5794 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200197` | Route 5794 | `12:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200205` | Route 5794 | `14:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200213` | Route 5794 | `16:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200174` | Route 5794 | `07:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200181` | Route 5794 | `08:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200188` | Route 5794 | `10:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200195` | Route 5794 | `12:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200202` | Route 5794 | `14:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200210` | Route 5794 | `16:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200218` | Route 5794 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200221` | Route 5794 | `19:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200224` | Route 5794 | `21:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:18` | `100.0%` | `0.0%` | 199 | 1 | `+0.0s` |
| `2026-11-23 06:30:18` | `100.0%` | `0.0%` | 199 | 1 | `+0.0s` |
| `2026-11-23 06:00:21` | `98.51%` | `0.0%` | 202 | 2 | `+0.0s` |
| `2026-11-23 05:30:18` | `89.33%` | `50.0%` | 225 | 26 | `-33.5s` |
| `2026-11-23 05:00:21` | `7.25%` | `100.0%` | 69 | 65 | `+40.4s` |
| `2026-11-23 04:30:21` | `5.49%` | `100.0%` | 91 | 88 | `+89.2s` |
| `2026-11-23 04:00:20` | `6.19%` | `80.0%` | 97 | 89 | `+204.6s` |
| `2026-11-23 03:30:18` | `10.0%` | `88.89%` | 100 | 89 | `+130.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:18.676000+00:00`.*
