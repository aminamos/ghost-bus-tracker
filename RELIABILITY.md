# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Metro Transit (Twin Cities)** in **Minneapolis–Saint Paul, MN** (Twin Cities Metropolitan Area, Minnesota).
> **Transit System:** Metro Transit | **Location:** Minneapolis–Saint Paul, MN | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T15:01:09.032000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`16.82%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`53.5%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `886` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `714` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `149` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-4.2s` (`-0.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-30.0s` (`-0.5 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 382 | 43.1% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 285 | 32.2% |
| 🟡 **Minor Delay** | +5m to +15m late | 45 | 5.1% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 0.2% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 149 | 16.8% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 23 | 2.6% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 537** | 4 | 1 | 2 | **`50.0%`** | `50.0%` | `-19.0s` |
| **Route 827** | 4 | 2 | 2 | **`50.0%`** | `50.0%` | `-52.5s` |
| **Route 534** | 10 | 2 | 4 | **`40.0%`** | `100.0%` | `+0.3 min` |
| **Route 539** | 10 | 4 | 4 | **`40.0%`** | `83.33%` | `+0.2 min` |
| **Route 540** | 10 | 4 | 4 | **`40.0%`** | `33.33%` | `-104.7s` |
| **Route 215** | 5 | 1 | 2 | **`40.0%`** | `100.0%` | `-4.7s` |
| **Route 18** | 31 | 14 | 12 | **`38.71%`** | `57.89%` | `+0.7 min` |
| **Route 14** | 22 | 10 | 8 | **`36.36%`** | `28.57%` | `-79.1s` |
| **Route 64** | 23 | 11 | 8 | **`34.78%`** | `40.0%` | `-31.1s` |
| **Route 9** | 12 | 6 | 4 | **`33.33%`** | `62.5%` | `+0.6 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 5** | `+4.1 min (+248.4s)` | `+15.4 min (+927s)` | 3 | `20.0%` |
| **Route 716** | `+2.5 min (+150.3s)` | `+7.9 min (+472s)` | 1 | `66.67%` |
| **Route 904** | `+2.3 min (+139.2s)` | `+4.7 min (+282s)` | 7 | `100.0%` |
| **Route 54** | `+2.0 min (+121.2s)` | `+19.1 min (+1143s)` | 12 | `62.5%` |
| **Route 698** | `+2.0 min (+118.0s)` | `+7.4 min (+445s)` | 3 | `33.33%` |
| **Route 901** | `+1.9 min (+116.2s)` | `+10.0 min (+600s)` | 8 | `87.5%` |
| **Route 725** | `+1.9 min (+112.2s)` | `+6.2 min (+373s)` | 2 | `50.0%` |
| **Route 94** | `+1.9 min (+111.8s)` | `+6.2 min (+371s)` | 6 | `88.89%` |
| **Route 48** | `+1.8 min (+110.7s)` | `+9.8 min (+586s)` | 2 | `0.0%` |
| **Route 921** | `+1.7 min (+101.4s)` | `+7.3 min (+439s)` | 7 | `78.57%` |

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
| `1131079` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1133176` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1133574` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1133782` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1134479` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1135459` | Route 10 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1317937` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319460` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319548` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1319585` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1364230` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1365001` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366056` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1366639` | Route 11 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `1331033` | Route 14 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-22 15:01:09` | `16.82%` | `53.5%` | 886 | 714 | `-4.2s` |
| `2026-10-22 13:31:54` | `15.92%` | `57.37%` | 911 | 760 | `+35.3s` |
| `2026-10-22 13:03:21` | `14.75%` | `60.8%` | 949 | 801 | `+39.5s` |
| `2026-10-22 12:30:37` | `14.21%` | `67.22%` | 985 | 836 | `+39.0s` |
| `2026-10-22 12:00:40` | `14.89%` | `65.16%` | 967 | 818 | `+11.8s` |
| `2026-10-22 11:30:35` | `16.47%` | `61.36%` | 923 | 766 | `-1.0s` |
| `2026-10-22 11:00:35` | `18.77%` | `59.72%` | 794 | 650 | `-9.5s` |
| `2026-10-22 10:30:35` | `22.04%` | `61.73%` | 667 | 520 | `-15.1s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T15:01:09.032000+00:00`.*
