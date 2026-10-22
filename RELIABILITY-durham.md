# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Durham Region Transit** in **Durham, ON** (Regional Municipality of Durham, Ontario).
> **Transit System:** Durham | **Location:** Durham, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:17:47.822000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`11.24%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`79.07%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `249` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `123` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `28` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+151.7s` (`+2.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 170 | 68.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 3 | 1.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 32 | 12.9% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 4.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 28 | 11.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 2 | 0.8% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 319** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.3 min` |
| **Route 502** | 8 | 3 | 3 | **`37.5%`** | `100.0%` | `+0.1 min` |
| **Route 118** | 6 | 4 | 2 | **`33.33%`** | `100.0%` | `+0.2 min` |
| **Route 112** | 6 | 6 | 2 | **`33.33%`** | `100.0%` | `+1.5 min` |
| **Route 505** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `+0.1 min` |
| **Route 407** | 7 | 3 | 2 | **`28.57%`** | `0.0%` | `+14.9 min` |
| **Route 302** | 9 | 6 | 2 | **`22.22%`** | `71.43%` | `+3.0 min` |
| **Route 301** | 5 | 2 | 1 | **`20.0%`** | `100.0%` | `+0.7 min` |
| **Route 920** | 12 | 11 | 2 | **`16.67%`** | `60.0%` | `+5.9 min` |
| **Route 905** | 12 | 8 | 2 | **`16.67%`** | `100.0%` | `+1.2 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 407** | `+14.9 min (+896.0s)` | `+16.9 min (+1016s)` | 3 | `0.0%` |
| **Route 902** | `+7.3 min (+440.2s)` | `+25.0 min (+1499s)` | 7 | `40.0%` |
| **Route 900** | `+6.9 min (+415.8s)` | `+26.9 min (+1612s)` | 13 | `52.94%` |
| **Route 920** | `+5.9 min (+355.1s)` | `+16.2 min (+971s)` | 11 | `60.0%` |
| **Route 507** | `+3.9 min (+234.0s)` | `+3.9 min (+234s)` | 1 | `100.0%` |
| **Route 901** | `+3.2 min (+189.8s)` | `+11.4 min (+682s)` | 7 | `56.25%` |
| **Route 302** | `+3.0 min (+179.6s)` | `+9.2 min (+553s)` | 6 | `71.43%` |
| **Route 410** | `+2.4 min (+145.3s)` | `+12.5 min (+750s)` | 4 | `83.33%` |
| **Route 916** | `+2.4 min (+144.8s)` | `+12.9 min (+776s)` | 10 | `81.82%` |
| **Route 421** | `+1.9 min (+115.2s)` | `+5.7 min (+341s)` | 4 | `75.0%` |

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
| `1355__401044_Timetable_-_2026-10` | Route 920 | `N/A` | `SCHEDULED` | Assigned vehicle 8529 is broadcasting off-schedule with no vehicle covering 1355__401044_Timetable_-_2026-10 |
| `1354__401063_Timetable_-_2026-10` | Route 920 | `N/A` | `SCHEDULED` | Assigned vehicle 8471 is broadcasting off-schedule with no vehicle covering 1354__401063_Timetable_-_2026-10 |
| `5876__201045_Timetable_-_2026-10` | Route 302 | `N/A` | `SCHEDULED` | Assigned vehicle 8625 is missing from active GPS transponder fleet |
| `171__401053_Timetable_-_2026-10` | Route 407 | `N/A` | `SCHEDULED` | Assigned vehicle 6112 is broadcasting off-schedule with no vehicle covering 171__401053_Timetable_-_2026-10 |
| `173__401053_Timetable_-_2026-10` | Route 407 | `N/A` | `SCHEDULED` | Assigned vehicle 6112 is broadcasting off-schedule with no vehicle covering 173__401053_Timetable_-_2026-10 |
| `1241__401039_Timetable_-_2026-10` | Route 502 | `N/A` | `SCHEDULED` | Assigned vehicle 6137 is broadcasting off-schedule with no vehicle covering 1241__401039_Timetable_-_2026-10 |
| `1116__201075_Timetable_-_2026-10` | Route 301 | `N/A` | `SCHEDULED` | Assigned vehicle 8506 is broadcasting off-schedule with no vehicle covering 1116__201075_Timetable_-_2026-10 |
| `1825__201086_Timetable_-_2026-10` | Route 112 | `N/A` | `SCHEDULED` | Assigned vehicle 7104 is broadcasting off-schedule with no vehicle covering 1825__201086_Timetable_-_2026-10 |
| `575__201075_Timetable_-_2026-10` | Route 319 | `N/A` | `SCHEDULED` | Assigned vehicle 8506 is broadcasting off-schedule with no vehicle covering 575__201075_Timetable_-_2026-10 |
| `1885__201010_Timetable_-_2026-10` | Route 905 | `N/A` | `SCHEDULED` | Assigned vehicle 7105 is broadcasting off-schedule with no vehicle covering 1885__201010_Timetable_-_2026-10 |
| `589__201075_Timetable_-_2026-10` | Route 319 | `N/A` | `SCHEDULED` | Assigned vehicle 8506 is broadcasting off-schedule with no vehicle covering 589__201075_Timetable_-_2026-10 |
| `5617__201074_Timetable_-_2026-10` | Route 915 | `N/A` | `SCHEDULED` | Assigned vehicle 7123 is broadcasting off-schedule with no vehicle covering 5617__201074_Timetable_-_2026-10 |
| `5855__201068_Timetable_-_2026-10` | Route 302 | `N/A` | `SCHEDULED` | Assigned vehicle 8546 is broadcasting off-schedule with no vehicle covering 5855__201068_Timetable_-_2026-10 |
| `5564__201093_Timetable_-_2026-10` | Route 916 | `N/A` | `SCHEDULED` | Assigned vehicle 8527 is broadcasting off-schedule with no vehicle covering 5564__201093_Timetable_-_2026-10 |
| `1769__201036_Timetable_-_2026-10` | Route 118 | `N/A` | `SCHEDULED` | Assigned vehicle 8540 is broadcasting off-schedule with no vehicle covering 1769__201036_Timetable_-_2026-10 |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:47.822000+00:00`.*
