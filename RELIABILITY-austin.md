# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-07T07:00:20.408000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.42%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1452` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `205` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1400` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1400 | 96.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 800** | 133 | 0 | 133 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 122 | 0 | 122 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 119 | 0 | 119 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 333** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 803** | 62 | 0 | 62 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 383** | 48 | 0 | 48 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 271** | 43 | 0 | 43 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `3014943_20889` | Route 7 | `23:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010891_22584` | Route 800 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012196_24647` | Route 837 | `24:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012295_24424` | Route 837 | `24:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005856_15390` | Route 483 | `27:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005911_15520` | Route 485 | `27:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005862_15340` | Route 483 | `27:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005909_15508` | Route 485 | `27:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004207_12994` | Route 337 | `05:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999608_3759` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004206_12995` | Route 337 | `05:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998986_2011` | Route 18 | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003692_11835` | Route 333 | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014630_20920` | Route 7 | `05:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999609_3739` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-07 07:00:20` | `96.42%` | `0.0%` | 1452 | 205 | `+0.0s` |
| `2026-11-07 06:30:23` | `94.84%` | `0.0%` | 1473 | 230 | `+0.0s` |
| `2026-11-07 06:00:22` | `93.04%` | `0.0%` | 1508 | 245 | `+0.0s` |
| `2026-11-07 05:30:19` | `90.02%` | `0.0%` | 1553 | 254 | `+0.0s` |
| `2026-11-07 05:00:19` | `84.89%` | `0.0%` | 1621 | 265 | `+0.0s` |
| `2026-11-07 04:30:19` | `81.01%` | `0.0%` | 1675 | 273 | `+0.0s` |
| `2026-11-07 04:00:24` | `76.85%` | `0.0%` | 1728 | 276 | `+0.0s` |
| `2026-11-07 03:30:21` | `74.24%` | `0.0%` | 1786 | 282 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-07T07:00:20.408000+00:00`.*
