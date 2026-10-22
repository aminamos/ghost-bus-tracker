# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Central Florida Regional Transportation Authority** in **Orlando, FL** (Orlando Metropolitan Area, Florida).
> **Transit System:** Orlando | **Location:** Orlando, FL | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:17:42.195000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`1.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`71.86%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `201` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `199` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `2` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+228.7s` (`+3.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+139.0s` (`+2.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 143 | 71.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 48 | 23.9% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 3.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 2 | 1.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17634** | 3 | 2 | 1 | **`33.33%`** | `100.0%` | `+0.7 min` |
| **Route 17570** | 6 | 5 | 1 | **`16.67%`** | `60.0%` | `+8.1 min` |
| **Route 17567** | 13 | 13 | 0 | **`0.0%`** | `76.92%` | `+4.0 min` |
| **Route 17602** | 8 | 8 | 0 | **`0.0%`** | `75.0%` | `+4.3 min` |
| **Route 17585** | 7 | 7 | 0 | **`0.0%`** | `71.43%` | `+3.5 min` |
| **Route 17608** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+3.7 min` |
| **Route 17604** | 6 | 6 | 0 | **`0.0%`** | `83.33%` | `+2.7 min` |
| **Route 17599** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+3.9 min` |
| **Route 17579** | 8 | 8 | 0 | **`0.0%`** | `75.0%` | `+3.4 min` |
| **Route 17618** | 5 | 5 | 0 | **`0.0%`** | `60.0%` | `+8.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17609** | `+18.1 min (+1083.0s)` | `+18.1 min (+1083s)` | 1 | `0.0%` |
| **Route 17563** | `+17.6 min (+1055.0s)` | `+17.6 min (+1055s)` | 1 | `0.0%` |
| **Route 17618** | `+8.9 min (+533.0s)` | `+26.9 min (+1611s)` | 5 | `60.0%` |
| **Route 17607** | `+8.4 min (+505.5s)` | `+14.7 min (+884s)` | 2 | `50.0%` |
| **Route 17570** | `+8.1 min (+485.8s)` | `+18.4 min (+1102s)` | 5 | `60.0%` |
| **Route 17619** | `+7.8 min (+470.0s)` | `+15.9 min (+956s)` | 3 | `33.33%` |
| **Route 17582** | `+6.8 min (+408.0s)` | `+11.5 min (+690s)` | 3 | `33.33%` |
| **Route 17617** | `+6.3 min (+381.0s)` | `+12.2 min (+729s)` | 4 | `25.0%` |
| **Route 17574** | `+6.2 min (+369.8s)` | `+12.7 min (+764s)` | 4 | `50.0%` |
| **Route 17592** | `+6.0 min (+362.0s)` | `+20.1 min (+1208s)` | 5 | `80.0%` |

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
| `2199427` | Route 17570 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2206527` | Route 17634 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:42.195000+00:00`.*
