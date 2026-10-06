# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-10-06T00:28:46.366513+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`9.69%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`67.95%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `650` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `547` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `63` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+74.2s` (`+1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+26.5s` (`+0.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 371 | 57.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 108 | 16.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 63 | 9.7% |
| 🔴 **Severe Delay** | Over 15m late | 4 | 0.6% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 63 | 9.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 40 | 6.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 540** | 10 | 6 | 4 | **`40.0%`** | `66.67%` | `+0.2 min` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `66.67%` | `+0.7 min` |
| **Route 721** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+1.5 min` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `42.86%` | `+0.4 min` |
| **Route 18** | 26 | 12 | 8 | **`30.77%`** | `55.56%` | `+2.6 min` |
| **Route 10** | 18 | 8 | 5 | **`27.78%`** | `66.67%` | `+3.1 min` |
| **Route 924** | 29 | 14 | 8 | **`27.59%`** | `42.86%` | `+2.6 min` |
| **Route 723** | 4 | 2 | 1 | **`25.0%`** | `66.67%` | `+5.2 min` |
| **Route 538** | 9 | 3 | 2 | **`22.22%`** | `71.43%` | `+1.3 min` |
| **Route 67** | 9 | 4 | 2 | **`22.22%`** | `71.43%` | `+2.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 22** | `+6.4 min (+383.9s)` | `+38.5 min (+2312s)` | 13 | `33.33%` |
| **Route 723** | `+5.2 min (+311.0s)` | `+14.5 min (+869s)` | 2 | `66.67%` |
| **Route 904** | `+4.4 min (+261.9s)` | `+8.4 min (+502s)` | 8 | `64.29%` |
| **Route 923** | `+3.5 min (+209.6s)` | `+14.9 min (+892s)` | 9 | `50.0%` |
| **Route 2** | `+3.5 min (+207.4s)` | `+10.1 min (+608s)` | 8 | `58.33%` |
| **Route 10** | `+3.1 min (+184.7s)` | `+15.4 min (+925s)` | 8 | `66.67%` |
| **Route 345** | `+3.0 min (+182.0s)` | `+3.1 min (+186s)` | 2 | `100.0%` |
| **Route 902** | `+2.8 min (+166.7s)` | `+8.5 min (+510s)` | 9 | `77.78%` |
| **Route 72** | `+2.7 min (+161.0s)` | `+3.3 min (+199s)` | 1 | `100.0%` |
| **Route 924** | `+2.6 min (+157.0s)` | `+11.4 min (+685s)` | 14 | `42.86%` |

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
| `1325612` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325635` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325968` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326793` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326951` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364366` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366220` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332019` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1332593` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1131636` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1135815` | Route 17 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360851` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1360980` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361300` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1361513` | Route 18 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-06 00:28:46` | `9.69%` | `67.95%` | 650 | 547 | `+74.2s` |
| `2026-10-05 18:39:11` | `13.83%` | `56.53%` | 962 | 749 | `+13.5s` |
| `2026-10-05 18:02:18` | `12.71%` | `58.11%` | 952 | 752 | `+37.7s` |
| `2026-10-05 17:57:47` | `12.3%` | `58.16%` | 943 | 748 | `+38.7s` |
| `2026-10-05 17:20:37` | `12.38%` | `58.27%` | 945 | 762 | `+20.1s` |
| `2026-10-05 16:34:15` | `12.45%` | `58.06%` | 932 | 751 | `+17.6s` |
| `2026-10-05 12:15:23` | `10.84%` | `63.85%` | 950 | 805 | `+30.8s` |
| `2026-10-05 12:14:27` | `11.02%` | `64.16%` | 944 | 798 | `+31.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-06T00:28:46.366513+00:00`.*
