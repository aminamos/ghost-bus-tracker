# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **London Transit Commission** in **London, ON** (City of London, Ontario).
> **Transit System:** London | **Location:** London, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:53.252000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`73.67%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`58.7%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `1409` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `184` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1038` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+347.8s` (`+5.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+59.5s` (`+1.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 216 | 15.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 34 | 2.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 63 | 4.5% |
| 🔴 **Severe Delay** | Over 15m late | 55 | 3.9% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1038 | 73.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 3 | 0.2% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 36** | 34 | 2 | 30 | **`88.24%`** | `0.0%` | `+18.2 min` |
| **Route 30** | 17 | 1 | 15 | **`88.24%`** | `0.0%` | `+25.7 min` |
| **Route 25** | 57 | 4 | 50 | **`87.72%`** | `14.29%` | `+5.8 min` |
| **Route 35** | 14 | 1 | 12 | **`85.71%`** | `100.0%` | `-7.5s` |
| **Route 34** | 34 | 3 | 28 | **`82.35%`** | `50.0%` | `+6.4 min` |
| **Route 33** | 33 | 3 | 27 | **`81.82%`** | `50.0%` | `+0.5 min` |
| **Route 09** | 62 | 6 | 50 | **`80.65%`** | `83.33%` | `-31.4s` |
| **Route 31** | 30 | 3 | 24 | **`80.0%`** | `50.0%` | `+4.1 min` |
| **Route 16** | 68 | 7 | 54 | **`79.41%`** | `57.14%` | `+0.2 min` |
| **Route 04** | 70 | 8 | 55 | **`78.57%`** | `60.0%` | `+3.1 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 30** | `+25.7 min (+1542.0s)` | `+32.6 min (+1959s)` | 1 | `0.0%` |
| **Route 127** | `+23.1 min (+1385.7s)` | `+42.5 min (+2553s)` | 5 | `10.0%` |
| **Route 94** | `+22.7 min (+1363.1s)` | `+33.2 min (+1992s)` | 4 | `0.0%` |
| **Route 106** | `+22.7 min (+1361.7s)` | `+42.1 min (+2529s)` | 5 | `18.18%` |
| **Route 02** | `+19.9 min (+1192.0s)` | `+49.6 min (+2975s)` | 10 | `20.0%` |
| **Route 93** | `+18.6 min (+1113.3s)` | `+38.3 min (+2297s)` | 6 | `0.0%` |
| **Route 36** | `+18.2 min (+1089.2s)` | `+24.2 min (+1450s)` | 2 | `0.0%` |
| **Route 27** | `+10.6 min (+634.1s)` | `+31.2 min (+1871s)` | 9 | `42.86%` |
| **Route 90** | `+6.8 min (+405.7s)` | `+23.4 min (+1407s)` | 6 | `58.33%` |
| **Route 34** | `+6.4 min (+384.7s)` | `+24.7 min (+1480s)` | 3 | `50.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 02** | ~8.0m | ~8.0m | **`+0.2 min`** | `0.0 / 100` |
| **Route 106** | ~10.0m | ~10.0m | **`+0.2 min`** | `0.0 / 100` |
| **Route 106** | ~12.5m | ~12.5m | **`+0.1 min`** | `0.0 / 100` |
| **Route 27** | ~12.5m | ~12.5m | **`+0.1 min`** | `3.4 / 100` |
| **Route 127** | ~16.0m | ~16.0m | **`+0.1 min`** | `15.9 / 100` |
| **Route 93** | ~18.5m | ~18.5m | **`+0.1 min`** | `36.0 / 100` |
| **Route 127** | ~22.0m | ~22.0m | **`+0.1 min`** | `44.8 / 100` |
| **Route 93** | ~27.0m | ~27.0m | **`+0.0 min`** | `56.2 / 100` |
| **Route 24** | ~10.5m | ~10.5m | **`+0.0 min`** | `32.6 / 100` |
| **Route 90** | ~16.0m | ~16.0m | **`+0.0 min`** | `49.2 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2385419` | Route 01 | `16:06:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385361` | Route 01 | `16:55:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385426` | Route 01 | `17:57:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385364` | Route 01 | `18:41:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385428` | Route 01 | `19:37:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385366` | Route 01 | `20:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385356` | Route 01 | `16:07:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385421` | Route 01 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385363` | Route 01 | `17:56:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385427` | Route 01 | `18:47:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385365` | Route 01 | `19:31:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385429` | Route 01 | `20:27:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385375` | Route 01 | `21:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385436` | Route 01 | `21:59:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2385374` | Route 01 | `22:39:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:53.252000+00:00`.*
