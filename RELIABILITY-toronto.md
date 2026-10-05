# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Toronto Transit Commission** in **Toronto, ON** (Greater Toronto Area, Ontario).
> **Transit System:** TTC | **Location:** Toronto, ON | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-05T12:14:22.105522+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`8.04%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `2425` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1825` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `195` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 195 | 8.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 600** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 184** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 900** | 14 | 5 | 8 | **`57.14%`** | `0.0%` | `+0.0s` |
| **Route 28** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route 135** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route 83** | 6 | 3 | 2 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 103** | 3 | 2 | 1 | **`33.33%`** | `0.0%` | `+0.0s` |
| **Route 121** | 7 | 4 | 2 | **`28.57%`** | `0.0%` | `+0.0s` |
| **Route 22** | 7 | 3 | 2 | **`28.57%`** | `0.0%` | `+0.0s` |
| **Route 986** | 16 | 13 | 4 | **`25.0%`** | `0.0%` | `+0.0s` |

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
| `-1496277345` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-43345536` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-961027501` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1804813496` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1885568186` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1474575292` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-726034202` | Route 511 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1154503720` | Route 7 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1535412988` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1057903011` | Route 501 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1898688218` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `-1353808235` | Route 600 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `101497020` | Route 44 | `N/A` | `SCHEDULED` | Assigned vehicle 3368 is broadcasting off-schedule with no vehicle covering 101497020 |
| `41549020` | Route 953 | `N/A` | `SCHEDULED` | Assigned vehicle 3212 is broadcasting off-schedule with no vehicle covering 41549020 |
| `80566020` | Route 986 | `N/A` | `SCHEDULED` | Assigned vehicle 3486 is broadcasting off-schedule with no vehicle covering 80566020 |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-05T12:14:22.105522+00:00`.*
