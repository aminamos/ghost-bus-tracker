# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Southeastern Pennsylvania Transportation Authority** in **Philadelphia, PA** (Greater Philadelphia / Delaware Valley, Pennsylvania).
> **Transit System:** SEPTA | **Location:** Philadelphia, PA | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-06T00:28:47.018617+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.17%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `606` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `311` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 0.2% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 294 | 48.5% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 16** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 104** | 18 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 8 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 107** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 108** | 25 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 109** | 3 | 3 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 110** | 8 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 111** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 112** | 6 | 0 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |
| **Route 113** | 12 | 6 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `869353` | Route 16 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 00:28:47` | `0.17%` | `0.0%` | 606 | 311 | `+0.0s` |
| `2026-10-05 18:39:12` | `1.56%` | `0.0%` | 898 | 613 | `+0.0s` |
| `2026-10-05 18:02:19` | `1.33%` | `0.0%` | 830 | 549 | `+0.0s` |
| `2026-10-05 17:57:48` | `1.21%` | `0.0%` | 829 | 523 | `+0.0s` |
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

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T00:28:47.018617+00:00`.*
