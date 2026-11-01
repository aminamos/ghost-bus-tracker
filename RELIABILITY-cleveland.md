# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:18.373000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`48.15%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`16.67%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `27` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `144` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `13` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-2221.3s` (`-37.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-3523.0s` (`-58.7 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 2 | 7.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 9 | 33.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 3.7% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 13 | 48.1% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 6** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 2 | 2 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 19** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `-4567.0s` |
| **Route 41** | 3 | 1 | 1 | **`33.33%`** | `0.0%` | `-4850.0s` |
| **Route 10** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-3460.5s` |
| **Route 8** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+1.7 min` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `-3540.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 66** | `+119.7 min (+7181.0s)` | `+119.7 min (+7181s)` | 1 | `0.0%` |
| **Route 8** | `+1.7 min (+100.0s)` | `+3.3 min (+198s)` | 1 | `100.0%` |

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
| `19227696` | Route 45 | `06:18:00` | `SCHEDULED` | Assigned vehicle 2456 is broadcasting off-schedule with no vehicle covering 19227696 |
| `19236161` | Route 19 | `26:10:00` | `SCHEDULED` | Assigned vehicle 4101 is missing from active GPS transponder fleet |
| `19236290` | Route 3 | `26:10:00` | `SCHEDULED` | Assigned vehicle 4108 is missing from active GPS transponder fleet |
| `19235523` | Route 9 | `06:26:00` | `SCHEDULED` | Assigned vehicle 4124 is broadcasting off-schedule with no vehicle covering 19235523 |
| `19235670` | Route 14 | `06:45:00` | `SCHEDULED` | Assigned vehicle 4125 is broadcasting off-schedule with no vehicle covering 19235670 |
| `19236072` | Route 6 | `25:40:00` | `SCHEDULED` | Assigned vehicle 4128 is missing from active GPS transponder fleet |
| `19236074` | Route 6 | `26:10:00` | `SCHEDULED` | Assigned vehicle 4134 is missing from active GPS transponder fleet |
| `19227546` | Route 22 | `05:40:00` | `SCHEDULED` | Assigned vehicle 4147 is broadcasting off-schedule with no vehicle covering 19227546 |
| `19227669` | Route 22 | `05:14:00` | `SCHEDULED` | Assigned vehicle 4148 is broadcasting off-schedule with no vehicle covering 19227669 |
| `19235123` | Route 7 | `07:17:00` | `SCHEDULED` | Assigned vehicle 4187 is broadcasting off-schedule with no vehicle covering 19235123 |
| `19235275` | Route 1 | `26:12:00` | `SCHEDULED` | Assigned vehicle 4188 is missing from active GPS transponder fleet |
| `19235906` | Route 41 | `25:29:00` | `SCHEDULED` | Assigned vehicle 4259 is missing from active GPS transponder fleet |
| `19236565` | Route 28 | `26:20:00` | `SCHEDULED` | Assigned vehicle 4263 is missing from active GPS transponder fleet |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:18` | `48.15%` | `16.67%` | 27 | 144 | `-2221.3s` |
| `2026-11-01 06:30:18` | `13.33%` | `9.52%` | 30 | 146 | `-2710.4s` |
| `2026-11-01 06:00:19` | `4.65%` | `88.0%` | 43 | 131 | `+261.5s` |
| `2026-11-01 05:30:18` | `0.0%` | `86.21%` | 47 | 131 | `+360.4s` |
| `2026-11-01 05:00:19` | `1.56%` | `86.21%` | 64 | 144 | `+245.8s` |
| `2026-11-01 04:30:19` | `5.68%` | `73.21%` | 88 | 149 | `+342.0s` |
| `2026-11-01 04:00:18` | `0.85%` | `67.69%` | 118 | 157 | `+285.0s` |
| `2026-11-01 03:30:18` | `1.5%` | `80.0%` | 133 | 170 | `+196.3s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:18.373000+00:00`.*
