# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-28T07:00:19.218000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.56%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`52.63%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1801` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `206` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1757` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-26.7s` (`-0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-32.0s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 10 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1757 | 97.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 800** | 196 | 0 | 196 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 145 | 0 | 145 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 337** | 123 | 0 | 123 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 71 | 0 | 71 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 333** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 486** | `+0.7 min (+41.0s)` | `+5.5 min (+333s)` | 2 | `25.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `90.6 / 100` |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `96.0 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.5 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2999483_3555` | Route 20 | `03:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014878_20896` | Route 7 | `04:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998893_1843` | Route 18 | `04:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014813_21213` | Route 7 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999482_3556` | Route 20 | `04:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004045_12742` | Route 337 | `04:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001189_7028` | Route 300 | `04:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014879_20897` | Route 7 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999339_2875` | Route 20 | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998894_1844` | Route 18 | `04:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000846_5547` | Route 3 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014332_8405` | Route 311 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014814_21214` | Route 7 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003562_11707` | Route 333 | `04:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997834_0295` | Route 1 | `04:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-28 07:00:19` | `97.56%` | `52.63%` | 1801 | 206 | `-26.7s` |
| `2026-10-28 06:30:22` | `97.23%` | `63.64%` | 1804 | 220 | `-1.0s` |
| `2026-10-28 06:00:23` | `97.01%` | `60.87%` | 1807 | 230 | `+33.5s` |
| `2026-10-28 05:30:27` | `96.19%` | `58.82%` | 1813 | 246 | `-8.1s` |
| `2026-10-28 05:00:27` | `94.21%` | `61.11%` | 1832 | 264 | `-8.7s` |
| `2026-10-28 04:30:33` | `91.62%` | `52.56%` | 1862 | 275 | `+21.0s` |
| `2026-10-28 04:00:33` | `88.35%` | `60.36%` | 1897 | 291 | `-5.5s` |
| `2026-10-28 03:30:22` | `84.47%` | `59.09%` | 1945 | 294 | `+31.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-28T07:00:19.218000+00:00`.*
