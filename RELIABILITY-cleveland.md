# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-08T07:00:18.001000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`89.61%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `356` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `142` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `319` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+102.3s` (`+1.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+31.0s` (`+0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 12 | 3.4% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.3% |
| 🟡 **Minor Delay** | +5m to +15m late | 2 | 0.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 319 | 89.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 11** | 70 | 0 | 70 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 36 | 0 | 36 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 77** | 32 | 0 | 32 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 8** | 15 | 0 | 15 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 15** | 77 | 1 | 76 | **`98.7%`** | `100.0%` | `+3.1 min` |
| **Route 14** | 93 | 2 | 89 | **`95.7%`** | `100.0%` | `+3.8 min` |
| **Route 19** | 5 | 3 | 1 | **`20.0%`** | `100.0%` | `-52.0s` |
| **Route 25** | 3 | 2 | 0 | **`0.0%`** | `100.0%` | `+2.1 min` |
| **Route 41** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 26** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 10** | `+6.2 min (+372.0s)` | `+6.2 min (+372s)` | 2 | `0.0%` |
| **Route 48** | `+6.2 min (+370.0s)` | `+6.2 min (+370s)` | 2 | `0.0%` |
| **Route 14** | `+3.8 min (+228.0s)` | `+4.5 min (+272s)` | 2 | `100.0%` |
| **Route 15** | `+3.1 min (+189.0s)` | `+3.1 min (+189s)` | 1 | `100.0%` |
| **Route 25** | `+2.1 min (+127.0s)` | `+2.1 min (+127s)` | 2 | `100.0%` |
| **Route 22** | `+1.9 min (+113.0s)` | `+1.9 min (+113s)` | 2 | `100.0%` |
| **Route 41** | `+0.3 min (+21.0s)` | `+0.5 min (+31s)` | 2 | `100.0%` |
| **Route 6** | `+0.3 min (+16.5s)` | `+0.5 min (+30s)` | 3 | `100.0%` |
| **Route 51** | `+0.1 min (+5.0s)` | `+0.1 min (+5s)` | 1 | `100.0%` |

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
| `19236089` | Route 19 | `06:40:00` | `SCHEDULED` | Assigned vehicle 4254 is broadcasting off-schedule with no vehicle covering 19236089 |
| `19235745` | Route 14 | `26:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19235744` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237116` | Route 8 | `07:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237120` | Route 8 | `09:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237124` | Route 8 | `11:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237128` | Route 8 | `13:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237132` | Route 8 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237136` | Route 8 | `17:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237140` | Route 8 | `19:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237114` | Route 8 | `06:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237118` | Route 8 | `08:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237122` | Route 8 | `10:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237126` | Route 8 | `12:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19237130` | Route 8 | `14:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-08 07:00:18` | `89.61%` | `80.0%` | 356 | 142 | `+102.3s` |
| `2026-11-08 06:30:19` | `87.36%` | `80.77%` | 364 | 150 | `+138.0s` |
| `2026-11-08 06:00:18` | `84.68%` | `71.43%` | 385 | 158 | `+192.1s` |
| `2026-11-08 05:30:19` | `79.95%` | `85.71%` | 409 | 163 | `+209.7s` |
| `2026-11-08 05:00:18` | `5.56%` | `65.45%` | 126 | 179 | `+184.4s` |
| `2026-11-08 04:30:22` | `9.15%` | `80.6%` | 153 | 186 | `+191.0s` |
| `2026-11-08 04:00:18` | `9.55%` | `75.68%` | 178 | 191 | `+217.0s` |
| `2026-11-08 03:30:18` | `11.17%` | `78.05%` | 197 | 191 | `+170.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-08T07:00:18.001000+00:00`.*
