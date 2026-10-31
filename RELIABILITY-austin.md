# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T07:00:33.573000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`97.23%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`50.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1623` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `213` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1578` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+174.8s` (`+2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+22.0s` (`+0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 9 | 0.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 3 | 0.2% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1578 | 97.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 6 | 0.4% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 800** | 132 | 0 | 132 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 837** | 124 | 0 | 124 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 122 | 0 | 122 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 116 | 0 | 116 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 337** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 18** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 486** | `+6.7 min (+402.0s)` | `+21.6 min (+1299s)` | 2 | `0.0%` |
| **Route 485** | `+5.0 min (+299.4s)` | `+14.8 min (+891s)` | 3 | `60.0%` |
| **Route 483** | `+0.1 min (+4.7s)` | `+3.0 min (+180s)` | 3 | `66.67%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `67.8 / 100` |
| **Route 485** | ~35.0m | ~35.0m | **`+0.0 min`** | `83.7 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.9 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3004207_12994` | Route 337 | `05:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997906_0333` | Route 1 | `05:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999608_3759` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004206_12995` | Route 337 | `05:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998986_2011` | Route 18 | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2997907_0334` | Route 1 | `05:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014513_1183` | Route 10 | `05:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014630_20920` | Route 7 | `05:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999609_3739` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014453_0655` | Route 10 | `05:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001336_7288` | Route 300 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014571_21457` | Route 7 | `05:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3012300_24648` | Route 837 | `05:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001397_6752` | Route 300 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003746_11474` | Route 333 | `05:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 07:00:33` | `97.23%` | `50.0%` | 1623 | 213 | `+174.8s` |
| `2026-10-31 06:30:24` | `96.8%` | `56.52%` | 1627 | 219 | `+181.3s` |
| `2026-10-31 06:00:20` | `96.39%` | `34.62%` | 1636 | 235 | `+223.1s` |
| `2026-10-31 05:30:22` | `95.23%` | `55.0%` | 1657 | 250 | `+179.0s` |
| `2026-10-31 05:00:34` | `93.11%` | `57.89%` | 1697 | 266 | `+161.9s` |
| `2026-10-31 04:30:25` | `90.79%` | `52.5%` | 1748 | 277 | `+146.6s` |
| `2026-10-31 04:00:18` | `86.84%` | `56.3%` | 1808 | 289 | `+82.3s` |
| `2026-10-31 03:30:22` | `83.0%` | `59.49%` | 1859 | 304 | `+40.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T07:00:33.573000+00:00`.*
