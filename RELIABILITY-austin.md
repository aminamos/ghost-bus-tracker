# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.887000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`61.11%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1864` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `207` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1808` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+181.4s` (`+3.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+7.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 11 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.1% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1808 | 97.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 7 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 803** | 135 | 0 | 135 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 800** | 133 | 0 | 133 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 122 | 0 | 122 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 119 | 0 | 119 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 117 | 0 | 117 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 383** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 801** | `+51.3 min (+3079.0s)` | `+51.3 min (+3079s)` | 1 | `0.0%` |
| **Route 3** | `+3.5 min (+212.0s)` | `+3.5 min (+212s)` | 1 | `100.0%` |
| **Route 485** | `+0.8 min (+47.0s)` | `+2.3 min (+137s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `88.5 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.2 / 100` |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `97.7 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3014943_21698` | Route 7 | `23:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010891_23447` | Route 800 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005856_15994` | Route 483 | `27:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005911_16142` | Route 485 | `27:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005862_15932` | Route 483 | `27:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005909_16127` | Route 485 | `27:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997943_0039` | Route 1 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004207_13012` | Route 337 | `05:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997944_0040` | Route 1 | `05:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999608_3935` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004206_13013` | Route 337 | `05:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997945_0041` | Route 1 | `05:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998986_2082` | Route 18 | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014513_1254` | Route 10 | `05:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014630_21741` | Route 7 | `05:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `97.0%` | `61.11%` | 1864 | 207 | `+181.4s` |
| `2026-11-21 06:00:22` | `94.33%` | `62.5%` | 1921 | 237 | `+111.1s` |
| `2026-11-21 05:30:18` | `91.9%` | `59.78%` | 1975 | 255 | `+60.4s` |
| `2026-11-21 05:00:22` | `88.14%` | `58.7%` | 2040 | 261 | `+103.8s` |
| `2026-11-21 04:30:19` | `84.9%` | `57.56%` | 2080 | 271 | `+66.6s` |
| `2026-11-21 04:00:23` | `80.69%` | `52.73%` | 2035 | 270 | `+64.1s` |
| `2026-11-21 03:30:19` | `77.96%` | `57.37%` | 2096 | 277 | `+40.9s` |
| `2026-11-21 03:00:18` | `76.38%` | `59.64%` | 2113 | 283 | `+88.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.887000+00:00`.*
