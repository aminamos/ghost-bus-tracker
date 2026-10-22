# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Barrie Transit** in **Barrie, ON** (City of Barrie, Ontario).
> **Transit System:** Barrie | **Location:** Barrie, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:17:57.920000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.19%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`98.45%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `139` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `30` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `10` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+22.1s` (`+0.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+4.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 127 | 91.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 1.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 10 | 7.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 100** | 11 | 1 | 6 | **`54.55%`** | `80.0%` | `+2.1 min` |
| **Route 7B** | 10 | 4 | 2 | **`20.0%`** | `100.0%` | `+0.1 min` |
| **Route 7A** | 8 | 4 | 1 | **`12.5%`** | `100.0%` | `+0.3 min` |
| **Route 8A** | 18 | 5 | 1 | **`5.56%`** | `100.0%` | `+0.3 min` |
| **Route 10** | 10 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.0 min` |
| **Route 11** | 10 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 8B** | 21 | 5 | 0 | **`0.0%`** | `100.0%` | `+0.4 min` |
| **Route 12A** | 8 | 4 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 101** | 10 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 2B** | 8 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 100** | `+2.1 min (+124.4s)` | `+8.1 min (+486s)` | 1 | `80.0%` |
| **Route 400** | `+0.8 min (+45.4s)` | `+6.0 min (+362s)` | 2 | `90.0%` |
| **Route 12B** | `+0.4 min (+26.0s)` | `+1.1 min (+66s)` | 4 | `100.0%` |
| **Route 8B** | `+0.4 min (+24.3s)` | `+3.7 min (+222s)` | 5 | `100.0%` |
| **Route 8A** | `+0.3 min (+20.5s)` | `+1.9 min (+113s)` | 5 | `100.0%` |
| **Route 2B** | `+0.3 min (+18.8s)` | `+0.6 min (+37s)` | 3 | `100.0%` |
| **Route 2A** | `+0.3 min (+17.3s)` | `+1.3 min (+79s)` | 3 | `100.0%` |
| **Route 7A** | `+0.3 min (+16.3s)` | `+1.3 min (+77s)` | 4 | `100.0%` |
| **Route 101** | `+0.2 min (+11.4s)` | `+0.6 min (+36s)` | 2 | `100.0%` |
| **Route 11** | `+0.1 min (+9.0s)` | `+1.2 min (+75s)` | 2 | `100.0%` |

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
| `9c4c083b-e38e-4842-be32-829c6f30cf6f` | Route 7B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `97e05a3b-9582-42a5-9c17-5af0453d6b6a` | Route 7B | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3629425e-8f8e-4379-9cfa-4ef86996162c` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1c543ca1-ae6d-4aa5-9f97-ba9deda3284c` | Route 7A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `55f14963-8bb2-4c1e-af30-60502c2ba338` | Route 8A | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `3d4d4482-4403-4889-9ceb-248616e69ae1` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `a2278fcc-02f3-4f05-86e2-c603aa4e8ead` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `694fae44-5829-4b9e-8d81-1dac2a8fbd0c` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `308f8d80-d89d-48b3-990e-37b09e2c7a02` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `b00011c3-4e78-4ad3-abe1-6782941c17d5` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:57.920000+00:00`.*
