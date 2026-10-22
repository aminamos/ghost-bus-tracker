# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Milwaukee County Transit System** in **Milwaukee, WI** (Milwaukee Metropolitan Area, Wisconsin).
> **Transit System:** Milwaukee | **Location:** Milwaukee, WI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:17:56.205000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`10.71%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`77.14%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `196` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `188` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `21` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+116.3s` (`+1.9 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+57.0s` (`+0.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 135 | 68.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 13 | 6.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 26 | 13.3% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 21 | 10.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 74** | 3 | 2 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 68** | 2 | 2 | 1 | **`50.0%`** | `100.0%` | `-3.0s` |
| **Route 35** | 10 | 7 | 4 | **`40.0%`** | `50.0%` | `+3.6 min` |
| **Route 52** | 3 | 2 | 1 | **`33.33%`** | `50.0%` | `-96.0s` |
| **Route 55** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+0.9 min` |
| **Route 56** | 4 | 3 | 1 | **`25.0%`** | `66.67%` | `+2.1 min` |
| **Route 63** | 4 | 3 | 1 | **`25.0%`** | `33.33%` | `+2.2 min` |
| **Route 76** | 10 | 7 | 2 | **`20.0%`** | `62.5%` | `+3.9 min` |
| **Route 92** | 5 | 4 | 1 | **`20.0%`** | `100.0%` | `+2.7 min` |
| **Route 22** | 5 | 4 | 1 | **`20.0%`** | `100.0%` | `+1.5 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 53** | `+4.3 min (+257.4s)` | `+9.7 min (+583s)` | 3 | `60.0%` |
| **Route RED** | `+4.1 min (+246.1s)` | `+17.1 min (+1026s)` | 7 | `77.78%` |
| **Route 76** | `+3.9 min (+234.5s)` | `+10.3 min (+619s)` | 7 | `62.5%` |
| **Route 35** | `+3.6 min (+214.7s)` | `+10.8 min (+645s)` | 7 | `50.0%` |
| **Route 33** | `+3.3 min (+196.5s)` | `+11.3 min (+678s)` | 2 | `50.0%` |
| **Route 34** | `+3.3 min (+195.6s)` | `+8.7 min (+520s)` | 3 | `80.0%` |
| **Route 40U** | `+3.2 min (+190.0s)` | `+4.0 min (+239s)` | 2 | `100.0%` |
| **Route 66** | `+3.1 min (+185.2s)` | `+10.8 min (+650s)` | 4 | `83.33%` |
| **Route 31** | `+2.9 min (+176.5s)` | `+3.6 min (+219s)` | 2 | `100.0%` |
| **Route 19** | `+2.9 min (+175.0s)` | `+8.1 min (+486s)` | 7 | `55.56%` |

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
| `37802165` | Route 92 | `N/A` | `SCHEDULED` | Assigned vehicle 6309 is missing from active GPS transponder fleet |
| `37804002` | Route 55 | `N/A` | `SCHEDULED` | Assigned vehicle 6021 is broadcasting off-schedule with no vehicle covering 37804002 |
| `37843382` | Route 21 | `N/A` | `SCHEDULED` | Assigned vehicle 5917 is broadcasting off-schedule with no vehicle covering 37843382 |
| `37803575` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 6304 is missing from active GPS transponder fleet |
| `37803576` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 6213 is broadcasting off-schedule with no vehicle covering 37803576 |
| `37842480` | Route 76 | `N/A` | `SCHEDULED` | Assigned vehicle 5805 is missing from active GPS transponder fleet |
| `37806512` | Route 22 | `N/A` | `SCHEDULED` | Assigned vehicle 6407 is broadcasting off-schedule with no vehicle covering 37806512 |
| `37802273` | Route 68 | `N/A` | `SCHEDULED` | Assigned vehicle 6403 is broadcasting off-schedule with no vehicle covering 37802273 |
| `37805831` | Route 74 | `N/A` | `SCHEDULED` | Assigned vehicle 6012 is broadcasting off-schedule with no vehicle covering 37805831 |
| `37803094` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 6318 is missing from active GPS transponder fleet |
| `37842460` | Route 76 | `N/A` | `SCHEDULED` | Assigned vehicle 6310 is broadcasting off-schedule with no vehicle covering 37842460 |
| `37803525` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 5810 is broadcasting off-schedule with no vehicle covering 37803525 |
| `37804871` | Route 63 | `N/A` | `SCHEDULED` | Assigned vehicle 5520 is broadcasting off-schedule with no vehicle covering 37804871 |
| `37805855` | Route 74 | `N/A` | `SCHEDULED` | Assigned vehicle 6022 is broadcasting off-schedule with no vehicle covering 37805855 |
| `37805847` | Route 74 | `N/A` | `SCHEDULED` | Assigned vehicle 6022 is broadcasting off-schedule with no vehicle covering 37805847 |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:56.205000+00:00`.*
