# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-02T07:00:18.474000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `244` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `244` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 244 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 108 | 0 | 108 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2200266` | Route 5795 | `14:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200261` | Route 5795 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200246` | Route 5795 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200278` | Route 5795 | `17:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200271` | Route 5795 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200273` | Route 5795 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200294` | Route 5795 | `25:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200292` | Route 5795 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200289` | Route 5795 | `22:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200275` | Route 5795 | `16:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200268` | Route 5795 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200283` | Route 5795 | `19:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200279` | Route 5795 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200249` | Route 5795 | `08:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200242` | Route 5795 | `07:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-02 07:00:18` | `100.0%` | `0.0%` | 244 | 1 | `+0.0s` |
| `2026-11-02 06:30:18` | `100.0%` | `0.0%` | 244 | 1 | `+0.0s` |
| `2026-11-02 06:00:23` | `99.19%` | `0.0%` | 247 | 3 | `+3789.0s` |
| `2026-11-02 05:30:22` | `91.14%` | `0.0%` | 271 | 26 | `+3838.7s` |
| `2026-11-02 05:00:19` | `4.41%` | `0.0%` | 68 | 65 | `+3810.1s` |
| `2026-11-02 04:30:21` | `6.45%` | `0.0%` | 93 | 86 | `+3672.1s` |
| `2026-11-02 04:00:18` | `8.08%` | `0.0%` | 99 | 89 | `+3765.7s` |
| `2026-11-02 03:30:25` | `13.59%` | `0.0%` | 103 | 91 | `+3657.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-02T07:00:18.474000+00:00`.*
