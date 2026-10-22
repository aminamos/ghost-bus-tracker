# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital District Transportation Authority** in **Albany, NY** (Capital District, New York).
> **Transit System:** Albany | **Location:** Albany, NY | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:17:42.860000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`13.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `301` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `161` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `40` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 40 | 13.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 810** | 3 | 0 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 540** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 107** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 286** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 233** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 802** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 214** | 6 | 3 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 18** | 6 | 2 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 737** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 605** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `14000583-OCT26-AlbRMB-Weekday-10` | Route 370 | `15:30:00` | `SCHEDULED` | Assigned vehicle 4197 is missing from active GPS transponder fleet |
| `13985350-OCT26-TroyRMB-Weekday-10` | Route 87 | `16:10:00` | `SCHEDULED` | Assigned vehicle 4259 is missing from active GPS transponder fleet |
| `13998846-OCT26-AlbRMB-Weekday-10` | Route 233 | `15:58:00` | `SCHEDULED` | Assigned vehicle 4194 is missing from active GPS transponder fleet |
| `13998490-OCT26-AlbRMB-Weekday-10` | Route 737 | `15:41:00` | `SCHEDULED` | Assigned vehicle 4122 is missing from active GPS transponder fleet |
| `14025854-OCT26-NX-Weekday-01` | Route 540 | `15:42:00` | `SCHEDULED` | Assigned vehicle 341 is missing from active GPS transponder fleet |
| `13985105-OCT26-TroyRMB-Weekday-10` | Route 802 | `15:25:00` | `SCHEDULED` | Assigned vehicle 4260 is missing from active GPS transponder fleet |
| `13984187-OCT26-SchRMB-Weekday-10` | Route 810 | `15:37:00` | `SCHEDULED` | Assigned vehicle 4251 is missing from active GPS transponder fleet |
| `13998377-OCT26-AlbRMB-Weekday-10` | Route 1 | `16:14:00` | `SCHEDULED` | Assigned vehicle 4196 is broadcasting off-schedule with no vehicle covering 13998377-OCT26-AlbRMB-Weekday-10 |
| `13998372-OCT26-AlbRMB-Weekday-10` | Route 1 | `15:14:00` | `SCHEDULED` | Assigned vehicle 4250 is broadcasting off-schedule with no vehicle covering 13998372-OCT26-AlbRMB-Weekday-10 |
| `13998759-OCT26-AlbRMB-Weekday-10` | Route 100 | `14:32:00` | `SCHEDULED` | Assigned vehicle 1904 is missing from active GPS transponder fleet |
| `13998637-OCT26-AlbRMB-Weekday-10` | Route 100 | `15:39:00` | `SCHEDULED` | Assigned vehicle 1904 is missing from active GPS transponder fleet |
| `13984507-OCT26-SchRMB-Weekday-10` | Route 905 | `15:17:00` | `SCHEDULED` | Assigned vehicle 5518 is missing from active GPS transponder fleet |
| `13998443-OCT26-AlbRMB-Weekday-10` | Route 214 | `15:36:00` | `SCHEDULED` | Assigned vehicle 4229 is broadcasting off-schedule with no vehicle covering 13998443-OCT26-AlbRMB-Weekday-10 |
| `14025857-OCT26-NX-Weekday-01` | Route 540 | `16:12:00` | `SCHEDULED` | Assigned vehicle 339 is missing from active GPS transponder fleet |
| `13985519-OCT26-TroyRMB-Weekday-10` | Route 922 | `15:25:00` | `SCHEDULED` | Assigned vehicle 2207 is missing from active GPS transponder fleet |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:42.860000+00:00`.*
