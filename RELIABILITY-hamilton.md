# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-16T07:00:22.445000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `252` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `252` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 252 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 108 | 0 | 108 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5794** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2200169` | Route 5794 | `05:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200215` | Route 5794 | `17:26:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200168` | Route 5794 | `05:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200180` | Route 5794 | `08:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200173` | Route 5794 | `06:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200228` | Route 5794 | `23:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200225` | Route 5794 | `21:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200204` | Route 5794 | `14:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200212` | Route 5794 | `16:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200182` | Route 5794 | `09:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200185` | Route 5794 | `09:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200167` | Route 5794 | `05:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200171` | Route 5794 | `06:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200170` | Route 5794 | `06:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200177` | Route 5794 | `07:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-16 07:00:22` | `100.0%` | `0.0%` | 252 | 1 | `+0.0s` |
| `2026-11-16 06:00:19` | `98.82%` | `0.0%` | 255 | 2 | `+0.0s` |
| `2026-11-16 05:30:20` | `93.94%` | `66.67%` | 330 | 23 | `-83.3s` |
| `2026-11-16 05:00:21` | `6.15%` | `100.0%` | 65 | 64 | `+34.9s` |
| `2026-11-16 04:30:19` | `7.69%` | `100.0%` | 91 | 85 | `+65.6s` |
| `2026-11-16 04:00:19` | `8.16%` | `92.86%` | 98 | 90 | `+25.4s` |
| `2026-11-16 03:30:18` | `13.73%` | `100.0%` | 102 | 90 | `+60.8s` |
| `2026-11-16 02:30:18` | `17.24%` | `100.0%` | 116 | 96 | `+36.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-16T07:00:22.445000+00:00`.*
