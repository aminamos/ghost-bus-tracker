# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** Hamilton | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:51.732000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`45.66%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`85.59%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `484` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `224` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `221` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+74.6s` (`+1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+5.0s` (`+0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 190 | 39.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 13 | 2.7% |
| 🟡 **Minor Delay** | +5m to +15m late | 16 | 3.3% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 221 | 45.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 40 | 8.3% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5803** | 62 | 5 | 55 | **`88.71%`** | `50.0%` | `-22.5s` |
| **Route 5802** | 48 | 6 | 42 | **`87.5%`** | `66.67%` | `+7.6 min` |
| **Route 5782** | 52 | 8 | 42 | **`80.77%`** | `100.0%` | `+0.2 min` |
| **Route 5795** | 33 | 6 | 22 | **`66.67%`** | `71.43%` | `+0.9 min` |
| **Route 5807** | 41 | 13 | 25 | **`60.98%`** | `92.86%` | `+1.0 min` |
| **Route 5783** | 57 | 24 | 32 | **`56.14%`** | `87.5%` | `+1.8 min` |
| **Route 5796** | 5 | 6 | 1 | **`20.0%`** | `100.0%` | `+1.2 min` |
| **Route 5797** | 7 | 6 | 1 | **`14.29%`** | `100.0%` | `+1.8 min` |
| **Route 5798** | 8 | 4 | 1 | **`12.5%`** | `100.0%` | `+0.7 min` |
| **Route 5780** | 18 | 18 | 0 | **`0.0%`** | `88.89%` | `+1.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5802** | `+7.6 min (+454.3s)` | `+22.0 min (+1321s)` | 6 | `66.67%` |
| **Route 5791** | `+3.6 min (+218.5s)` | `+3.9 min (+235s)` | 2 | `100.0%` |
| **Route 5808** | `+3.0 min (+179.8s)` | `+10.6 min (+633s)` | 9 | `77.78%` |
| **Route 5783** | `+1.8 min (+109.2s)` | `+11.2 min (+671s)` | 24 | `87.5%` |
| **Route 5797** | `+1.8 min (+107.7s)` | `+3.5 min (+209s)` | 6 | `100.0%` |
| **Route 5830** | `+1.8 min (+105.5s)` | `+15.7 min (+939s)` | 13 | `92.31%` |
| **Route 5799** | `+1.6 min (+94.6s)` | `+4.7 min (+279s)` | 6 | `100.0%` |
| **Route 5829** | `+1.4 min (+85.7s)` | `+8.9 min (+533s)` | 12 | `83.33%` |
| **Route 5793** | `+1.4 min (+81.7s)` | `+5.2 min (+315s)` | 10 | `80.0%` |
| **Route 5828** | `+1.4 min (+81.2s)` | `+6.9 min (+416s)` | 20 | `85.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5802** | ~15.0m | ~15.0m | **`+0.1 min`** | `31.9 / 100` |
| **Route 5802** | ~15.0m | ~15.0m | **`+0.0 min`** | `46.0 / 100` |
| **Route 5830** | ~15.0m | ~15.0m | **`+0.0 min`** | `62.0 / 100` |
| **Route 5808** | ~7.0m | ~7.0m | **`+0.0 min`** | `44.9 / 100` |
| **Route 5829** | ~10.0m | ~10.0m | **`+0.0 min`** | `66.4 / 100` |
| **Route 5783** | ~6.0m | ~6.0m | **`+0.0 min`** | `57.1 / 100` |
| **Route 5783** | ~14.0m | ~14.0m | **`+0.0 min`** | `74.6 / 100` |
| **Route 5828** | ~6.0m | ~6.0m | **`+0.0 min`** | `62.5 / 100` |
| **Route 5780** | ~6.0m | ~6.0m | **`+0.0 min`** | `68.3 / 100` |
| **Route 5793** | ~10.0m | ~10.0m | **`+0.0 min`** | `77.3 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2200599` | Route 5797 | `14:53:00` | `SCHEDULED` | Assigned vehicle 11209 is broadcasting off-schedule with no vehicle covering 2200599 |
| `2200715` | Route 5798 | `14:56:00` | `SCHEDULED` | Assigned vehicle 11430 is broadcasting off-schedule with no vehicle covering 2200715 |
| `2200452` | Route 5796 | `14:47:00` | `SCHEDULED` | Assigned vehicle 11642 is broadcasting off-schedule with no vehicle covering 2200452 |
| `2190247` | Route 5783 | `14:00:00` | `SCHEDULED` | Assigned vehicle 32322 is broadcasting off-schedule with no vehicle covering 2190247 |
| `2197622` | Route 5807 | `23:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197628` | Route 5807 | `20:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197636` | Route 5807 | `17:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197637` | Route 5807 | `16:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197620` | Route 5807 | `24:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197625` | Route 5807 | `22:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197631` | Route 5807 | `19:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197619` | Route 5807 | `25:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197623` | Route 5807 | `23:03:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197629` | Route 5807 | `20:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2197639` | Route 5807 | `16:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:51.732000+00:00`.*
