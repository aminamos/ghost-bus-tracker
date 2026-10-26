# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-26T07:00:26.805000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1912` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `161` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1912` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1912 | 100.0% |
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
| **Route 663** | 106 | 0 | 106 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 310** | 71 | 0 | 71 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 333** | 65 | 0 | 65 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2998894_1844` | Route 18 | `04:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000846_5547` | Route 3 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014332_8405` | Route 311 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014814_21214` | Route 7 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:26` | `100.0%` | `0.0%` | 1912 | 161 | `+0.0s` |
| `2026-10-26 06:30:43` | `100.0%` | `0.0%` | 1909 | 173 | `+0.0s` |
| `2026-10-26 05:00:28` | `99.27%` | `0.0%` | 1911 | 194 | `+1442.7s` |
| `2026-10-26 04:00:21` | `95.26%` | `54.84%` | 1961 | 217 | `+413.0s` |
| `2026-10-26 03:30:48` | `92.55%` | `57.69%` | 1986 | 227 | `+285.3s` |
| `2026-10-26 01:00:32` | `78.82%` | `65.07%` | 2125 | 233 | `+204.9s` |
| `2026-10-26 00:30:49` | `77.33%` | `64.41%` | 2126 | 240 | `+191.3s` |
| `2026-10-25 23:30:45` | `75.68%` | `78.79%` | 2126 | 249 | `+132.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:26.805000+00:00`.*
