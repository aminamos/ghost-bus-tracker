# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Metropolitan Transportation Authority** in **Austin, TX** (Austin–Round Rock Metropolitan Area, Texas).
> **Transit System:** CapMetro | **Location:** Austin, TX | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:21.472000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1903` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `168` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1903` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1903 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 800** | 196 | 0 | 196 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 145 | 0 | 145 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 300** | 130 | 0 | 130 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 127 | 0 | 127 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 120 | 0 | 120 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 803** | 92 | 0 | 92 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 383** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 271** | 69 | 0 | 69 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2999483_3675` | Route 20 | `03:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014878_21711` | Route 7 | `04:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014944_0948` | Route 10 | `04:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998893_1882` | Route 18 | `04:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014813_21980` | Route 7 | `04:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999482_3676` | Route 20 | `04:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004045_12697` | Route 337 | `04:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3001189_6959` | Route 300 | `04:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3004336_13343` | Route 339 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014879_21712` | Route 7 | `04:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3014945_0949` | Route 10 | `04:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2999339_2968` | Route 20 | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3015008_0421` | Route 10 | `04:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2998894_1883` | Route 18 | `04:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3000846_5466` | Route 3 | `04:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:21` | `100.0%` | `0.0%` | 1903 | 168 | `+0.0s` |
| `2026-11-23 06:30:18` | `99.79%` | `66.67%` | 1905 | 179 | `-38.3s` |
| `2026-11-23 06:00:32` | `99.37%` | `33.33%` | 1909 | 189 | `-78.2s` |
| `2026-11-23 05:30:19` | `98.28%` | `50.0%` | 1921 | 192 | `+164.8s` |
| `2026-11-23 05:00:25` | `96.23%` | `55.56%` | 1935 | 205 | `+76.5s` |
| `2026-11-23 04:30:23` | `93.77%` | `65.28%` | 1958 | 218 | `+85.7s` |
| `2026-11-23 04:00:20` | `90.73%` | `66.67%` | 1984 | 222 | `+37.8s` |
| `2026-11-23 03:30:19` | `87.38%` | `67.38%` | 2021 | 227 | `+80.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:21.472000+00:00`.*
