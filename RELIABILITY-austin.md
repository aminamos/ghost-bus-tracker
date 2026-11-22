# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-22T07:00:19.566000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.12%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`66.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1735` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `178` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1685` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+154.9s` (`+2.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+43.0s` (`+0.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 10 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.1% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1685 | 97.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 803** | 136 | 0 | 136 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 800** | 117 | 0 | 117 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 801** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 383** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | `+4.6 min (+278.0s)` | `+11.6 min (+693s)` | 3 | `75.0%` |
| **Route 483** | `+1.8 min (+110.2s)` | `+18.6 min (+1116s)` | 3 | `63.64%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `74.8 / 100` |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `88.4 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `92.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3011903_24902` | Route 803 | `23:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005870_16011` | Route 483 | `27:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005922_16157` | Route 485 | `27:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005876_15958` | Route 483 | `27:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005923_16163` | Route 485 | `27:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999804_4043` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998013_0076` | Route 1 | `05:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998359_1384` | Route 10 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001446_7406` | Route 300 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000943_5911` | Route 3 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004461_13449` | Route 339 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999805_4044` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010537_22394` | Route 7 | `05:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010595_21859` | Route 7 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3011529_24010` | Route 801 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-22 07:00:19` | `97.12%` | `66.67%` | 1735 | 178 | `+154.9s` |
| `2026-11-22 06:30:22` | `96.4%` | `50.0%` | 1751 | 191 | `+110.3s` |
| `2026-11-22 06:00:21` | `94.85%` | `59.52%` | 1785 | 206 | `+130.0s` |
| `2026-11-22 05:00:21` | `90.38%` | `67.96%` | 1872 | 231 | `+131.4s` |
| `2026-11-22 04:30:18` | `87.63%` | `66.43%` | 1908 | 226 | `+126.4s` |
| `2026-11-22 04:00:19` | `84.53%` | `69.19%` | 1971 | 228 | `+108.8s` |
| `2026-11-22 03:30:22` | `82.0%` | `68.75%` | 2006 | 233 | `+138.9s` |
| `2026-11-22 03:00:20` | `80.2%` | `66.4%` | 2035 | 233 | `+286.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-22T07:00:19.566000+00:00`.*
