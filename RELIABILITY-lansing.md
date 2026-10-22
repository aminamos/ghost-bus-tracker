# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Area Transportation Authority** in **Lansing, MI** (Lansing Metropolitan Area, Michigan).
> **Transit System:** Lansing | **Location:** Lansing, MI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:17:42.996000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`73.63%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `100` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `62` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+168.0s` (`+2.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+118.0s` (`+2.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 67 | 67.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 6 | 6.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 17 | 17.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 7.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 12607** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `+1.9 min` |
| **Route 12605** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+1.6 min` |
| **Route 12593** | 9 | 7 | 2 | **`22.22%`** | `83.33%` | `+1.3 min` |
| **Route 12596** | 5 | 3 | 1 | **`20.0%`** | `25.0%` | `+4.7 min` |
| **Route 12595** | 5 | 3 | 1 | **`20.0%`** | `75.0%` | `-29.5s` |
| **Route 12599** | 6 | 4 | 1 | **`16.67%`** | `80.0%` | `+4.3 min` |
| **Route 12615** | 5 | 4 | 0 | **`0.0%`** | `100.0%` | `+1.5 min` |
| **Route 12600** | 6 | 3 | 0 | **`0.0%`** | `16.67%` | `+7.2 min` |
| **Route 12594** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.9 min` |
| **Route 12612** | 5 | 3 | 0 | **`0.0%`** | `0.0%` | `+7.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 12612** | `+7.9 min (+472.0s)` | `+11.1 min (+667s)` | 3 | `0.0%` |
| **Route 12600** | `+7.2 min (+433.5s)` | `+10.3 min (+617s)` | 3 | `16.67%` |
| **Route 12617** | `+6.7 min (+400.0s)` | `+16.2 min (+973s)` | 2 | `66.67%` |
| **Route 12614** | `+6.2 min (+374.7s)` | `+9.1 min (+548s)` | 3 | `33.33%` |
| **Route 12596** | `+4.7 min (+279.8s)` | `+6.7 min (+403s)` | 3 | `25.0%` |
| **Route 12599** | `+4.3 min (+255.6s)` | `+11.0 min (+658s)` | 4 | `80.0%` |
| **Route 12603** | `+4.0 min (+240.2s)` | `+7.7 min (+460s)` | 2 | `75.0%` |
| **Route 12606** | `+3.3 min (+198.0s)` | `+4.1 min (+244s)` | 2 | `100.0%` |
| **Route 12601** | `+3.1 min (+185.0s)` | `+4.3 min (+258s)` | 2 | `100.0%` |
| **Route 12622** | `+2.6 min (+156.0s)` | `+2.6 min (+156s)` | 1 | `100.0%` |

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
| `4334468` | Route 12596 | `N/A` | `SCHEDULED` | Assigned vehicle 2599 is broadcasting off-schedule with no vehicle covering 4334468 |
| `4336999` | Route 12605 | `N/A` | `SCHEDULED` | Assigned vehicle 2600 is broadcasting off-schedule with no vehicle covering 4336999 |
| `4335269` | Route 12599 | `N/A` | `SCHEDULED` | Assigned vehicle 2607 is broadcasting off-schedule with no vehicle covering 4335269 |
| `4332956` | Route 12593 | `N/A` | `SCHEDULED` | Assigned vehicle 2608 is broadcasting off-schedule with no vehicle covering 4332956 |
| `4332891` | Route 12593 | `N/A` | `SCHEDULED` | Assigned vehicle 2701 is broadcasting off-schedule with no vehicle covering 4332891 |
| `4333916` | Route 12595 | `N/A` | `SCHEDULED` | Assigned vehicle 2711 is broadcasting off-schedule with no vehicle covering 4333916 |
| `4337495` | Route 12607 | `N/A` | `SCHEDULED` | Assigned vehicle 2728 is broadcasting off-schedule with no vehicle covering 4337495 |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:42.996000+00:00`.*
