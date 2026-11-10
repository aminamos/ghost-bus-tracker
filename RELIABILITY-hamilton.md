# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-10T07:00:18.691000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.28%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `254` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `11` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `242` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+72.5s` (`+1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 3 | 1.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 1 | 0.4% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 242 | 95.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 109 | 1 | 107 | **`98.17%`** | `100.0%` | `-13.5s` |
| **Route 5783** | 78 | 2 | 76 | **`97.44%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 61 | 1 | 59 | **`96.72%`** | `50.0%` | `+2.6 min` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5795** | `+2.6 min (+158.5s)` | `+5.3 min (+317s)` | 1 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5795** | ~20.0m | ~20.0m | **`+0.0 min`** | `86.8 / 100` |
| **Route 5782** | ~20.0m | ~20.0m | **`+0.0 min`** | `98.9 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2200292` | Route 5795 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200275` | Route 5795 | `16:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200273` | Route 5795 | `16:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200271` | Route 5795 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200278` | Route 5795 | `17:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200261` | Route 5795 | `12:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200256` | Route 5795 | `11:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200281` | Route 5795 | `18:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200268` | Route 5795 | `15:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200283` | Route 5795 | `19:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200279` | Route 5795 | `17:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200244` | Route 5795 | `07:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200266` | Route 5795 | `14:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200249` | Route 5795 | `08:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2200285` | Route 5795 | `20:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-10 07:00:18` | `95.28%` | `75.0%` | 254 | 11 | `+72.5s` |
| `2026-11-10 06:30:19` | `82.99%` | `83.33%` | 294 | 49 | `+87.8s` |
| `2026-11-10 06:00:18` | `74.3%` | `92.31%` | 323 | 77 | `+10.5s` |
| `2026-11-10 05:30:21` | `70.62%` | `87.5%` | 337 | 88 | `+23.3s` |
| `2026-11-10 05:00:19` | `6.8%` | `100.0%` | 103 | 93 | `+29.8s` |
| `2026-11-10 04:30:20` | `9.26%` | `86.67%` | 108 | 94 | `+77.4s` |
| `2026-11-10 04:00:21` | `16.81%` | `89.36%` | 113 | 96 | `+59.1s` |
| `2026-11-10 03:30:18` | `15.83%` | `0.0%` | 120 | 98 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-10T07:00:18.691000+00:00`.*
