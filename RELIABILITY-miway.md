# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **MiWay** in **Mississauga, ON** (City of Mississauga, Ontario).
> **Transit System:** MiWay | **Location:** Mississauga, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-25T06:15:48.269000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`86.23%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `167` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `23` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `144` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+1937.0s` (`+32.3 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+1937.0s` (`+32.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 1 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 144 | 86.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 7** | 52 | 0 | 52 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 103** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 17** | 56 | 1 | 55 | **`98.21%`** | `0.0%` | `+32.3 min` |
| **Route 26** | 5 | 5 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 29** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 4 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 48** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17** | `+32.3 min (+1937.0s)` | `+32.3 min (+1937s)` | 1 | `0.0%` |

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
| `30503384` | Route 17 | `24:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503382` | Route 17 | `23:28:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503380` | Route 17 | `22:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503378` | Route 17 | `21:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503366` | Route 17 | `17:24:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503385` | Route 17 | `24:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503383` | Route 17 | `23:54:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503381` | Route 17 | `23:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503379` | Route 17 | `22:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503377` | Route 17 | `20:58:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503374` | Route 17 | `19:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503370` | Route 17 | `18:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503348` | Route 17 | `11:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503373` | Route 17 | `19:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `30503369` | Route 17 | `18:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-25 06:15:48` | `86.23%` | `0.0%` | 167 | 23 | `+1937.0s` |
| `2026-10-25 06:01:04` | `82.76%` | `0.0%` | 174 | 30 | `+1433.0s` |
| `2026-10-25 05:30:23` | `74.74%` | `50.0%` | 194 | 49 | `+216.5s` |
| `2026-10-25 05:00:33` | `71.22%` | `0.0%` | 205 | 59 | `-197.0s` |
| `2026-10-25 04:33:58` | `68.37%` | `60.0%` | 215 | 67 | `+40.2s` |
| `2026-10-25 03:30:21` | `8.33%` | `75.0%` | 108 | 99 | `+43.0s` |
| `2026-10-25 03:00:22` | `8.4%` | `62.5%` | 131 | 118 | `+115.4s` |
| `2026-10-25 02:30:20` | `10.96%` | `50.0%` | 146 | 130 | `+91.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-25T06:15:48.269000+00:00`.*
