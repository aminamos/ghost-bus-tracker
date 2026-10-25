# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-25T06:15:46.670000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`3.7%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`85.71%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `27` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `158` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+171.4s` (`+2.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+102.0s` (`+1.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 12 | 44.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 7.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 3.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 22** | 2 | 2 | 1 | **`50.0%`** | `100.0%` | `+1.6 min` |
| **Route 25** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.5 min` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.9 min` |
| **Route 19** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.6 min` |
| **Route 41** | 4 | 3 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 6** | 3 | 2 | 0 | **`0.0%`** | `50.0%` | `+4.7 min` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+4.6 min` |
| **Route 51** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 48** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 14** | `+4.9 min (+292.5s)` | `+9.1 min (+547s)` | 2 | `50.0%` |
| **Route 6** | `+4.7 min (+283.0s)` | `+5.6 min (+338s)` | 2 | `50.0%` |
| **Route 26** | `+4.6 min (+278.0s)` | `+4.6 min (+278s)` | 2 | `100.0%` |
| **Route 25** | `+4.5 min (+269.0s)` | `+4.5 min (+269s)` | 2 | `100.0%` |
| **Route 1** | `+2.6 min (+156.0s)` | `+2.6 min (+156s)` | 1 | `100.0%` |
| **Route 3** | `+1.6 min (+98.0s)` | `+1.6 min (+98s)` | 1 | `100.0%` |
| **Route 22** | `+1.6 min (+97.0s)` | `+1.6 min (+97s)` | 2 | `100.0%` |
| **Route 19** | `+1.6 min (+96.0s)` | `+1.6 min (+96s)` | 2 | `100.0%` |
| **Route 41** | `+1.5 min (+92.0s)` | `+1.8 min (+106s)` | 3 | `100.0%` |
| **Route 51** | `+0.6 min (+35.0s)` | `+0.6 min (+35s)` | 1 | `100.0%` |

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
| `19227669` | Route 22 | `05:14:00` | `SCHEDULED` | Assigned vehicle 4153 is broadcasting off-schedule with no vehicle covering 19227669 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:46` | `3.7%` | `85.71%` | 27 | 158 | `+171.4s` |
| `2026-10-25 06:00:57` | `3.03%` | `92.31%` | 33 | 159 | `+79.8s` |
| `2026-10-25 05:30:21` | `0.0%` | `82.14%` | 48 | 150 | `+136.8s` |
| `2026-10-25 05:00:21` | `1.54%` | `71.43%` | 65 | 159 | `+181.1s` |
| `2026-10-25 04:33:54` | `3.49%` | `83.33%` | 86 | 150 | `+173.1s` |
| `2026-10-25 03:30:19` | `0.0%` | `68.75%` | 143 | 170 | `+261.9s` |
| `2026-10-25 03:00:20` | `0.61%` | `65.82%` | 164 | 179 | `+269.8s` |
| `2026-10-25 02:30:19` | `0.0%` | `73.56%` | 177 | 177 | `+273.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:46.670000+00:00`.*
