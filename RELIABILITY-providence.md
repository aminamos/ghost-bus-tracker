# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Rhode Island Public Transit Authority** in **Providence, RI** (Rhode Island).
> **Transit System:** Providence | **Location:** Providence, RI | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:56.566000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`36.22%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`63.2%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `196` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `127` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `71` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+180.0s` (`+3.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+60.0s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 79 | 40.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 16 | 8.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 24 | 12.2% |
| 🔴 **Severe Delay** | Over 15m late | 6 | 3.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 71 | 36.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 34** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 57** | 3 | 1 | 2 | **`66.67%`** | `100.0%` | `+5.0 min` |
| **Route 31** | 5 | 2 | 3 | **`60.0%`** | `100.0%` | `+0.5 min` |
| **Route 56** | 7 | 3 | 4 | **`57.14%`** | `66.67%` | `+5.0 min` |
| **Route 50** | 6 | 3 | 3 | **`50.0%`** | `100.0%` | `-20.0s` |
| **Route 55** | 4 | 2 | 2 | **`50.0%`** | `50.0%` | `+7.0 min` |
| **Route 17** | 4 | 2 | 2 | **`50.0%`** | `50.0%` | `+4.5 min` |
| **Route 4** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `+1.5 min` |
| **Route 16** | 4 | 2 | 2 | **`50.0%`** | `50.0%` | `+14.0 min` |
| **Route 87** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `+2.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 16** | `+14.0 min (+840.0s)` | `+23.0 min (+1380s)` | 2 | `50.0%` |
| **Route 66** | `+10.5 min (+630.0s)` | `+11.0 min (+660s)` | 2 | `0.0%` |
| **Route 7** | `+10.0 min (+600.0s)` | `+17.0 min (+1020s)` | 3 | `33.33%` |
| **Route 19** | `+7.2 min (+435.0s)` | `+19.0 min (+1140s)` | 4 | `50.0%` |
| **Route 55** | `+7.0 min (+420.0s)` | `+11.0 min (+660s)` | 2 | `50.0%` |
| **Route 6** | `+7.0 min (+420.0s)` | `+7.0 min (+420s)` | 2 | `0.0%` |
| **Route 60** | `+6.2 min (+370.0s)` | `+21.0 min (+1260s)` | 6 | `16.67%` |
| **Route 73** | `+6.0 min (+360.0s)` | `+6.0 min (+360s)` | 1 | `0.0%` |
| **Route 56** | `+5.0 min (+300.0s)` | `+11.0 min (+660s)` | 3 | `66.67%` |
| **Route 57** | `+5.0 min (+300.0s)` | `+5.0 min (+300s)` | 1 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 16** | ~9.0m | ~9.0m | **`+0.1 min`** | `0.0 / 100` |
| **Route 27** | ~8.0m | ~8.0m | **`+0.1 min`** | `3.8 / 100` |
| **Route 20** | ~6.0m | ~6.0m | **`+0.1 min`** | `0.0 / 100` |
| **Route 60** | ~17.5m | ~17.5m | **`+0.0 min`** | `45.1 / 100` |
| **Route 19** | ~17.0m | ~17.0m | **`+0.0 min`** | `51.4 / 100` |
| **Route 64** | ~30.0m | ~30.0m | **`+0.0 min`** | `64.0 / 100` |
| **Route 11** | ~8.5m | ~8.5m | **`+0.0 min`** | `40.6 / 100` |
| **Route 56** | ~6.5m | ~6.5m | **`+0.0 min`** | `33.5 / 100` |
| **Route 7** | ~26.0m | ~26.0m | **`+0.0 min`** | `69.7 / 100` |
| **Route 1** | ~4.0m | ~4.0m | **`+0.0 min`** | `35.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `4909327` | Route 17 | `15:33:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4909389` | Route 1 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4910194` | Route 17 | `15:16:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4909618` | Route 33 | `15:17:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907650` | Route 92 | `15:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4906845` | Route 28 | `15:43:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907655` | Route 20 | `15:12:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907727` | Route 7 | `15:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907799` | Route 30 | `15:40:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907785` | Route 20 | `15:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907764` | Route 20 | `15:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907745` | Route 20 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907856` | Route 4 | `15:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4907920` | Route 27 | `15:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4909413` | Route 56 | `15:29:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:56.566000+00:00`.*
