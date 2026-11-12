# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-12T07:00:21.362000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`25.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `75` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `234` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `19` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 19 | 25.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 16 | 21.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 4** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 837** | 2 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 481** | 15 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 485** | 10 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 486** | 10 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 483** | 10 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 484** | 6 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `3014764_14818` | Route 4 | `08:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014765_14788` | Route 4 | `08:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014766_14925` | Route 4 | `09:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014767_14894` | Route 4 | `09:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014768_14926` | Route 4 | `09:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014769_14855` | Route 4 | `10:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014770_14856` | Route 4 | `10:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014771_14955` | Route 4 | `10:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014772_14927` | Route 4 | `10:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014773_14956` | Route 4 | `11:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014774_14895` | Route 4 | `11:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014775_14896` | Route 4 | `11:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014776_14982` | Route 4 | `11:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014777_14957` | Route 4 | `12:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014778_14983` | Route 4 | `12:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-12 07:00:21` | `25.33%` | `0.0%` | 75 | 234 | `+0.0s` |
| `2026-11-12 06:30:19` | `20.0%` | `100.0%` | 95 | 248 | `+54.0s` |
| `2026-11-12 06:00:21` | `14.73%` | `0.0%` | 129 | 263 | `+699.5s` |
| `2026-11-12 05:30:21` | `10.44%` | `0.0%` | 182 | 275 | `+279.7s` |
| `2026-11-12 05:00:21` | `7.54%` | `50.0%` | 252 | 285 | `+10.8s` |
| `2026-11-12 04:30:19` | `5.71%` | `50.0%` | 333 | 289 | `+401.7s` |
| `2026-11-12 04:00:20` | `4.61%` | `42.86%` | 412 | 297 | `+538.1s` |
| `2026-11-12 03:30:19` | `3.84%` | `57.14%` | 495 | 305 | `+315.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-12T07:00:21.362000+00:00`.*
