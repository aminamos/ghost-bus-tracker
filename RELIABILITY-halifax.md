# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-23T07:01:26.418000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `733` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `0` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `733` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 733 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 107 | 0 | 107 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7A** | 101 | 0 | 101 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7B** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 55 | 0 | 55 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 24** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 34 | 0 | 34 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4658285` | Route 72 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649423` | Route 1 | `24:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649417` | Route 1 | `22:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649409` | Route 1 | `21:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649400` | Route 1 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649391` | Route 1 | `18:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649379` | Route 1 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649368` | Route 1 | `14:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649358` | Route 1 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649346` | Route 1 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649337` | Route 1 | `09:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649327` | Route 1 | `07:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4649320` | Route 1 | `06:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4650502` | Route 182 | `06:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4661710` | Route 9B | `06:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:26` | `100.0%` | `0.0%` | 733 | 0 | `+0.0s` |
| `2026-10-23 06:30:25` | `100.0%` | `0.0%` | 733 | 0 | `+0.0s` |
| `2026-10-23 06:00:22` | `100.0%` | `0.0%` | 733 | 0 | `+0.0s` |
| `2026-10-23 05:30:23` | `100.0%` | `0.0%` | 733 | 0 | `+0.0s` |
| `2026-10-23 05:15:29` | `100.0%` | `0.0%` | 733 | 0 | `+0.0s` |
| `2026-10-23 05:00:43` | `100.0%` | `0.0%` | 1 | 0 | `+0.0s` |
| `2026-10-23 04:30:38` | `25.0%` | `66.67%` | 4 | 3 | `+4.3s` |
| `2026-10-23 04:00:42` | `12.9%` | `66.67%` | 31 | 22 | `-47.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:26.418000+00:00`.*
