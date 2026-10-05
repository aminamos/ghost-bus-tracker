# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **King County Metro / Sound Transit** in **Seattle, WA** (Central Puget Sound Region, Washington).
> **Transit System:** Sound Transit & KCM | **Location:** Seattle, WA | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-05T18:02:19.723953+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`21.43%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `168` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `113` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `36` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 36 | 21.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route UNKNOWN** | 64 | 33 | 31 | **`48.44%`** | `0.0%` | `+0.0s` |
| **Route 512** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 100511** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 100232** | 9 | 6 | 2 | **`22.22%`** | `0.0%` | `+0.0s` |
| **Route 2LINE** | 17 | 17 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100479** | 19 | 19 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 594** | 6 | 8 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 574** | 6 | 9 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 560** | 4 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 100451** | 8 | 7 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `2752020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41604 is broadcasting off-schedule with no vehicle covering 2752020 |
| `4296020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 41604 is broadcasting off-schedule with no vehicle covering 4296020 |
| `3492020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9201 is broadcasting off-schedule with no vehicle covering 3492020 |
| `851843461` | Route 100232 | `N/A` | `SCHEDULED` | Assigned vehicle 9686 is missing from active GPS transponder fleet |
| `1618020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9203 is broadcasting off-schedule with no vehicle covering 1618020 |
| `2373020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9217 is broadcasting off-schedule with no vehicle covering 2373020 |
| `3186020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9220 is broadcasting off-schedule with no vehicle covering 3186020 |
| `4392020` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 9734 is broadcasting off-schedule with no vehicle covering 4392020 |
| `851839391` | Route 100511 | `N/A` | `SCHEDULED` | Assigned vehicle 8248834 is missing from active GPS transponder fleet |
| `851839411` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248834 is missing from active GPS transponder fleet |
| `851843491` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248838 is missing from active GPS transponder fleet |
| `851839601` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248820 is missing from active GPS transponder fleet |
| `851839621` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248820 is missing from active GPS transponder fleet |
| `16687254__H:121:0:Weekday:1:26SEP:52037:12345` | Route 512 | `N/A` | `SCHEDULED` | Assigned vehicle H:121:0:Weekday:1:26SEP:52037:12345 is missing from active GPS transponder fleet |
| `872393531` | Route UNKNOWN | `N/A` | `SCHEDULED` | Assigned vehicle 8248857 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 18:02:19` | `21.43%` | `0.0%` | 168 | 113 | `+0.0s` |
| `2026-10-05 17:57:49` | `18.99%` | `0.0%` | 158 | 109 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T18:02:19.723953+00:00`.*
