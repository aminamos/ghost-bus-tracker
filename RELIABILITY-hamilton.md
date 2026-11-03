# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-03T07:00:18.758000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.28%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `254` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `11` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `242` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+72.2s` (`+1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 1.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 242 | 95.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `-12.5s` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 61 | 1 | 59 | **`96.72%`** | `50.0%` | `+2.6 min` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5795** | `+2.6 min (+157.0s)` | `+5.2 min (+314s)` | 1 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5795** | ~20.0m | ~20.0m | **`+0.0 min`** | `86.9 / 100` |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `99.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2190334` | Route 5783 | `06:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190447` | Route 5783 | `23:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190365` | Route 5783 | `11:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190344` | Route 5783 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190322` | Route 5783 | `05:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190448` | Route 5783 | `23:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190433` | Route 5783 | `20:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190410` | Route 5783 | `17:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190382` | Route 5783 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190361` | Route 5783 | `10:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190432` | Route 5783 | `20:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190412` | Route 5783 | `17:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190384` | Route 5783 | `14:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190420` | Route 5783 | `18:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190392` | Route 5783 | `15:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-03 07:00:18` | `95.28%` | `75.0%` | 254 | 11 | `+72.2s` |
| `2026-11-03 06:00:19` | `73.68%` | `86.67%` | 323 | 77 | `+79.7s` |
| `2026-11-03 05:30:18` | `70.03%` | `96.15%` | 337 | 88 | `+64.7s` |
| `2026-11-03 05:00:25` | `10.0%` | `90.0%` | 100 | 90 | `+11.4s` |
| `2026-11-03 04:30:21` | `12.26%` | `92.31%` | 106 | 92 | `+98.6s` |
| `2026-11-03 04:00:20` | `14.29%` | `71.43%` | 112 | 95 | `+219.7s` |
| `2026-11-03 03:30:20` | `15.7%` | `100.0%` | 121 | 100 | `+48.4s` |
| `2026-11-03 03:00:18` | `17.52%` | `88.24%` | 137 | 110 | `+75.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-03T07:00:18.758000+00:00`.*
