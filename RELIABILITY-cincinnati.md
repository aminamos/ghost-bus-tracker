# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southwest Ohio Regional Transit Authority** in **Cincinnati, OH** (Cincinnati Metropolitan Area, Ohio).
> **Transit System:** Cincinnati | **Location:** Cincinnati, OH | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:17:44.824000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`2.81%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`83.46%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `392` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `214` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `11` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+135.3s` (`+2.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 318 | 81.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 5 | 1.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 53 | 13.5% |
| 🔴 **Severe Delay** | Over 15m late | 5 | 1.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 11 | 2.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 49** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `+1.0 min` |
| **Route 77** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+8.0 min` |
| **Route 71** | 5 | 3 | 1 | **`20.0%`** | `50.0%` | `+5.0 min` |
| **Route 20** | 8 | 5 | 1 | **`12.5%`** | `85.71%` | `+3.7 min` |
| **Route 78** | 18 | 10 | 2 | **`11.11%`** | `75.0%` | `+4.3 min` |
| **Route 27** | 9 | 6 | 1 | **`11.11%`** | `100.0%` | `+0.9 min` |
| **Route 16** | 11 | 6 | 1 | **`9.09%`** | `80.0%` | `+2.7 min` |
| **Route 21** | 13 | 8 | 1 | **`7.69%`** | `83.33%` | `+2.8 min` |
| **Route 19** | 18 | 10 | 1 | **`5.56%`** | `82.35%` | `+3.0 min` |
| **Route 43** | 23 | 14 | 1 | **`4.35%`** | `86.36%` | `+1.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 100** | `+8.5 min (+510.0s)` | `+9.0 min (+540s)` | 2 | `0.0%` |
| **Route 77** | `+8.0 min (+480.0s)` | `+8.0 min (+480s)` | 2 | `0.0%` |
| **Route 46** | `+5.4 min (+322.5s)` | `+21.0 min (+1260s)` | 4 | `75.0%` |
| **Route 71** | `+5.0 min (+300.0s)` | `+9.0 min (+540s)` | 3 | `50.0%` |
| **Route 78** | `+4.3 min (+258.8s)` | `+20.0 min (+1200s)` | 10 | `75.0%` |
| **Route 32** | `+4.0 min (+240.0s)` | `+14.0 min (+840s)` | 6 | `66.67%` |
| **Route 4** | `+3.8 min (+228.8s)` | `+11.0 min (+660s)` | 9 | `68.75%` |
| **Route 20** | `+3.7 min (+222.9s)` | `+6.0 min (+360s)` | 5 | `85.71%` |
| **Route 10** | `+3.5 min (+207.3s)` | `+18.0 min (+1080s)` | 7 | `63.64%` |
| **Route 64** | `+3.4 min (+204.0s)` | `+8.0 min (+480s)` | 6 | `70.0%` |

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
| `2027125` | Route 49 | `N/A` | `SCHEDULED` | Assigned vehicle 2278 is broadcasting off-schedule with no vehicle covering 2027125 |
| `2027451` | Route 16 | `N/A` | `SCHEDULED` | Assigned vehicle 2281 is broadcasting off-schedule with no vehicle covering 2027451 |
| `2057551` | Route 71 | `N/A` | `SCHEDULED` | Assigned vehicle 2307 is broadcasting off-schedule with no vehicle covering 2057551 |
| `2027753` | Route 27 | `N/A` | `SCHEDULED` | Assigned vehicle 2322 is broadcasting off-schedule with no vehicle covering 2027753 |
| `2061862` | Route 77 | `N/A` | `SCHEDULED` | Assigned vehicle 2344 is broadcasting off-schedule with no vehicle covering 2061862 |
| `2030150` | Route 43 | `N/A` | `SCHEDULED` | Assigned vehicle 2425 is broadcasting off-schedule with no vehicle covering 2030150 |
| `2027973` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 2449 is broadcasting off-schedule with no vehicle covering 2027973 |
| `2026798` | Route 21 | `N/A` | `SCHEDULED` | Assigned vehicle 2474 is broadcasting off-schedule with no vehicle covering 2026798 |
| `2027559` | Route 20 | `N/A` | `SCHEDULED` | Assigned vehicle 2507 is broadcasting off-schedule with no vehicle covering 2027559 |
| `2029465` | Route 78 | `N/A` | `SCHEDULED` | Assigned vehicle 2511 is broadcasting off-schedule with no vehicle covering 2029465 |
| `2029463` | Route 78 | `N/A` | `SCHEDULED` | Assigned vehicle 2514 is broadcasting off-schedule with no vehicle covering 2029463 |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:44.824000+00:00`.*
