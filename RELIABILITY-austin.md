# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-29T07:00:19.356000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.69%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1863` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `222` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1820` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+9.2s` (`+0.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-9.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 11 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 8 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.1% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1820 | 97.7% |
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
| **Route 311** | 100 | 0 | 100 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 271** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 71 | 0 | 71 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | `+2.3 min (+136.8s)` | `+8.2 min (+489s)` | 3 | `80.0%` |
| **Route 486** | `+0.7 min (+40.2s)` | `+4.8 min (+289s)` | 2 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `91.5 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.2 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.5 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.3 / 100` |
| **Route 484** | ~45.0m | ~45.0m | **`+0.0 min`** | `99.9 / 100` |

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
| `2026-10-29 07:00:19` | `97.69%` | `55.0%` | 1863 | 222 | `+9.2s` |
| `2026-10-29 06:30:25` | `97.52%` | `61.9%` | 1898 | 222 | `-23.5s` |
| `2026-10-29 06:00:24` | `97.58%` | `55.0%` | 1898 | 234 | `-28.2s` |
| `2026-10-29 05:30:19` | `96.08%` | `56.25%` | 1913 | 257 | `+12.0s` |
| `2026-10-29 05:00:20` | `93.96%` | `57.45%` | 1937 | 267 | `+19.4s` |
| `2026-10-29 04:30:22` | `91.97%` | `58.46%` | 1955 | 300 | `+18.8s` |
| `2026-10-29 04:00:20` | `88.01%` | `56.99%` | 2010 | 311 | `-1.7s` |
| `2026-10-29 03:30:18` | `84.4%` | `58.4%` | 2058 | 317 | `+51.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-29T07:00:19.356000+00:00`.*
