# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-26T07:00:23.017000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`92.75%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `193` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `179` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 179 | 92.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 72 | 2 | 70 | **`97.22%`** | `0.0%` | `+0.0s` |
| **Route 7** | 55 | 3 | 52 | **`94.55%`** | `0.0%` | `+0.0s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `30740066` | Route 7 | `15:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740082` | Route 7 | `22:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740077` | Route 7 | `20:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740085` | Route 7 | `24:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740081` | Route 7 | `22:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740076` | Route 7 | `19:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740086` | Route 7 | `25:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740069` | Route 7 | `16:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740084` | Route 7 | `24:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740080` | Route 7 | `21:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740075` | Route 7 | `19:23:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740078` | Route 7 | `20:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740072` | Route 7 | `18:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740079` | Route 7 | `21:13:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30740073` | Route 7 | `18:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:23` | `92.75%` | `0.0%` | 193 | 14 | `+0.0s` |
| `2026-10-26 06:30:42` | `94.27%` | `0.0%` | 192 | 10 | `+0.0s` |
| `2026-10-26 05:30:35` | `90.64%` | `0.0%` | 203 | 19 | `+0.0s` |
| `2026-10-26 05:00:27` | `86.38%` | `0.0%` | 213 | 29 | `-152.0s` |
| `2026-10-26 04:30:46` | `2.44%` | `0.0%` | 41 | 40 | `+0.0s` |
| `2026-10-26 04:00:20` | `3.51%` | `25.0%` | 57 | 55 | `+238.5s` |
| `2026-10-26 03:30:41` | `4.29%` | `40.0%` | 70 | 66 | `+84.4s` |
| `2026-10-26 01:00:31` | `13.89%` | `85.71%` | 144 | 123 | `+26.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:23.017000+00:00`.*
