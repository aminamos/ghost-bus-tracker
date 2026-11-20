# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-20T06:30:18.977000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`82.72%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`87.5%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `301` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `51` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `249` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-15.8s` (`-0.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 7 | 2.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 249 | 82.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `+0.0s` |
| **Route 5794** | 68 | 2 | 66 | **`97.06%`** | `100.0%` | `-2.0s` |
| **Route 5783** | 85 | 9 | 76 | **`89.41%`** | `100.0%` | `+0.2 min` |
| **Route 5793** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5807** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `-146.0s` |
| **Route 5830** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5806** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5792** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5780** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5783** | `+0.2 min (+12.0s)` | `+0.4 min (+24s)` | 9 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5783** | ~15.0m | ~15.0m | **`+0.0 min`** | `98.7 / 100` |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2190450` | Route 5783 | `24:22:00` | `SCHEDULED` | Assigned vehicle 32316 is broadcasting off-schedule with no vehicle covering 2190450 |
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

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-20 06:30:18` | `82.72%` | `87.5%` | 301 | 51 | `-15.8s` |
| `2026-11-20 06:00:20` | `74.77%` | `94.44%` | 329 | 78 | `+16.3s` |
| `2026-11-20 05:30:18` | `73.39%` | `92.0%` | 342 | 86 | `-8.2s` |
| `2026-11-20 05:00:19` | `8.0%` | `94.12%` | 100 | 90 | `+12.1s` |
| `2026-11-20 04:30:18` | `12.5%` | `87.5%` | 104 | 91 | `+80.1s` |
| `2026-11-20 04:00:18` | `13.89%` | `85.0%` | 108 | 93 | `+46.3s` |
| `2026-11-20 03:30:20` | `17.09%` | `95.0%` | 117 | 98 | `+39.0s` |
| `2026-11-20 03:00:19` | `23.13%` | `86.36%` | 147 | 110 | `+89.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-20T06:30:18.977000+00:00`.*
