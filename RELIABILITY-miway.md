# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-09T07:00:19.724000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.64%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `367` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `14` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `351` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-237.0s` (`-4.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-237.0s` (`-4.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 351 | 95.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 101** | 68 | 0 | 68 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 57 | 0 | 57 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 74 | 1 | 72 | **`97.3%`** | `0.0%` | `+0.0s` |
| **Route 1** | 89 | 4 | 84 | **`94.38%`** | `0.0%` | `-237.0s` |
| **Route 11** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 61** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `30726898` | Route 1 | `04:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726651` | Route 1 | `06:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726661` | Route 1 | `08:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726724` | Route 1 | `25:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726668` | Route 1 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726659` | Route 1 | `08:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726669` | Route 1 | `10:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726679` | Route 1 | `13:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726690` | Route 1 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726701` | Route 1 | `18:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726710` | Route 1 | `20:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726666` | Route 1 | `09:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726676` | Route 1 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726686` | Route 1 | `14:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30726698` | Route 1 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-09 07:00:19` | `95.64%` | `0.0%` | 367 | 14 | `-237.0s` |
| `2026-11-09 06:30:22` | `95.16%` | `50.0%` | 372 | 18 | `-48.5s` |
| `2026-11-09 06:00:18` | `92.45%` | `0.0%` | 384 | 29 | `-128.3s` |
| `2026-11-09 05:30:18` | `4.55%` | `50.0%` | 44 | 42 | `-65.2s` |
| `2026-11-09 05:00:18` | `6.67%` | `40.0%` | 60 | 56 | `-59.6s` |
| `2026-11-09 04:30:19` | `8.33%` | `28.57%` | 72 | 66 | `-396.7s` |
| `2026-11-09 04:00:19` | `10.59%` | `33.33%` | 85 | 77 | `-63.5s` |
| `2026-11-09 03:30:18` | `10.58%` | `51.06%` | 104 | 92 | `-148.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-09T07:00:19.724000+00:00`.*
