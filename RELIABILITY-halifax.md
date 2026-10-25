# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Halifax Transit** in **Halifax, NS** (Halifax Regional Municipality, Nova Scotia).
> **Transit System:** Halifax Transit | **Location:** Halifax, NS | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-25T07:00:33.409000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`100.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `416` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `416` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 416 | 100.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 64 | 0 | 64 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7A** | 51 | 0 | 51 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 21** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 24** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 7B** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 56** | 30 | 0 | 30 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 320** | 24 | 1 | 24 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9B** | 19 | 0 | 19 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 9A** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `4653722` | Route 320 | `06:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653742` | Route 320 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653724` | Route 320 | `08:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653744` | Route 320 | `09:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653726` | Route 320 | `10:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653746` | Route 320 | `11:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653728` | Route 320 | `12:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653748` | Route 320 | `13:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653723` | Route 320 | `07:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653743` | Route 320 | `08:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653725` | Route 320 | `09:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653745` | Route 320 | `10:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653727` | Route 320 | `11:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653747` | Route 320 | `12:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4653729` | Route 320 | `13:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 07:00:33` | `100.0%` | `0.0%` | 416 | 1 | `+0.0s` |
| `2026-10-25 06:30:33` | `100.0%` | `0.0%` | 416 | 0 | `+0.0s` |
| `2026-10-25 06:15:47` | `100.0%` | `0.0%` | 416 | 0 | `+0.0s` |
| `2026-10-25 06:01:04` | `100.0%` | `0.0%` | 416 | 0 | `+0.0s` |
| `2026-10-25 05:30:22` | `100.0%` | `0.0%` | 416 | 0 | `+0.0s` |
| `2026-10-25 05:00:33` | `0.0%` | `0.0%` | 0 | 0 | `+0.0s` |
| `2026-10-25 04:33:57` | `0.0%` | `100.0%` | 2 | 2 | `-32.0s` |
| `2026-10-25 04:00:35` | `12.5%` | `54.55%` | 16 | 13 | `+386.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T07:00:33.409000+00:00`.*
