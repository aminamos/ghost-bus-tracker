# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-12T07:00:20.525000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.18%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `425` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `10` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `413` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+31.5s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+31.5s` (`+0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 0.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 413 | 97.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5801** | 100 | 0 | 100 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5794** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5792** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `+0.5 min` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | `+0.5 min (+31.5s)` | `+1.1 min (+63s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `97.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2200212` | Route 5794 | `16:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200204` | Route 5794 | `14:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200196` | Route 5794 | `12:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200225` | Route 5794 | `21:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200214` | Route 5794 | `17:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200228` | Route 5794 | `23:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200184` | Route 5794 | `09:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200198` | Route 5794 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200191` | Route 5794 | `11:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200206` | Route 5794 | `15:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200231` | Route 5794 | `24:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200199` | Route 5794 | `13:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200192` | Route 5794 | `11:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200167` | Route 5794 | `05:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200171` | Route 5794 | `06:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-12 07:00:20` | `97.18%` | `100.0%` | 425 | 10 | `+31.5s` |
| `2026-11-12 06:30:19` | `89.61%` | `100.0%` | 462 | 47 | `-1.8s` |
| `2026-11-12 06:00:19` | `82.66%` | `85.0%` | 496 | 77 | `+79.2s` |
| `2026-11-12 05:30:19` | `79.49%` | `87.5%` | 512 | 86 | `+18.6s` |
| `2026-11-12 05:00:21` | `8.0%` | `95.65%` | 100 | 90 | `+28.2s` |
| `2026-11-12 04:30:19` | `12.38%` | `95.56%` | 105 | 91 | `+60.4s` |
| `2026-11-12 04:00:19` | `13.64%` | `100.0%` | 110 | 93 | `+29.3s` |
| `2026-11-12 03:30:19` | `16.67%` | `100.0%` | 120 | 97 | `+34.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:20.525000+00:00`.*
