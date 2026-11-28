# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-28T07:00:21.031000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1400` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `157` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1400` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1400 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 800** | 132 | 0 | 132 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 126 | 0 | 126 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 122 | 0 | 122 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 118 | 0 | 118 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 117 | 0 | 117 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 383** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 803** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 322** | 67 | 0 | 67 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `3004207_13012` | Route 337 | `05:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999608_3935` | Route 20 | `05:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004206_13013` | Route 337 | `05:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998986_2082` | Route 18 | `05:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014513_1254` | Route 10 | `05:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014630_21741` | Route 7 | `05:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999609_3915` | Route 20 | `05:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014453_0722` | Route 10 | `05:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3011908_25416` | Route 803 | `05:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001336_7284` | Route 300 | `05:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014571_22284` | Route 7 | `05:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001397_6745` | Route 300 | `05:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3003746_11400` | Route 333 | `05:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013583_2863` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3013617_2464` | Route 2 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:21` | `100.0%` | `0.0%` | 1400 | 157 | `+0.0s` |
| `2026-11-28 06:30:22` | `99.64%` | `0.0%` | 1403 | 179 | `+482.5s` |
| `2026-11-28 06:00:23` | `99.08%` | `20.0%` | 1407 | 196 | `+133.2s` |
| `2026-11-28 05:30:21` | `97.75%` | `15.38%` | 1424 | 195 | `+166.8s` |
| `2026-11-28 05:00:24` | `94.89%` | `45.45%` | 1448 | 204 | `+110.5s` |
| `2026-11-28 04:30:19` | `91.57%` | `56.36%` | 1482 | 209 | `+66.4s` |
| `2026-11-28 04:00:24` | `87.63%` | `66.25%` | 1504 | 210 | `+62.0s` |
| `2026-11-28 03:30:23` | `84.22%` | `70.91%` | 1546 | 216 | `+36.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:21.031000+00:00`.*
