# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Greater Cleveland Regional Transit Authority** in **Cleveland, OH** (Cleveland Metropolitan Area, Ohio).
> **Transit System:** GCRTA | **Location:** Cleveland, OH | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-11-14T07:00:18.876000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`5.45%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`21.74%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `55` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `180` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `3` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+4862.3s` (`+81.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+6073.0s` (`+101.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 10 | 18.2% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 36 | 65.5% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 3 | 5.5% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 14** | 6 | 2 | 2 | **`33.33%`** | `0.0%` | `+109.5 min` |
| **Route 19** | 4 | 2 | 0 | **`0.0%`** | `50.0%` | `+57.2 min` |
| **Route 25** | 4 | 2 | 0 | **`0.0%`** | `25.0%` | `+79.1 min` |
| **Route 26** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+99.9 min` |
| **Route 22** | 4 | 2 | 0 | **`0.0%`** | `0.0%` | `+105.5 min` |
| **Route 15** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+116.5 min` |
| **Route 1** | 2 | 1 | 0 | **`0.0%`** | `50.0%` | `+42.7 min` |
| **Route 28** | 2 | 1 | 0 | **`0.0%`** | `50.0%` | `+50.0 min` |
| **Route 10** | 4 | 2 | 0 | **`0.0%`** | `25.0%` | `+72.1 min` |
| **Route 6** | 6 | 3 | 0 | **`0.0%`** | `33.33%` | `+75.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 15** | `+116.5 min (+6988.0s)` | `+120.2 min (+7213s)` | 1 | `0.0%` |
| **Route 51** | `+114.7 min (+6881.0s)` | `+116.7 min (+7001s)` | 2 | `0.0%` |
| **Route 3** | `+112.7 min (+6762.0s)` | `+115.2 min (+6912s)` | 1 | `0.0%` |
| **Route 14** | `+109.5 min (+6569.5s)` | `+120.2 min (+7213s)` | 2 | `0.0%` |
| **Route 22** | `+105.5 min (+6328.0s)` | `+110.2 min (+6612s)` | 2 | `0.0%` |
| **Route 26** | `+99.9 min (+5991.5s)` | `+110.2 min (+6614s)` | 2 | `0.0%` |
| **Route 48** | `+98.5 min (+5909.0s)` | `+105.2 min (+6314s)` | 2 | `0.0%` |
| **Route 25** | `+79.1 min (+4746.0s)` | `+110.2 min (+6610s)` | 2 | `25.0%` |
| **Route 6** | `+75.6 min (+4537.8s)` | `+124.3 min (+7456s)` | 3 | `33.33%` |
| **Route 10** | `+72.1 min (+4328.2s)` | `+120.1 min (+7207s)` | 2 | `25.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 6** | ~30.0m | ~30.0m | **`+0.8 min`** | `0.0 / 100` |
| **Route 6** | ~30.5m | ~30.5m | **`+0.7 min`** | `0.0 / 100` |
| **Route 25** | ~52.0m | ~52.0m | **`+0.5 min`** | `0.0 / 100` |
| **Route 10** | ~92.0m | ~92.0m | **`+0.3 min`** | `40.3 / 100` |
| **Route 10** | ~64.0m | ~64.0m | **`+0.1 min`** | `50.0 / 100` |
| **Route 41** | ~61.0m | ~61.0m | **`+0.1 min`** | `50.0 / 100` |
| **Route 14** | ~70.5m | ~70.5m | **`+0.0 min`** | `82.0 / 100` |
| **Route 26** | ~60.0m | ~60.0m | **`+0.0 min`** | `87.5 / 100` |
| **Route 22** | ~60.0m | ~60.0m | **`+0.0 min`** | `93.4 / 100` |
| **Route 25** | ~60.0m | ~60.0m | **`+0.0 min`** | `94.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `19234512` | Route 11 | `05:57:00` | `SCHEDULED` | Assigned vehicle 4110 is broadcasting off-schedule with no vehicle covering 19234512 |
| `19234727` | Route 14 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `19234728` | Route 14 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-14 07:00:18` | `5.45%` | `21.74%` | 55 | 180 | `+4862.3s` |
| `2026-11-14 06:30:19` | `12.5%` | `25.0%` | 64 | 171 | `+3190.1s` |
| `2026-11-14 06:00:19` | `15.38%` | `24.0%` | 91 | 179 | `+2005.5s` |
| `2026-11-14 05:30:18` | `12.93%` | `33.33%` | 116 | 194 | `+908.7s` |
| `2026-11-14 05:00:20` | `8.21%` | `68.85%` | 134 | 201 | `+265.1s` |
| `2026-11-14 04:30:18` | `8.02%` | `76.92%` | 162 | 210 | `+220.7s` |
| `2026-11-14 04:00:20` | `10.77%` | `74.39%` | 195 | 223 | `+183.1s` |
| `2026-11-14 03:00:19` | `14.17%` | `78.12%` | 247 | 222 | `+209.0s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-14T07:00:18.876000+00:00`.*
