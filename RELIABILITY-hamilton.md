# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-24T06:30:22.448000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`99.45%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `361` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `2` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `359` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 359 | 99.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5783** | 138 | 0 | 138 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 96 | 0 | 96 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 87 | 1 | 86 | **`98.85%`** | `0.0%` | `+0.0s` |

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
| `2189971` | Route 5782 | `05:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190023` | Route 5782 | `06:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189975` | Route 5782 | `07:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190027` | Route 5782 | `08:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189979` | Route 5782 | `09:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190033` | Route 5782 | `10:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189986` | Route 5782 | `11:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190040` | Route 5782 | `12:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2189993` | Route 5782 | `13:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190047` | Route 5782 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190000` | Route 5782 | `16:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190053` | Route 5782 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190005` | Route 5782 | `18:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190057` | Route 5782 | `19:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2190009` | Route 5782 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-24 06:30:22` | `99.45%` | `0.0%` | 361 | 2 | `+0.0s` |
| `2026-10-24 05:30:20` | `88.24%` | `100.0%` | 408 | 50 | `+57.3s` |
| `2026-10-24 05:00:23` | `82.0%` | `87.5%` | 439 | 79 | `+13.2s` |
| `2026-10-24 04:30:21` | `81.02%` | `85.71%` | 453 | 86 | `+102.2s` |
| `2026-10-24 04:00:22` | `10.58%` | `92.86%` | 104 | 89 | `+45.6s` |
| `2026-10-24 03:30:34` | `18.92%` | `80.0%` | 111 | 91 | `+119.5s` |
| `2026-10-24 03:00:20` | `19.49%` | `87.5%` | 118 | 92 | `+72.6s` |
| `2026-10-24 02:30:33` | `24.62%` | `85.71%` | 130 | 95 | `+145.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-24T06:30:22.448000+00:00`.*
