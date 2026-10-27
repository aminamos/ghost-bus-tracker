# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-27T05:00:22.962000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`4.29%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`75.23%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `350` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `484` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `15` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+185.6s` (`+3.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+118.0s` (`+2.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 249 | 71.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 28 | 8.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 44 | 12.6% |
| 🔴 **Severe Delay** | Over 15m late | 10 | 2.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 15 | 4.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 4 | 1.1% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 104** | 3 | 2 | 1 | **`33.33%`** | `50.0%` | `-39.5s` |
| **Route 35** | 8 | 8 | 2 | **`25.0%`** | `100.0%` | `+2.7 min` |
| **Route 19** | 8 | 8 | 2 | **`25.0%`** | `83.33%` | `+5.3 min` |
| **Route EART** | 4 | 4 | 1 | **`25.0%`** | `66.67%` | `+0.3 min` |
| **Route 12** | 4 | 4 | 1 | **`25.0%`** | `66.67%` | `-30.0s` |
| **Route 108** | 4 | 3 | 1 | **`25.0%`** | `100.0%` | `+1.7 min` |
| **Route 8** | 4 | 4 | 1 | **`25.0%`** | `66.67%` | `+4.2 min` |
| **Route 13** | 5 | 3 | 1 | **`20.0%`** | `100.0%` | `+2.1 min` |
| **Route 16** | 5 | 5 | 1 | **`20.0%`** | `100.0%` | `+2.0 min` |
| **Route 0** | 6 | 5 | 1 | **`16.67%`** | `40.0%` | `+2.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17** | `+16.2 min (+971.0s)` | `+69.4 min (+4164s)` | 7 | `50.0%` |
| **Route 51** | `+9.7 min (+580.7s)` | `+30.7 min (+1842s)` | 6 | `42.86%` |
| **Route 29** | `+6.8 min (+407.7s)` | `+17.1 min (+1025s)` | 7 | `57.14%` |
| **Route 72** | `+6.6 min (+394.0s)` | `+34.7 min (+2082s)` | 9 | `80.0%` |
| **Route 40** | `+6.4 min (+383.3s)` | `+29.4 min (+1765s)` | 5 | `66.67%` |
| **Route 44** | `+5.5 min (+330.0s)` | `+13.8 min (+827s)` | 5 | `50.0%` |
| **Route 70** | `+5.4 min (+323.6s)` | `+9.8 min (+588s)` | 8 | `60.0%` |
| **Route 19** | `+5.3 min (+319.3s)` | `+14.6 min (+874s)` | 8 | `83.33%` |
| **Route 56** | `+5.1 min (+304.6s)` | `+12.2 min (+735s)` | 3 | `60.0%` |
| **Route 41** | `+5.1 min (+304.1s)` | `+18.7 min (+1120s)` | 8 | `75.0%` |

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
| `24430053` | Route EART | `N/A` | `SCHEDULED` | Assigned vehicle 1606 is broadcasting off-schedule with no vehicle covering 24430053 |
| `24784255` | Route 16 | `N/A` | `SCHEDULED` | Assigned vehicle 5220 is broadcasting off-schedule with no vehicle covering 24784255 |
| `24784232` | Route 50 | `N/A` | `SCHEDULED` | Assigned vehicle 5726 is broadcasting off-schedule with no vehicle covering 24784232 |
| `24784247` | Route 12 | `N/A` | `SCHEDULED` | Assigned vehicle 5321 is broadcasting off-schedule with no vehicle covering 24784247 |
| `24427878` | Route 108 | `N/A` | `SCHEDULED` | Assigned vehicle 6859 is broadcasting off-schedule with no vehicle covering 24427878 |
| `24784465` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 8143 is broadcasting off-schedule with no vehicle covering 24784465 |
| `24784532` | Route 35 | `N/A` | `SCHEDULED` | Assigned vehicle 5728 is broadcasting off-schedule with no vehicle covering 24784532 |
| `24783691` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 8118 is broadcasting off-schedule with no vehicle covering 24783691 |
| `24784996` | Route 0 | `N/A` | `SCHEDULED` | Assigned vehicle 5662 is broadcasting off-schedule with no vehicle covering 24784996 |
| `24732196` | Route 13 | `N/A` | `SCHEDULED` | Assigned vehicle 5008 is broadcasting off-schedule with no vehicle covering 24732196 |
| `24782558` | Route 8 | `N/A` | `SCHEDULED` | Assigned vehicle 5263 is broadcasting off-schedule with no vehicle covering 24782558 |
| `24784861` | Route 70 | `N/A` | `SCHEDULED` | Assigned vehicle 5165 is broadcasting off-schedule with no vehicle covering 24784861 |
| `24428445` | Route 72 | `N/A` | `SCHEDULED` | Assigned vehicle 6815 is broadcasting off-schedule with no vehicle covering 24428445 |
| `24783728` | Route 19 | `N/A` | `SCHEDULED` | Assigned vehicle 5763 is broadcasting off-schedule with no vehicle covering 24783728 |
| `24428055` | Route 104 | `N/A` | `SCHEDULED` | Assigned vehicle 6771 is broadcasting off-schedule with no vehicle covering 24428055 |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-27 05:00:22` | `4.29%` | `75.23%` | 350 | 484 | `+185.6s` |
| `2026-10-27 04:30:20` | `4.06%` | `72.12%` | 394 | 493 | `+189.8s` |
| `2026-10-27 04:00:57` | `2.65%` | `75.82%` | 415 | 553 | `+176.9s` |
| `2026-10-27 03:30:23` | `3.46%` | `74.88%` | 434 | 587 | `+166.7s` |
| `2026-10-27 02:30:20` | `2.56%` | `72.8%` | 508 | 630 | `+202.2s` |
| `2026-10-27 01:30:23` | `2.67%` | `71.45%` | 636 | 699 | `+250.0s` |
| `2026-10-27 00:30:55` | `2.57%` | `70.55%` | 739 | 702 | `+240.0s` |
| `2026-10-26 23:00:23` | `2.83%` | `67.61%` | 741 | 707 | `+251.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-27T05:00:22.962000+00:00`.*
