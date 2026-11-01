# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:19.242000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`84.54%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `194` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `170` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `164` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+1836.5s` (`+30.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+1836.5s` (`+30.6 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 1 | 0.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 164 | 84.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 837** | 117 | 0 | 117 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 311** | 47 | 0 | 47 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 485** | 5 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 486** | 7 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 483** | 7 | 3 | 0 | **`0.0%`** | `50.0%` | `+30.6 min` |
| **Route 481** | 7 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 484** | 4 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 483** | `+30.6 min (+1836.5s)` | `+59.2 min (+3552s)` | 3 | `50.0%` |

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
| `3002053_8598` | Route 311 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012428_26658` | Route 837 | `05:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012486_26083` | Route 837 | `06:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002054_8599` | Route 311 | `06:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012429_26659` | Route 837 | `06:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012487_26084` | Route 837 | `06:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012430_26660` | Route 837 | `06:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002055_8600` | Route 311 | `06:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012488_26085` | Route 837 | `06:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012431_26661` | Route 837 | `06:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002056_8601` | Route 311 | `07:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012489_26086` | Route 837 | `07:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012432_26662` | Route 837 | `07:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002057_8603` | Route 311 | `07:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012490_26087` | Route 837 | `07:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:19` | `84.54%` | `50.0%` | 194 | 170 | `+1836.5s` |
| `2026-11-01 06:30:19` | `85.86%` | `66.67%` | 191 | 182 | `+1305.7s` |
| `2026-11-01 06:00:21` | `82.83%` | `50.0%` | 198 | 190 | `-43.5s` |
| `2026-11-01 05:30:23` | `72.69%` | `33.33%` | 227 | 201 | `-83.0s` |
| `2026-11-01 05:00:21` | `62.88%` | `0.0%` | 264 | 209 | `+0.0s` |
| `2026-11-01 04:30:24` | `56.16%` | `0.0%` | 292 | 220 | `+0.0s` |
| `2026-11-01 04:00:18` | `48.36%` | `100.0%` | 335 | 226 | `+143.5s` |
| `2026-11-01 03:30:20` | `42.45%` | `100.0%` | 384 | 228 | `-6.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:19.242000+00:00`.*
