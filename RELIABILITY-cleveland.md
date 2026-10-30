# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-30T07:00:22.157000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.67%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`85.71%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `30` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `173` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-85.3s` (`-1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+13.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 6 | 20.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 3.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 6.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 22** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 10** | 3 | 2 | 0 | **`0.0%`** | `50.0%` | `-451.5s` |
| **Route 41** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+2.8 min` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `-33.0s` |
| **Route 6** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.4 min` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.1 min` |
| **Route 3** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 41** | `+2.8 min (+170.0s)` | `+2.8 min (+170s)` | 1 | `100.0%` |
| **Route 6** | `+1.4 min (+82.0s)` | `+2.2 min (+133s)` | 2 | `100.0%` |
| **Route 51** | `+0.1 min (+5.0s)` | `+0.1 min (+5s)` | 2 | `100.0%` |

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
| `19234615` | Route 14 | `07:43:00` | `SCHEDULED` | Assigned vehicle 4106 is broadcasting off-schedule with no vehicle covering 19234615 |
| `19229211` | Route 22 | `05:40:00` | `SCHEDULED` | Assigned vehicle 4183 is broadcasting off-schedule with no vehicle covering 19229211 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 07:00:22` | `6.67%` | `85.71%` | 30 | 173 | `-85.3s` |
| `2026-10-30 06:30:21` | `6.67%` | `86.36%` | 30 | 176 | `+38.5s` |
| `2026-10-30 06:00:21` | `0.0%` | `68.75%` | 35 | 194 | `+206.6s` |
| `2026-10-30 05:30:21` | `1.92%` | `83.33%` | 52 | 185 | `+200.0s` |
| `2026-10-30 05:00:19` | `1.39%` | `93.55%` | 72 | 190 | `+579.7s` |
| `2026-10-30 04:30:18` | `1.9%` | `76.47%` | 105 | 199 | `+403.9s` |
| `2026-10-30 04:00:20` | `1.55%` | `72.31%` | 129 | 230 | `+476.0s` |
| `2026-10-30 03:30:18` | `2.04%` | `75.64%` | 147 | 234 | `+328.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T07:00:22.157000+00:00`.*
