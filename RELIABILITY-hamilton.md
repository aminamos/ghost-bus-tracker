# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-15T07:00:19.239000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`96.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`100.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `216` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `8` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `208` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+7.0s` (`+0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-14.0s` (`-0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 5 | 2.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 208 | 96.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 73 | 1 | 72 | **`98.63%`** | `100.0%` | `+0.0 min` |
| **Route 5783** | 60 | 1 | 59 | **`98.33%`** | `100.0%` | `+2.1 min` |
| **Route 5795** | 38 | 1 | 37 | **`97.37%`** | `100.0%` | `-47.0s` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-30.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5783** | `+2.1 min (+124.0s)` | `+2.1 min (+124s)` | 1 | `100.0%` |
| **Route 5782** | `+0.0 min (+2.0s)` | `+0.0 min (+2s)` | 1 | `100.0%` |

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
| `2197823` | Route 5807 | `24:46:00` | `SCHEDULED` | Assigned vehicle 11612 is missing from active GPS transponder fleet |
| `2194119` | Route 5795 | `08:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193846` | Route 5794 | `17:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194149` | Route 5795 | `22:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193865` | Route 5794 | `07:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194128` | Route 5795 | `07:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194153` | Route 5795 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194147` | Route 5795 | `21:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194124` | Route 5795 | `10:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194138` | Route 5795 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194141` | Route 5795 | `18:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194148` | Route 5795 | `21:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194117` | Route 5795 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194136` | Route 5795 | `14:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194132` | Route 5795 | `13:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-15 07:00:19` | `96.3%` | `100.0%` | 216 | 8 | `+7.0s` |
| `2026-11-15 06:30:19` | `84.55%` | `89.47%` | 246 | 38 | `+2.7s` |
| `2026-11-15 05:30:19` | `72.26%` | `92.31%` | 292 | 80 | `+86.0s` |
| `2026-11-15 05:00:19` | `10.42%` | `90.0%` | 96 | 85 | `+105.1s` |
| `2026-11-15 04:30:19` | `14.95%` | `90.91%` | 107 | 92 | `+106.5s` |
| `2026-11-15 04:00:20` | `16.07%` | `92.31%` | 112 | 92 | `+69.2s` |
| `2026-11-15 03:30:18` | `21.01%` | `100.0%` | 119 | 94 | `+54.7s` |
| `2026-11-15 03:00:20` | `24.62%` | `100.0%` | 130 | 99 | `+75.7s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-15T07:00:19.239000+00:00`.*
