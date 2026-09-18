# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-18T06:08:06.647145+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`7.84%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`68.09%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `51` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `47` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `4` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+40.8s` (`0.7 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+-3.0s` (`-0.1 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 32 | 62.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 11 | 21.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 7.8% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 4 | 7.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17** | 3 | 1 | 2 | **`66.67%`** | `0.0%` | `-63.0s` |
| **Route 11** | 2 | 1 | 1 | **`50.0%`** | `100.0%` | `+1.1m` |
| **Route 14** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-63.5s` |
| **Route 18** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.5m` |
| **Route 2** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-26.5s` |
| **Route 22** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+1.8m` |
| **Route 3** | 5 | 5 | 0 | **`0.0%`** | `100.0%` | `+1.0m` |
| **Route 4** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `-59.0s` |
| **Route 5** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `-106.5s` |
| **Route 62** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `-31.5s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 923** | `+6.6 min (398.7s)` | `+12.9 min (774s)` | 2 | `33.33%` |
| **Route 922** | `+2.6 min (157.7s)` | `+6.8 min (406s)` | 3 | `66.67%` |
| **Route 74** | `+2.2 min (134.0s)` | `+2.2 min (134s)` | 1 | `100.0%` |
| **Route 924** | `+2.0 min (121.7s)` | `+8.5 min (508s)` | 3 | `0.0%` |
| **Route 921** | `+2.0 min (120.0s)` | `+4.1 min (245s)` | 2 | `100.0%` |
| **Route 22** | `+1.8 min (108.5s)` | `+3.0 min (178s)` | 2 | `100.0%` |
| **Route 18** | `+1.5 min (92.0s)` | `+2.3 min (137s)` | 2 | `100.0%` |
| **Route 515** | `+1.5 min (89.0s)` | `+1.5 min (89s)` | 1 | `100.0%` |
| **Route 11** | `+1.1 min (63.0s)` | `+1.1 min (63s)` | 1 | `100.0%` |
| **Route 906** | `+1.0 min (60.0s)` | `+1.0 min (60s)` | 1 | `100.0%` |

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
| `1135133` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349023` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1136096` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1318865` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-18 06:08:06` | `7.84%` | `68.09%` | 51 | 47 | `+40.8s` |
| `2026-09-18 01:00:45` | `15.29%` | `66.8%` | 595 | 494 | `+67.2s` |
| `2026-09-17 22:57:58` | `14.59%` | `51.39%` | 905 | 755 | `+97.9s` |
| `2026-09-17 20:26:25` | `17.07%` | `57.79%` | 1113 | 905 | `+61.3s` |
| `2026-09-17 17:10:31` | `17.58%` | `56.41%` | 927 | 745 | `+-5.7s` |
| `2026-09-17 12:18:36` | `15.82%` | `61.21%` | 967 | 812 | `+9.9s` |
| `2026-09-17 06:55:00` | `0.0%` | `100.0%` | 18 | 7 | `+53.1s` |
| `2026-09-17 01:33:58` | `15.52%` | `64.73%` | 567 | 448 | `+104.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-18T06:08:06.647145+00:00`.*
