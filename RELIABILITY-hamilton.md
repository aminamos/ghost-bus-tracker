# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-23T07:01:26.591000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`99.72%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `361` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `2` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `360` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 360 | 99.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 108 | 0 | 108 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 76 | 0 | 76 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5802** | 73 | 0 | 73 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 60 | 0 | 60 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5807** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5803** | 4 | 0 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2189879` | Route 5782 | `04:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189932` | Route 5782 | `05:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189911` | Route 5782 | `07:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189942` | Route 5782 | `08:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189885` | Route 5782 | `09:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189949` | Route 5782 | `10:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189894` | Route 5782 | `12:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189956` | Route 5782 | `13:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189898` | Route 5782 | `14:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189964` | Route 5782 | `15:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189906` | Route 5782 | `17:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189921` | Route 5782 | `18:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189875` | Route 5782 | `19:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189926` | Route 5782 | `21:01:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189865` | Route 5782 | `22:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-23 07:01:26` | `99.72%` | `0.0%` | 361 | 2 | `+0.0s` |
| `2026-10-23 06:30:26` | `95.0%` | `75.0%` | 380 | 18 | `+23.8s` |
| `2026-10-23 06:00:22` | `95.0%` | `75.0%` | 380 | 18 | `+23.8s` |
| `2026-10-23 05:30:23` | `79.82%` | `92.0%` | 451 | 83 | `+17.0s` |
| `2026-10-23 05:15:29` | `79.82%` | `92.0%` | 451 | 83 | `+17.0s` |
| `2026-10-23 05:00:43` | `79.82%` | `92.0%` | 451 | 83 | `+17.0s` |
| `2026-10-23 04:30:38` | `78.33%` | `96.77%` | 466 | 87 | `+16.9s` |
| `2026-10-23 04:00:42` | `16.51%` | `88.24%` | 109 | 89 | `+73.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-23T07:01:26.591000+00:00`.*
