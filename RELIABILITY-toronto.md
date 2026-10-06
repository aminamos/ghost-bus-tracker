# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T17:21:07.024733+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`6.81%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1894` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1529` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `129` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 129 | 6.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 30** | 2 | 1 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 600** | 16 | 1 | 15 | **`93.75%`** | `0.0%` | `+0.0s` |
| **Route 189** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 151** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 135** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 66** | 6 | 3 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 127** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 67** | 7 | 4 | 2 | **`28.57%`** | `0.0%` | `+0.0s` |
| **Route 32** | 12 | 8 | 3 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `-340644813` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-555921641` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-252991938` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1685370731` | Route 929 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-493027393` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-2140475893` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-675228921` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1000194766` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-4744512` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-164662642` | Route 510 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1516648131` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1818672288` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-454239226` | Route 32 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1584114697` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-261641369` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 17:21:07` | `6.81%` | `0.0%` | 1894 | 1529 | `+0.0s` |
| `2026-10-06 13:46:38` | `6.5%` | `0.0%` | 2061 | 1782 | `+0.0s` |
| `2026-10-06 06:42:13` | `5.45%` | `0.0%` | 330 | 914 | `+0.0s` |
| `2026-10-06 00:28:48` | `7.06%` | `0.0%` | 1529 | 1714 | `+0.0s` |
| `2026-10-05 18:39:14` | `6.89%` | `0.0%` | 2205 | 1784 | `+0.0s` |
| `2026-10-05 18:02:22` | `7.34%` | `0.0%` | 1976 | 1653 | `+0.0s` |
| `2026-10-05 17:57:50` | `8.33%` | `0.0%` | 1945 | 1629 | `+0.0s` |
| `2026-10-05 17:20:41` | `8.56%` | `0.0%` | 1881 | 1525 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T17:21:07.024733+00:00`.*
