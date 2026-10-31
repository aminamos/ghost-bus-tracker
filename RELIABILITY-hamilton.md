# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-31T06:30:19.140000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`99.01%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `203` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `2` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `201` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 201 | 99.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 96 | 0 | 96 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 66 | 0 | 66 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2194055` | Route 5795 | `21:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194072` | Route 5795 | `23:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194041` | Route 5795 | `13:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194045` | Route 5795 | `15:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194049` | Route 5795 | `16:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194053` | Route 5795 | `18:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194054` | Route 5795 | `19:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194067` | Route 5795 | `21:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194058` | Route 5795 | `22:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194062` | Route 5795 | `24:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194070` | Route 5795 | `06:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194075` | Route 5795 | `08:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194063` | Route 5795 | `09:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194077` | Route 5795 | `11:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194069` | Route 5795 | `12:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-31 06:30:19` | `99.01%` | `0.0%` | 203 | 2 | `+0.0s` |
| `2026-10-31 06:00:19` | `94.37%` | `100.0%` | 213 | 14 | `+26.5s` |
| `2026-10-31 05:30:21` | `80.72%` | `100.0%` | 249 | 51 | `+76.0s` |
| `2026-10-31 04:30:22` | `69.7%` | `81.25%` | 297 | 87 | `+189.1s` |
| `2026-10-31 04:00:18` | `11.32%` | `92.31%` | 106 | 91 | `+96.0s` |
| `2026-10-31 03:30:18` | `16.81%` | `80.0%` | 113 | 92 | `+144.5s` |
| `2026-10-31 03:00:18` | `19.17%` | `88.24%` | 120 | 93 | `+148.0s` |
| `2026-10-31 02:00:22` | `24.0%` | `80.0%` | 150 | 110 | `+115.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-31T06:30:19.140000+00:00`.*
