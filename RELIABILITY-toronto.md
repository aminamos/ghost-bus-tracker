# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-22T18:30:37.174000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.45%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2079` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1725` | GPS transponders broadcasting valid coordinates |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 134 | 6.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 600** | 8 | 1 | 7 | **`87.5%`** | `0.0%` | `+0.0s` |
| **Route 99** | 4 | 2 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 92** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 125** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 156** | 2 | 2 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 900** | 13 | 6 | 5 | **`38.46%`** | `0.0%` | `+0.0s` |
| **Route 103** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 76** | 11 | 6 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route 944** | 12 | 8 | 3 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 117** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `-244645641` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-863162567` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-2006216937` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1933445551` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-2023384059` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1346096752` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1881984748` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-300851656` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `93269020` | Route 52 | `N/A` | `SCHEDULED` | Assigned vehicle 3264 is broadcasting off-schedule with no vehicle covering 93269020 |
| `39600020` | Route 17 | `N/A` | `SCHEDULED` | Assigned vehicle 3207 is broadcasting off-schedule with no vehicle covering 39600020 |
| `1583020` | Route 941 | `N/A` | `SCHEDULED` | Assigned vehicle 9446 is missing from active GPS transponder fleet |
| `33539020` | Route 7 | `N/A` | `SCHEDULED` | Assigned vehicle 9014 is broadcasting off-schedule with no vehicle covering 33539020 |
| `133622020` | Route 900 | `N/A` | `SCHEDULED` | Assigned vehicle 3347 is broadcasting off-schedule with no vehicle covering 133622020 |
| `25492020` | Route 112 | `N/A` | `SCHEDULED` | Assigned vehicle 7230 is broadcasting off-schedule with no vehicle covering 25492020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 18:30:37` | `6.45%` | `0.0%` | 2079 | 1725 | `+0.0s` |
| `2026-10-22 18:00:40` | `7.07%` | `0.0%` | 1939 | 1609 | `+0.0s` |
| `2026-10-22 17:30:38` | `7.65%` | `0.0%` | 1844 | 1542 | `+0.0s` |
| `2026-10-22 17:00:39` | `8.3%` | `0.0%` | 1831 | 1495 | `+0.0s` |
| `2026-10-22 16:31:19` | `8.23%` | `0.0%` | 1834 | 1479 | `+0.0s` |
| `2026-10-22 15:01:09` | `7.33%` | `0.0%` | 1814 | 1581 | `+0.0s` |
| `2026-10-22 14:30:50` | `8.29%` | `0.0%` | 1857 | 1686 | `+0.0s` |
| `2026-10-22 14:00:48` | `7.63%` | `0.0%` | 1914 | 1770 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T18:30:37.174000+00:00`.*
