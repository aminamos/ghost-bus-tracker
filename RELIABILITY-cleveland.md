# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-26T07:00:21.026000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`83.33%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `35` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `183` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `4` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-236.8s` (`-3.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+65.5s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 5 | 14.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 2.9% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 4 | 11.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 41** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.9 min` |
| **Route 22** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 26** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.4 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.2 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+4.0 min` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `-1980.0s` |
| **Route 3** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 10** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 6** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `-15.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 1** | `+4.0 min (+240.0s)` | `+4.0 min (+240s)` | 1 | `100.0%` |
| **Route 26** | `+3.4 min (+203.0s)` | `+3.4 min (+203s)` | 2 | `100.0%` |
| **Route 41** | `+1.9 min (+117.0s)` | `+1.9 min (+117s)` | 1 | `100.0%` |
| **Route 28** | `+0.2 min (+14.0s)` | `+0.2 min (+14s)` | 1 | `100.0%` |

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
| `19237116` | Route 8 | `07:12:00` | `SCHEDULED` | Assigned vehicle 4120 is broadcasting off-schedule with no vehicle covering 19237116 |
| `19237024` | Route 48 | `07:22:00` | `SCHEDULED` | Assigned vehicle 4189 is broadcasting off-schedule with no vehicle covering 19237024 |
| `19226563` | Route 25 | `09:18:00` | `SCHEDULED` | Assigned vehicle 4235 is broadcasting off-schedule with no vehicle covering 19226563 |
| `19237283` | Route 14 | `06:45:00` | `SCHEDULED` | Assigned vehicle 4262 is broadcasting off-schedule with no vehicle covering 19237283 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-26 07:00:21` | `11.43%` | `83.33%` | 35 | 183 | `-236.8s` |
| `2026-10-26 06:30:39` | `0.0%` | `72.73%` | 28 | 162 | `+104.6s` |
| `2026-10-26 05:30:22` | `2.08%` | `84.62%` | 48 | 175 | `+127.9s` |
| `2026-10-26 05:00:24` | `3.23%` | `84.0%` | 62 | 183 | `+102.9s` |
| `2026-10-26 04:30:36` | `2.22%` | `79.63%` | 90 | 183 | `+132.9s` |
| `2026-10-26 04:00:19` | `0.89%` | `86.27%` | 112 | 201 | `+156.1s` |
| `2026-10-26 03:30:35` | `0.71%` | `80.0%` | 140 | 200 | `+172.8s` |
| `2026-10-26 01:00:27` | `0.52%` | `65.17%` | 193 | 201 | `+394.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-26T07:00:21.026000+00:00`.*
