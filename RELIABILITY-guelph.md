# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Guelph Transit** in **Guelph, ON** (City of Guelph, Ontario).
> **Transit System:** Guelph | **Location:** Guelph, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:50.040000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`50.51%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `392` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `40` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `198` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 198 | 50.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 124 | 31.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 3014** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 3005** | 20 | 1 | 19 | **`95.0%`** | `0.0%` | `+0.0s` |
| **Route 2997** | 20 | 1 | 19 | **`95.0%`** | `0.0%` | `+0.0s` |
| **Route 2992** | 23 | 1 | 21 | **`91.3%`** | `0.0%` | `+0.0s` |
| **Route 2991** | 20 | 1 | 18 | **`90.0%`** | `0.0%` | `+0.0s` |
| **Route 3002** | 22 | 2 | 19 | **`86.36%`** | `0.0%` | `+0.0s` |
| **Route 3003** | 21 | 2 | 18 | **`85.71%`** | `0.0%` | `+0.0s` |
| **Route 3013** | 25 | 2 | 21 | **`84.0%`** | `0.0%` | `+0.0s` |
| **Route 3001** | 27 | 1 | 14 | **`51.85%`** | `0.0%` | `+0.0s` |
| **Route 2998** | 26 | 1 | 12 | **`46.15%`** | `0.0%` | `+0.0s` |

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
| `481509` | Route 3002 | `24:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480259` | Route 2997 | `24:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481507` | Route 3002 | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480257` | Route 2997 | `23:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481505` | Route 3002 | `22:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480255` | Route 2997 | `22:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481290` | Route 3001 | `24:11:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `481287` | Route 3001 | `22:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `480480` | Route 2998 | `23:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484108` | Route 3014 | `15:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484068` | Route 3014 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484109` | Route 3014 | `15:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484067` | Route 3014 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484110` | Route 3014 | `16:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `484066` | Route 3014 | `16:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:50.040000+00:00`.*
