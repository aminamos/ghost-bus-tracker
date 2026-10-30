# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-30T07:00:25.978000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `248` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `248` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 248 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 108 | 0 | 108 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5803** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2190384` | Route 5783 | `14:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190365` | Route 5783 | `11:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190344` | Route 5783 | `08:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190322` | Route 5783 | `05:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190448` | Route 5783 | `23:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190433` | Route 5783 | `20:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190410` | Route 5783 | `17:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190382` | Route 5783 | `13:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190361` | Route 5783 | `10:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190334` | Route 5783 | `06:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190447` | Route 5783 | `23:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190432` | Route 5783 | `20:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190412` | Route 5783 | `17:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190392` | Route 5783 | `15:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190371` | Route 5783 | `12:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 07:00:25` | `100.0%` | `0.0%` | 248 | 1 | `+0.0s` |
| `2026-10-30 06:00:25` | `96.12%` | `0.0%` | 258 | 10 | `+0.0s` |
| `2026-10-30 05:30:26` | `82.71%` | `100.0%` | 295 | 49 | `+23.2s` |
| `2026-10-30 05:00:20` | `74.69%` | `75.0%` | 324 | 75 | `+73.5s` |
| `2026-10-30 04:30:18` | `71.72%` | `90.91%` | 343 | 85 | `+129.3s` |
| `2026-10-30 04:00:21` | `10.78%` | `83.33%` | 102 | 89 | `+97.7s` |
| `2026-10-30 03:30:18` | `14.68%` | `81.82%` | 109 | 90 | `+127.8s` |
| `2026-10-30 03:00:20` | `17.24%` | `85.71%` | 116 | 92 | `+82.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T07:00:25.978000+00:00`.*
