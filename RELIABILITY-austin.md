# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-14T07:00:22.140000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`66.26%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `163` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `214` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `108` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+32.0s` (`+0.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+14.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 1.8% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 108 | 66.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 4 | 2.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 311** | 49 | 0 | 49 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 59 | 1 | 58 | **`98.31%`** | `0.0%` | `+0.0s` |
| **Route 481** | 14 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 486** | 11 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 483** | 11 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 485** | 8 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.5 min` |
| **Route 484** | 6 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | `+0.5 min (+32.0s)` | `+1.4 min (+84s)` | 3 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `98.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3014513_1268` | Route 10 | `05:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002004_7933` | Route 311 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014514_1269` | Route 10 | `06:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014515_1270` | Route 10 | `06:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002005_7934` | Route 311 | `06:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014516_1271` | Route 10 | `06:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014517_1272` | Route 10 | `06:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002006_7935` | Route 311 | `07:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014518_1273` | Route 10 | `07:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002007_7936` | Route 311 | `07:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014519_1274` | Route 10 | `07:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002008_7939` | Route 311 | `07:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014520_1275` | Route 10 | `07:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014521_1276` | Route 10 | `07:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002009_7937` | Route 311 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:22` | `66.26%` | `100.0%` | 163 | 214 | `+32.0s` |
| `2026-11-14 06:30:25` | `58.7%` | `66.67%` | 184 | 231 | `+109.7s` |
| `2026-11-14 06:00:26` | `50.23%` | `57.14%` | 215 | 253 | `+123.2s` |
| `2026-11-14 05:30:19` | `39.78%` | `54.84%` | 269 | 265 | `-4.7s` |
| `2026-11-14 05:00:28` | `32.53%` | `59.52%` | 332 | 284 | `+54.1s` |
| `2026-11-14 04:30:21` | `25.62%` | `71.15%` | 406 | 285 | `+49.1s` |
| `2026-11-14 04:00:24` | `21.16%` | `59.65%` | 482 | 286 | `-6.0s` |
| `2026-11-14 03:30:23` | `18.07%` | `72.46%` | 559 | 295 | `+76.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:22.140000+00:00`.*
