# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-18T06:30:19.172000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`84.11%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `302` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `49` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `254` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-7.6s` (`-0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 5 | 1.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 254 | 84.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5813** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `-0.5s` |
| **Route 5794** | 68 | 2 | 66 | **`97.06%`** | `100.0%` | `+0.0s` |
| **Route 5783** | 85 | 9 | 76 | **`89.41%`** | `100.0%` | `-18.5s` |
| **Route 5829** | 4 | 1 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 5807** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5830** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5793** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5806** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 5780** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `100.0 / 100` |
| **Route 5783** | ~15.0m | ~15.0m | **`+0.0 min`** | `97.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2190450` | Route 5783 | `24:22:00` | `SCHEDULED` | Assigned vehicle 12216 is broadcasting off-schedule with no vehicle covering 2190450 |
| `2200217` | Route 5794 | `17:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200209` | Route 5794 | `15:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200216` | Route 5794 | `17:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200208` | Route 5794 | `15:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200218` | Route 5794 | `18:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200221` | Route 5794 | `19:49:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200188` | Route 5794 | `10:42:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200201` | Route 5794 | `13:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200187` | Route 5794 | `10:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200193` | Route 5794 | `11:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200227` | Route 5794 | `22:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200198` | Route 5794 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200224` | Route 5794 | `21:19:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200181` | Route 5794 | `08:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-18 06:30:19` | `84.11%` | `100.0%` | 302 | 49 | `-7.6s` |
| `2026-11-18 05:00:18` | `10.0%` | `100.0%` | 100 | 90 | `+49.1s` |
| `2026-11-18 04:30:19` | `10.48%` | `91.67%` | 105 | 91 | `+69.5s` |
| `2026-11-18 04:00:18` | `14.41%` | `90.91%` | 111 | 93 | `+95.6s` |
| `2026-11-18 03:30:18` | `16.67%` | `92.31%` | 120 | 97 | `+79.5s` |
| `2026-11-18 03:00:19` | `18.98%` | `100.0%` | 137 | 108 | `+77.2s` |
| `2026-11-18 02:00:19` | `23.38%` | `80.0%` | 154 | 118 | `+143.2s` |
| `2026-11-18 01:30:20` | `26.51%` | `87.5%` | 166 | 124 | `+114.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-18T06:30:19.172000+00:00`.*
