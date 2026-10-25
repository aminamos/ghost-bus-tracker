# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-25T06:15:49.775000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`44.44%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1485` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `166` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1430` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+412.0s` (`+6.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+86.5s` (`+1.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 8 | 0.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 0.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 0.3% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1430 | 96.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 4 | 0.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 800** | 117 | 0 | 117 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 18** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 392** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 63 | 0 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 337** | 63 | 0 | 63 | **`100.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 7** | `+25.6 min (+1535.0s)` | `+25.6 min (+1535s)` | 1 | `0.0%` |
| **Route 483** | `+7.1 min (+425.7s)` | `+33.9 min (+2035s)` | 3 | `33.33%` |
| **Route 486** | `+2.6 min (+154.6s)` | `+7.5 min (+447s)` | 2 | `80.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `58.0 / 100` |
| **Route 483** | ~30.0m | ~30.0m | **`+0.0 min`** | `69.9 / 100` |
| **Route 486** | ~30.0m | ~30.0m | **`+0.0 min`** | `91.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `3005876_15359` | Route 483 | `27:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999804_3867` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998359_1327` | Route 10 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001446_7410` | Route 300 | `05:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000943_5969` | Route 3 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001818_7920` | Route 310 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3002053_8736` | Route 311 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999805_3868` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010537_21567` | Route 7 | `05:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3010595_21038` | Route 7 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003816_11547` | Route 333 | `05:53:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013675_2809` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013708_2435` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999660_3299` | Route 20 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000968_5675` | Route 3 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:49` | `96.3%` | `44.44%` | 1485 | 166 | `+412.0s` |
| `2026-10-25 06:01:04` | `96.24%` | `42.11%` | 1488 | 171 | `+525.1s` |
| `2026-10-25 05:30:33` | `95.04%` | `20.69%` | 1512 | 182 | `+957.5s` |
| `2026-10-25 04:33:58` | `92.63%` | `50.0%` | 1575 | 211 | `+431.7s` |
| `2026-10-25 03:30:23` | `85.28%` | `60.16%` | 1685 | 226 | `+358.1s` |
| `2026-10-25 03:00:23` | `82.33%` | `65.0%` | 1732 | 226 | `+303.9s` |
| `2026-10-25 02:30:27` | `80.09%` | `66.67%` | 1768 | 229 | `+263.4s` |
| `2026-10-25 01:30:21` | `77.61%` | `62.61%` | 1858 | 244 | `+265.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:49.775000+00:00`.*
