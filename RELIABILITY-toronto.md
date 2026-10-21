# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-21T22:30:36.012000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2332` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1820` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `171` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 171 | 7.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 600** | 6 | 0 | 6 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 55** | 4 | 2 | 4 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 82** | 3 | 2 | 3 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 33** | 4 | 2 | 3 | **`75.0%`** | `0.0%` | `+0.0s` |
| **Route 105** | 6 | 3 | 4 | **`66.67%`** | `0.0%` | `+0.0s` |
| **Route 99** | 6 | 2 | 3 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 125** | 9 | 3 | 3 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 512** | 29 | 18 | 9 | **`31.03%`** | `0.0%` | `+0.0s` |
| **Route 900** | 12 | 6 | 3 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 64** | 8 | 5 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `-1426386491` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1631317094` | Route 91 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1502216410` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-568817039` | Route 512 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1893179938` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-83649556` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1129059901` | Route 510 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1621193222` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1793947528` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-284743393` | Route 72 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `107365020` | Route 47 | `N/A` | `SCHEDULED` | Assigned vehicle 7001 is broadcasting off-schedule with no vehicle covering 107365020 |
| `105962020` | Route 101 | `N/A` | `SCHEDULED` | Assigned vehicle 3461 is broadcasting off-schedule with no vehicle covering 105962020 |
| `81651020` | Route 54 | `N/A` | `SCHEDULED` | Assigned vehicle 8964 is broadcasting off-schedule with no vehicle covering 81651020 |
| `18841020` | Route 68 | `N/A` | `SCHEDULED` | Assigned vehicle 8638 is broadcasting off-schedule with no vehicle covering 18841020 |
| `3200020` | Route 82 | `N/A` | `SCHEDULED` | Assigned vehicle 8530 is broadcasting off-schedule with no vehicle covering 3200020 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-21 22:30:36` | `7.33%` | `0.0%` | 2332 | 1820 | `+0.0s` |
| `2026-10-21 22:00:35` | `7.1%` | `0.0%` | 2407 | 1815 | `+0.0s` |
| `2026-10-21 21:30:36` | `6.8%` | `0.0%` | 2428 | 1835 | `+0.0s` |
| `2026-10-21 21:00:36` | `7.52%` | `0.0%` | 2421 | 1848 | `+0.0s` |
| `2026-10-21 20:30:36` | `6.69%` | `0.0%` | 2437 | 1849 | `+0.0s` |
| `2026-10-21 20:00:36` | `7.56%` | `0.0%` | 2381 | 1849 | `+0.0s` |
| `2026-10-21 19:30:39` | `6.33%` | `0.0%` | 2369 | 1837 | `+0.0s` |
| `2026-10-21 19:00:51` | `6.82%` | `0.0%` | 2288 | 1824 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-21T22:30:36.012000+00:00`.*
