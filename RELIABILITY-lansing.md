# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Capital Area Transportation Authority** in **Lansing, MI** (Lansing Metropolitan Area, Michigan).
> **Transit System:** CATA | **Location:** Lansing, MI | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-25T07:00:18.553000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.07%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`72.73%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `99` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `59` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+108.3s` (`+1.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+68.0s` (`+1.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 64 | 64.6% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 13 | 13.1% |
| 🟡 **Minor Delay** | +5m to +15m late | 10 | 10.1% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 1.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 7.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 12598** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+0.5 min` |
| **Route 12596** | 5 | 3 | 1 | **`20.0%`** | `75.0%` | `+2.5 min` |
| **Route 12607** | 5 | 2 | 1 | **`20.0%`** | `100.0%` | `+0.5 min` |
| **Route 12599** | 7 | 4 | 1 | **`14.29%`** | `83.33%` | `+3.0 min` |
| **Route 12593** | 12 | 7 | 1 | **`8.33%`** | `66.67%` | `+1.2 min` |
| **Route 12612** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.0 min` |
| **Route 12610** | 4 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.6 min` |
| **Route 12611** | 4 | 2 | 0 | **`0.0%`** | `50.0%` | `+7.0 min` |
| **Route 12609** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 12617** | 3 | 2 | 0 | **`0.0%`** | `33.33%` | `+3.8 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 12622** | `+10.6 min (+633.5s)` | `+10.7 min (+641s)` | 1 | `0.0%` |
| **Route 12611** | `+7.0 min (+417.8s)` | `+15.7 min (+941s)` | 2 | `50.0%` |
| **Route 12618** | `+4.4 min (+261.3s)` | `+8.8 min (+526s)` | 3 | `66.67%` |
| **Route 12617** | `+3.8 min (+228.0s)` | `+14.2 min (+854s)` | 2 | `33.33%` |
| **Route 12605** | `+3.5 min (+208.5s)` | `+5.3 min (+317s)` | 1 | `50.0%` |
| **Route 12599** | `+3.0 min (+178.8s)` | `+6.0 min (+360s)` | 4 | `83.33%` |
| **Route 12601** | `+2.9 min (+173.0s)` | `+3.1 min (+188s)` | 1 | `100.0%` |
| **Route 12606** | `+2.5 min (+150.0s)` | `+2.5 min (+150s)` | 2 | `100.0%` |
| **Route 12596** | `+2.5 min (+148.0s)` | `+5.3 min (+320s)` | 3 | `75.0%` |
| **Route 12612** | `+2.0 min (+118.5s)` | `+2.4 min (+142s)` | 2 | `100.0%` |

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
| `4334141` | Route 12596 | `N/A` | `SCHEDULED` | Assigned vehicle 2625 is broadcasting off-schedule with no vehicle covering 4334141 |
| `4337711` | Route 12608 | `N/A` | `SCHEDULED` | Assigned vehicle 2626 is broadcasting off-schedule with no vehicle covering 4337711 |
| `4334838` | Route 12598 | `N/A` | `SCHEDULED` | Assigned vehicle 2702 is broadcasting off-schedule with no vehicle covering 4334838 |
| `4332560` | Route 12593 | `N/A` | `SCHEDULED` | Assigned vehicle 2731 is broadcasting off-schedule with no vehicle covering 4332560 |
| `4336400` | Route 12603 | `N/A` | `SCHEDULED` | Assigned vehicle 2739 is broadcasting off-schedule with no vehicle covering 4336400 |
| `4335066` | Route 12599 | `N/A` | `SCHEDULED` | Assigned vehicle 2742 is broadcasting off-schedule with no vehicle covering 4335066 |
| `4337312` | Route 12607 | `N/A` | `SCHEDULED` | Assigned vehicle 26001 is broadcasting off-schedule with no vehicle covering 4337312 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-25 07:00:18` | `7.07%` | `72.73%` | 99 | 59 | `+108.3s` |
| `2026-11-25 06:30:18` | `7.07%` | `72.73%` | 99 | 59 | `+108.3s` |
| `2026-11-25 06:00:18` | `7.07%` | `72.73%` | 99 | 59 | `+108.3s` |
| `2026-11-25 05:30:18` | `7.07%` | `72.73%` | 99 | 59 | `+108.3s` |
| `2026-11-25 05:00:17` | `7.07%` | `72.73%` | 99 | 59 | `+108.3s` |
| `2026-11-25 04:30:17` | `7.07%` | `72.73%` | 99 | 59 | `+108.3s` |
| `2026-11-25 04:00:18` | `7.07%` | `72.73%` | 99 | 59 | `+108.3s` |
| `2026-11-25 03:30:19` | `7.07%` | `72.73%` | 99 | 59 | `+108.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-25T07:00:18.553000+00:00`.*
