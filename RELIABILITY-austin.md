# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:18.260000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.52%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1496` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `190` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1444` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1444 | 96.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 6 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 837** | 117 | 0 | 117 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 800** | 117 | 0 | 117 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 333** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 63 | 0 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 324** | 62 | 0 | 62 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `3005922_15529` | Route 485 | `27:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005923_15535` | Route 485 | `27:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999804_3867` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3011617_23409` | Route 801 | `05:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998013_0227` | Route 1 | `05:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001446_7410` | Route 300 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000943_5969` | Route 3 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999805_3868` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010537_21567` | Route 7 | `05:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3011618_23395` | Route 801 | `05:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010595_21038` | Route 7 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3011529_23163` | Route 801 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003816_11547` | Route 333 | `05:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003261_10601` | Route 324 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012046_24263` | Route 803 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:18` | `96.52%` | `0.0%` | 1496 | 190 | `+0.0s` |
| `2026-11-08 06:30:27` | `95.76%` | `0.0%` | 1511 | 201 | `+0.0s` |
| `2026-11-08 06:00:18` | `93.87%` | `0.0%` | 1549 | 219 | `+0.0s` |
| `2026-11-08 05:30:20` | `91.56%` | `0.0%` | 1588 | 236 | `+0.0s` |
| `2026-11-08 05:00:18` | `88.77%` | `0.0%` | 1639 | 251 | `+0.0s` |
| `2026-11-08 04:30:26` | `85.73%` | `0.0%` | 1689 | 253 | `+0.0s` |
| `2026-11-08 04:00:20` | `82.48%` | `0.0%` | 1747 | 253 | `+0.0s` |
| `2026-11-08 03:30:18` | `79.39%` | `0.0%` | 1781 | 255 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.260000+00:00`.*
