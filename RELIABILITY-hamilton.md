# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-04T07:00:21.305000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.67%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `254` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `10` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `243` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-12.7s` (`-0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 1.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 243 | 95.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `-19.0s` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.4 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2200251` | Route 5795 | `09:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200256` | Route 5795 | `11:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200278` | Route 5795 | `17:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200280` | Route 5795 | `18:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200246` | Route 5795 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200294` | Route 5795 | `25:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200275` | Route 5795 | `16:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200271` | Route 5795 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200244` | Route 5795 | `07:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200238` | Route 5795 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200268` | Route 5795 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200250` | Route 5795 | `09:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200255` | Route 5795 | `10:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200242` | Route 5795 | `07:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200263` | Route 5795 | `13:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:21` | `95.67%` | `100.0%` | 254 | 10 | `-12.7s` |
| `2026-11-04 06:00:18` | `73.68%` | `87.5%` | 323 | 77 | `+47.6s` |
| `2026-11-04 05:30:18` | `71.22%` | `95.45%` | 337 | 87 | `+14.0s` |
| `2026-11-04 05:00:17` | `8.82%` | `85.71%` | 102 | 92 | `+328.6s` |
| `2026-11-04 04:30:17` | `11.32%` | `85.71%` | 106 | 92 | `+113.4s` |
| `2026-11-04 04:00:25` | `13.51%` | `75.0%` | 111 | 94 | `+184.4s` |
| `2026-11-04 03:30:21` | `15.7%` | `100.0%` | 121 | 99 | `+50.7s` |
| `2026-11-04 02:30:19` | `19.73%` | `82.35%` | 147 | 116 | `+61.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:21.305000+00:00`.*
