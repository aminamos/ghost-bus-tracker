# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metropolitan Atlanta Rapid Transit Authority** in **Atlanta, GA** (Metro Atlanta (Fulton, DeKalb, Clayton Counties), Georgia).
> **Transit System:** MARTA | **Location:** Atlanta, GA | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T12:15:27.500488+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.61%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `447` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `176` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `34` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 34 | 7.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 135 | 30.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 71** | 4 | 3 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route A** | 6 | 4 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 178** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 111** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 83** | 8 | 5 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 80** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 20** | 4 | 3 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 73** | 4 | 1 | 1 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route 89** | 9 | 4 | 2 | **`22.22%`** | `0.0%` | `+0.0s` |
| **Route 125** | 5 | 3 | 1 | **`20.0%`** | `0.0%` | `+0.0s` |

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
| `11696381` | Route 4 | `08:11:00` | `SCHEDULED` | Assigned vehicle 2308 is broadcasting off-schedule with no vehicle covering 11696381 |
| `11703507` | Route 22 | `08:12:00` | `SCHEDULED` | Assigned vehicle 2309 is broadcasting off-schedule with no vehicle covering 11703507 |
| `11710328` | Route 55 | `08:20:00` | `SCHEDULED` | Assigned vehicle 2325 is broadcasting off-schedule with no vehicle covering 11710328 |
| `11697181` | Route 5 | `08:15:00` | `SCHEDULED` | Assigned vehicle 2350 is broadcasting off-schedule with no vehicle covering 11697181 |
| `11704847` | Route 26 | `08:15:00` | `SCHEDULED` | Assigned vehicle 2372 is broadcasting off-schedule with no vehicle covering 11704847 |
| `11699370` | Route 12 | `08:15:00` | `SCHEDULED` | Assigned vehicle 2378 is broadcasting off-schedule with no vehicle covering 11699370 |
| `11706640` | Route 39 | `08:15:00` | `SCHEDULED` | Assigned vehicle 2434 is broadcasting off-schedule with no vehicle covering 11706640 |
| `11784551` | Route 83 | `08:16:00` | `SCHEDULED` | Assigned vehicle 3510 is broadcasting off-schedule with no vehicle covering 11784551 |
| `11722526` | Route 96 | `08:14:00` | `SCHEDULED` | Assigned vehicle 3512 is broadcasting off-schedule with no vehicle covering 11722526 |
| `11734478` | Route 184 | `08:19:00` | `SCHEDULED` | Assigned vehicle 3528 is broadcasting off-schedule with no vehicle covering 11734478 |
| `11718353` | Route 84 | `08:15:00` | `SCHEDULED` | Assigned vehicle 3541 is broadcasting off-schedule with no vehicle covering 11718353 |
| `11720733` | Route 89 | `08:16:00` | `SCHEDULED` | Assigned vehicle 3545 is broadcasting off-schedule with no vehicle covering 11720733 |
| `11784633` | Route 83 | `08:15:00` | `SCHEDULED` | Assigned vehicle 3556 is broadcasting off-schedule with no vehicle covering 11784633 |
| `11720711` | Route 89 | `08:33:00` | `SCHEDULED` | Assigned vehicle 3575 is broadcasting off-schedule with no vehicle covering 11720711 |
| `11730176` | Route 128 | `08:18:00` | `SCHEDULED` | Assigned vehicle 3650 is broadcasting off-schedule with no vehicle covering 11730176 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-05 12:15:27` | `7.61%` | `0.0%` | 447 | 176 | `+0.0s` |
| `2026-10-05 12:14:31` | `7.4%` | `0.0%` | 446 | 175 | `+0.0s` |
| `2026-10-05 12:10:54` | `7.42%` | `0.0%` | 445 | 175 | `+0.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T12:15:27.500488+00:00`.*
