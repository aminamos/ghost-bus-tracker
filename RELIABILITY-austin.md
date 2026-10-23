# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-23T07:01:27.550000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.84%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`36.84%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2126` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `226` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2080` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+460.1s` (`+7.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-27.0s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 7 | 0.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2080 | 97.8% |
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
| **Route 837** | 115 | 0 | 115 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 18** | 74 | 0 | 74 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 486** | `+19.0 min (+1137.6s)` | `+65.4 min (+3925s)` | 2 | `12.5%` |
| **Route 485** | `+0.5 min (+32.5s)` | `+1.3 min (+76s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 486** | ~30.0m | ~30.0m | **`+0.2 min`** | `7.8 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `90.9 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `96.3 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.8 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2999483_3555` | Route 20 | `03:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014878_20896` | Route 7 | `04:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014944_0927` | Route 10 | `04:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998893_1843` | Route 18 | `04:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014813_21213` | Route 7 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999482_3556` | Route 20 | `04:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004045_12742` | Route 337 | `04:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001189_7028` | Route 300 | `04:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014879_20897` | Route 7 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014945_0928` | Route 10 | `04:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999339_2875` | Route 20 | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001028_6261` | Route 30 | `04:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998894_1844` | Route 18 | `04:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000846_5547` | Route 3 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014332_8405` | Route 311 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:27` | `97.84%` | `36.84%` | 2126 | 226 | `+460.1s` |
| `2026-10-23 06:30:32` | `97.56%` | `52.17%` | 2128 | 241 | `+333.8s` |
| `2026-10-23 06:00:24` | `97.42%` | `44.0%` | 2130 | 248 | `+143.9s` |
| `2026-10-23 05:30:28` | `96.67%` | `47.22%` | 2132 | 261 | `-15.8s` |
| `2026-10-23 05:15:29` | `96.25%` | `63.64%` | 2131 | 268 | `-17.9s` |
| `2026-10-23 05:00:43` | `94.83%` | `62.71%` | 2145 | 271 | `+39.8s` |
| `2026-10-23 04:30:41` | `92.6%` | `59.49%` | 2162 | 281 | `+119.1s` |
| `2026-10-23 04:00:43` | `89.32%` | `62.73%` | 2190 | 291 | `+109.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:27.550000+00:00`.*
