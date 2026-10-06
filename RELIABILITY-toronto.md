# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T13:46:38.953535+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.5%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2061` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1782` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `134` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 134 | 6.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 600** | 13 | 3 | 13 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 125** | 8 | 4 | 6 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 126** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 83** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 968** | 4 | 4 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 944** | 10 | 7 | 4 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 44** | 12 | 8 | 4 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 65** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 132** | 6 | 3 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 191** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |

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
| `-1100366756` | Route 25 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-675228921` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1516648131` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1684303236` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-261641369` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-127649911` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-40114943` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-340644813` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-2115778149` | Route 25 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-244104228` | Route 25 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1559198662` | Route 191 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-426425300` | Route 100 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-83515717` | Route 70 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1029634005` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-2140475893` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 13:46:38` | `6.5%` | `0.0%` | 2061 | 1782 | `+0.0s` |
| `2026-10-06 06:42:13` | `5.45%` | `0.0%` | 330 | 914 | `+0.0s` |
| `2026-10-06 00:28:48` | `7.06%` | `0.0%` | 1529 | 1714 | `+0.0s` |
| `2026-10-05 18:39:14` | `6.89%` | `0.0%` | 2205 | 1784 | `+0.0s` |
| `2026-10-05 18:02:22` | `7.34%` | `0.0%` | 1976 | 1653 | `+0.0s` |
| `2026-10-05 17:57:50` | `8.33%` | `0.0%` | 1945 | 1629 | `+0.0s` |
| `2026-10-05 17:20:41` | `8.56%` | `0.0%` | 1881 | 1525 | `+0.0s` |
| `2026-10-05 16:34:19` | `9.38%` | `0.0%` | 1866 | 1452 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T13:46:38.953535+00:00`.*
