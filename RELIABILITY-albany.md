# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital District Transportation Authority** in **Albany, NY** (Capital District, New York).
> **Transit System:** CDTA | **Location:** Albany, NY | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-30T04:30:18.083000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `25` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `15` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `4` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 4 | 16.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 1** | 6 | 2 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 905** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 922** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 910** | 6 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 452** | 3 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `13984556-OCT26-SchRMB-Weekday-10` | Route 905 | `00:46:00` | `SCHEDULED` | Assigned vehicle 5532 is missing from active GPS transponder fleet |
| `13998392-OCT26-AlbRMB-Weekday-10` | Route 1 | `00:06:00` | `SCHEDULED` | Assigned vehicle 4246 is missing from active GPS transponder fleet |
| `13998358-OCT26-AlbRMB-Weekday-10` | Route 1 | `00:40:00` | `SCHEDULED` | Assigned vehicle 4246 is missing from active GPS transponder fleet |
| `13998707-OCT26-AlbRMB-Weekday-10` | Route 18 | `23:56:00` | `SCHEDULED` | Assigned vehicle 4128 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 04:30:18` | `16.0%` | `0.0%` | 25 | 15 | `+0.0s` |
| `2026-10-30 03:30:18` | `13.16%` | `0.0%` | 76 | 51 | `+0.0s` |
| `2026-10-30 03:00:19` | `11.54%` | `0.0%` | 104 | 59 | `+0.0s` |
| `2026-10-30 02:00:18` | `17.56%` | `0.0%` | 131 | 66 | `+0.0s` |
| `2026-10-30 01:30:19` | `15.0%` | `0.0%` | 140 | 73 | `+0.0s` |
| `2026-10-30 01:00:18` | `21.19%` | `0.0%` | 151 | 78 | `+0.0s` |
| `2026-10-30 00:00:19` | `8.0%` | `0.0%` | 175 | 99 | `+0.0s` |
| `2026-10-29 23:30:19` | `14.21%` | `0.0%` | 190 | 104 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T04:30:18.083000+00:00`.*
