# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-05T17:57:49.091861+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`18.99%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `158` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `109` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `30` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 30 | 19.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 100511** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route UNKNOWN** | 59 | 32 | 26 | **`44.07%`** | `0.0%` | `+0.0s` |
| **Route 512** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 17 | 17 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 20 | 20 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 6 | 8 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 5 | 8 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 5 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 6 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `851839711` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9673 is broadcasting off-schedule with no vehicle covering 851839711 |
| `3492020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9201 is broadcasting off-schedule with no vehicle covering 3492020 |
| `872393521` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9688 is broadcasting off-schedule with no vehicle covering 872393521 |
| `1618020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9203 is broadcasting off-schedule with no vehicle covering 1618020 |
| `2373020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9217 is broadcasting off-schedule with no vehicle covering 2373020 |
| `3186020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9220 is broadcasting off-schedule with no vehicle covering 3186020 |
| `1292020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9221 is broadcasting off-schedule with no vehicle covering 1292020 |
| `4392020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9734 is broadcasting off-schedule with no vehicle covering 4392020 |
| `851839391` | Route 100511 | `N/A` | `SCHEDULED` | Assigned vehicle 8248834 is missing from active GPS transponder fleet |
| `851839411` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248834 is missing from active GPS transponder fleet |
| `851843971` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 8248838 is missing from active GPS transponder fleet |
| `851843491` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248838 is missing from active GPS transponder fleet |
| `851839601` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248820 is missing from active GPS transponder fleet |
| `16687254__H:121:0:Weekday:1:26SEP:52037:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:1:26SEP:52037:12345 is missing from active GPS transponder fleet |
| `872393531` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248857 is missing from active GPS transponder fleet |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T17:57:49.091861+00:00`.*
