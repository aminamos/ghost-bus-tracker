# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T19:00:21.808000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.97%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2237` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1797` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `156` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 156 | 7.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 600** | 7 | 1 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 184** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 30** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 167** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 156** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 90** | 10 | 5 | 4 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 49** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 5 | 3 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 104** | 3 | 3 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 944** | 12 | 8 | 3 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `-408383912` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-575481895` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-244645641` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1003769299` | Route 29 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-2091083565` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-2006216937` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1933445551` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1346096752` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1506695167` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1881984748` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1993340017` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1720282321` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-300851656` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1287767234` | Route 32 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `4562020` | Route 49 | `N/A` | `SCHEDULED` | Assigned vehicle 8361 is broadcasting off-schedule with no vehicle covering 4562020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 19:00:21` | `6.97%` | `0.0%` | 2237 | 1797 | `+0.0s` |
| `2026-10-22 18:30:37` | `6.45%` | `0.0%` | 2079 | 1725 | `+0.0s` |
| `2026-10-22 18:00:40` | `7.07%` | `0.0%` | 1939 | 1609 | `+0.0s` |
| `2026-10-22 17:30:38` | `7.65%` | `0.0%` | 1844 | 1542 | `+0.0s` |
| `2026-10-22 17:00:39` | `8.3%` | `0.0%` | 1831 | 1495 | `+0.0s` |
| `2026-10-22 16:31:19` | `8.23%` | `0.0%` | 1834 | 1479 | `+0.0s` |
| `2026-10-22 15:01:09` | `7.33%` | `0.0%` | 1814 | 1581 | `+0.0s` |
| `2026-10-22 14:30:50` | `8.29%` | `0.0%` | 1857 | 1686 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:00:21.808000+00:00`.*
