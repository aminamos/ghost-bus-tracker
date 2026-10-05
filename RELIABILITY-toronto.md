# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T17:57:50.964844+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1945` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1629` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `162` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 162 | 8.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 600** | 18 | 0 | 18 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 184** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 104** | 3 | 3 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 92** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 126** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 123** | 9 | 5 | 4 | **`44.44%`** | `0.0%` | `+0.0s` |
| **Route 90** | 9 | 4 | 4 | **`44.44%`** | `0.0%` | `+0.0s` |
| **Route 62** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 50** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |

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
| `-1155510042` | Route 512 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1850927314` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-872762800` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-897295558` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-2142887842` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-887346832` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1490113166` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1688026021` | Route 29 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1468440021` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1656863411` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-426048211` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1825755977` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1135226274` | Route 929 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1017879987` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-331695131` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 17:57:50` | `8.33%` | `0.0%` | 1945 | 1629 | `+0.0s` |
| `2026-10-05 17:20:41` | `8.56%` | `0.0%` | 1881 | 1525 | `+0.0s` |
| `2026-10-05 16:34:19` | `9.38%` | `0.0%` | 1866 | 1452 | `+0.0s` |
| `2026-10-05 12:15:28` | `6.56%` | `0.0%` | 2422 | 1818 | `+0.0s` |
| `2026-10-05 12:14:22` | `8.04%` | `0.0%` | 2425 | 1825 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T17:57:50.964844+00:00`.*
