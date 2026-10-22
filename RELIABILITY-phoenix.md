# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Phoenix | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:17:41.230000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`3.3%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`77.59%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `637` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `585` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `21` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+210.5s` (`+3.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+116.0s` (`+1.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 471 | 73.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 29 | 4.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 86 | 13.5% |
| 🔴 **Severe Delay** | Over 15m late | 21 | 3.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 21 | 3.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 8 | 1.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 56** | 7 | 4 | 2 | **`28.57%`** | `33.33%` | `+6.1 min` |
| **Route 170** | 8 | 7 | 2 | **`25.0%`** | `83.33%` | `+2.2 min` |
| **Route 28** | 4 | 2 | 1 | **`25.0%`** | `66.67%` | `-44.0s` |
| **Route 15** | 4 | 3 | 1 | **`25.0%`** | `33.33%` | `+0.5 min` |
| **Route 66** | 5 | 4 | 1 | **`20.0%`** | `75.0%` | `+4.6 min` |
| **Route 48** | 6 | 5 | 1 | **`16.67%`** | `60.0%` | `+4.5 min` |
| **Route 43** | 6 | 6 | 1 | **`16.67%`** | `80.0%` | `+1.8 min` |
| **Route 3** | 15 | 14 | 2 | **`13.33%`** | `84.62%` | `+3.1 min` |
| **Route DASH** | 8 | 4 | 1 | **`12.5%`** | `85.71%` | `+1.5 min` |
| **Route 19** | 18 | 17 | 2 | **`11.11%`** | `68.75%` | `+2.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 7** | `+12.4 min (+744.6s)` | `+89.3 min (+5358s)` | 15 | `62.5%` |
| **Route 41** | `+9.9 min (+596.0s)` | `+74.9 min (+4495s)` | 14 | `53.33%` |
| **Route 27** | `+9.8 min (+589.4s)` | `+56.8 min (+3406s)` | 8 | `62.5%` |
| **Route 77** | `+8.8 min (+525.1s)` | `+68.8 min (+4128s)` | 9 | `62.5%` |
| **Route 122** | `+6.7 min (+403.6s)` | `+28.4 min (+1707s)` | 3 | `80.0%` |
| **Route VENU** | `+6.1 min (+364.4s)` | `+42.6 min (+2554s)` | 6 | `80.0%` |
| **Route 56** | `+6.1 min (+363.3s)` | `+9.7 min (+580s)` | 4 | `33.33%` |
| **Route MARY** | `+5.9 min (+355.0s)` | `+12.0 min (+718s)` | 4 | `60.0%` |
| **Route 51** | `+5.7 min (+340.0s)` | `+18.7 min (+1122s)` | 6 | `66.67%` |
| **Route 32** | `+5.6 min (+338.4s)` | `+14.6 min (+877s)` | 4 | `60.0%` |

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
| `24161859` | Route 66 | `N/A` | `SCHEDULED` | Assigned vehicle 2511 is broadcasting off-schedule with no vehicle covering 24161859 |
| `24270575` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 8096 is broadcasting off-schedule with no vehicle covering 24270575 |
| `24270594` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 8092 is broadcasting off-schedule with no vehicle covering 24270594 |
| `24270106` | Route 170 | `N/A` | `SCHEDULED` | Assigned vehicle 5281 is broadcasting off-schedule with no vehicle covering 24270106 |
| `24271675` | Route 70 | `N/A` | `SCHEDULED` | Assigned vehicle 5703 is broadcasting off-schedule with no vehicle covering 24271675 |
| `24286737` | Route 3 | `N/A` | `SCHEDULED` | Assigned vehicle 8127 is broadcasting off-schedule with no vehicle covering 24286737 |
| `24270389` | Route 28 | `N/A` | `SCHEDULED` | Assigned vehicle 5205 is missing from active GPS transponder fleet |
| `24161390` | Route 56 | `N/A` | `SCHEDULED` | Assigned vehicle 6738 is broadcasting off-schedule with no vehicle covering 24161390 |
| `24271758` | Route 70 | `N/A` | `SCHEDULED` | Assigned vehicle 5162 is broadcasting off-schedule with no vehicle covering 24271758 |
| `24161376` | Route 45 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `24162680` | Route 77 | `N/A` | `SCHEDULED` | Assigned vehicle 6820 is broadcasting off-schedule with no vehicle covering 24162680 |
| `24270094` | Route 170 | `N/A` | `SCHEDULED` | Assigned vehicle 5660 is broadcasting off-schedule with no vehicle covering 24270094 |
| `24286673` | Route 3 | `N/A` | `SCHEDULED` | Assigned vehicle 5350 is broadcasting off-schedule with no vehicle covering 24286673 |
| `24285712` | Route 43 | `N/A` | `SCHEDULED` | Assigned vehicle 8141 is broadcasting off-schedule with no vehicle covering 24285712 |
| `24271344` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 8145 is broadcasting off-schedule with no vehicle covering 24271344 |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:41.230000+00:00`.*
