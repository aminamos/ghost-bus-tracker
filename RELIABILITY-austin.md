# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-04T07:00:21.507000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.24%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1813` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `223` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1763` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1763 | 97.2% |
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
| **Route 271** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 333** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 4** | 62 | 0 | 62 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `3012295_24424` | Route 837 | `24:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005856_15390` | Route 483 | `27:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005911_15520` | Route 485 | `27:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005862_15340` | Route 483 | `27:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3005909_15508` | Route 485 | `27:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999483_3555` | Route 20 | `03:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014878_20896` | Route 7 | `04:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998893_1843` | Route 18 | `04:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014813_21213` | Route 7 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999482_3556` | Route 20 | `04:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004045_12742` | Route 337 | `04:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001189_7028` | Route 300 | `04:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014879_20897` | Route 7 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-04 07:00:21` | `97.24%` | `0.0%` | 1813 | 223 | `+0.0s` |
| `2026-11-04 06:30:33` | `96.16%` | `0.0%` | 1822 | 252 | `+0.0s` |
| `2026-11-04 06:00:22` | `94.25%` | `0.0%` | 1844 | 269 | `+0.0s` |
| `2026-11-04 05:30:18` | `91.91%` | `0.0%` | 1866 | 278 | `+0.0s` |
| `2026-11-04 05:00:20` | `88.1%` | `0.0%` | 1907 | 284 | `+0.0s` |
| `2026-11-04 04:30:18` | `84.27%` | `0.0%` | 1958 | 290 | `+0.0s` |
| `2026-11-04 04:00:26` | `80.81%` | `0.0%` | 2001 | 297 | `+0.0s` |
| `2026-11-04 03:30:22` | `77.71%` | `0.0%` | 2046 | 302 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-04T07:00:21.507000+00:00`.*
