# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)**.
> **Status:** 🟡 **ELEVATED GHOSTS** | **Last Scan:** `2026-09-17T22:57:58.221608+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`14.59%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`51.39%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `905` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `755` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `132` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+97.9s` (`1.6 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 388 | 42.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 241 | 26.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 106 | 11.7% |
| 🔴 **Severe Delay** | Over 15m late | 20 | 2.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 132 | 14.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 18 | 2.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 25** | 7 | 2 | 4 | **`57.14%`** | `50.0%` | `+1.5m` |
| **Route 723** | 4 | 2 | 2 | **`50.0%`** | `100.0%` | `-30.0s` |
| **Route 18** | 27 | 14 | 13 | **`48.15%`** | `100.0%` | `+0.7m` |
| **Route 64** | 21 | 10 | 9 | **`42.86%`** | `88.89%` | `+0.8m` |
| **Route 223** | 7 | 2 | 3 | **`42.86%`** | `100.0%` | `-83.8s` |
| **Route 538** | 10 | 3 | 4 | **`40.0%`** | `100.0%` | `-2.8s` |
| **Route 65** | 10 | 4 | 4 | **`40.0%`** | `100.0%` | `-66.3s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `+0.4m` |
| **Route 36** | 11 | 5 | 4 | **`36.36%`** | `83.33%` | `+1.4m` |
| **Route 540** | 11 | 6 | 4 | **`36.36%`** | `71.43%` | `+2.7m` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 363** | `+100.0 min (6002.0s)` | `+100.0 min (6002s)` | 1 | `0.0%` |
| **Route 667** | `+27.8 min (1669.0s)` | `+27.8 min (1669s)` | 1 | `0.0%` |
| **Route 467** | `+11.9 min (712.5s)` | `+12.3 min (736s)` | 2 | `0.0%` |
| **Route 882** | `+9.8 min (589.0s)` | `+9.8 min (589s)` | 1 | `0.0%` |
| **Route 747** | `+6.9 min (415.0s)` | `+13.6 min (818s)` | 3 | `0.0%` |
| **Route 355** | `+6.9 min (412.0s)` | `+6.9 min (412s)` | 1 | `0.0%` |
| **Route 645** | `+6.5 min (389.6s)` | `+26.4 min (1584s)` | 6 | `40.0%` |
| **Route 54** | `+5.7 min (343.8s)` | `+27.0 min (1622s)` | 12 | `57.14%` |
| **Route 673** | `+5.5 min (328.0s)` | `+10.3 min (617s)` | 1 | `50.0%` |
| **Route 10** | `+5.3 min (315.6s)` | `+44.9 min (2696s)` | 15 | `60.0%` |

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
| `1325105` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325247` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1325594` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326072` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326110` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326499` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326527` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326585` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326726` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1326779` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319708` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1349633` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350049` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1350618` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331262` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-09-17 22:57:58` | `14.59%` | `51.39%` | 905 | 755 | `+97.9s` |
| `2026-09-17 20:26:25` | `17.07%` | `57.79%` | 1113 | 905 | `+61.3s` |
| `2026-09-17 17:10:31` | `17.58%` | `56.41%` | 927 | 745 | `+-5.7s` |
| `2026-09-17 12:18:36` | `15.82%` | `61.21%` | 967 | 812 | `+9.9s` |
| `2026-09-17 06:55:00` | `0.0%` | `100.0%` | 18 | 7 | `+53.1s` |
| `2026-09-17 01:33:58` | `15.52%` | `64.73%` | 567 | 448 | `+104.1s` |
| `2026-09-16 23:04:33` | `14.18%` | `47.86%` | 910 | 746 | `+188.2s` |
| `2026-09-16 20:17:29` | `17.56%` | `58.39%` | 1105 | 883 | `+35.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-09-17T22:57:58.221608+00:00`.*
