# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T06:30:22.724000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.76%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`52.94%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1573` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `205` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1522` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+12.0s` (`+0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-45.0s` (`-0.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 9 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 7 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1522 | 96.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 9 | 0.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 800** | 132 | 0 | 132 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 122 | 0 | 122 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 337** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 18** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 837** | `+13.6 min (+814.0s)` | `+13.6 min (+814s)` | 1 | `0.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.8 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.7 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3004207_12994` | Route 337 | `05:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997906_0333` | Route 1 | `05:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999608_3759` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004206_12995` | Route 337 | `05:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998986_2011` | Route 18 | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997907_0334` | Route 1 | `05:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014513_1183` | Route 10 | `05:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014630_20920` | Route 7 | `05:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001955_8638` | Route 311 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999609_3739` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001336_7288` | Route 300 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014571_21457` | Route 7 | `05:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001397_6752` | Route 300 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003746_11474` | Route 333 | `05:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013583_2741` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:22` | `96.76%` | `52.94%` | 1573 | 205 | `+12.0s` |
| `2026-10-24 05:30:21` | `94.77%` | `40.0%` | 1607 | 240 | `+335.1s` |
| `2026-10-24 05:00:24` | `92.71%` | `52.83%` | 1645 | 260 | `+356.6s` |
| `2026-10-24 04:30:25` | `89.68%` | `56.32%` | 1696 | 287 | `+178.8s` |
| `2026-10-24 04:00:23` | `85.85%` | `55.74%` | 1760 | 304 | `+194.2s` |
| `2026-10-24 03:00:21` | `78.13%` | `61.61%` | 1870 | 309 | `+114.8s` |
| `2026-10-24 02:00:26` | `72.7%` | `62.08%` | 1967 | 323 | `+127.9s` |
| `2026-10-24 01:30:26` | `71.33%` | `60.85%` | 2023 | 336 | `+181.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.724000+00:00`.*
