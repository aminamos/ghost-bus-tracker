# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-05T17:20:38.786070+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.81%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `743` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `499` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `6` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 6 | 0.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 238 | 32.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 8** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 79** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 114** | 5 | 4 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |
| **Route 51** | 7 | 6 | 1 | **`14.29%`** | `0.0%` | `+0.0s` |
| **Route 64** | 18 | 7 | 1 | **`5.56%`** | `0.0%` | `+0.0s` |
| **Route 47** | 20 | 11 | 1 | **`5.0%`** | `0.0%` | `+0.0s` |
| **Route 1** | 3 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 104** | 10 | 4 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 107** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `957878` | Route 114 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `996662` | Route 47 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `998292` | Route 51 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `975933` | Route 64 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `976527` | Route 79 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `908267` | Route 8 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 17:20:38` | `0.81%` | `0.0%` | 743 | 499 | `+0.0s` |
| `2026-10-05 16:34:17` | `0.81%` | `0.0%` | 739 | 490 | `+0.0s` |
| `2026-10-05 12:15:25` | `0.41%` | `0.0%` | 974 | 667 | `+0.0s` |
| `2026-10-05 12:14:21` | `0.31%` | `0.0%` | 973 | 667 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T17:20:38.786070+00:00`.*
