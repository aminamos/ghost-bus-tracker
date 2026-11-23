# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Edmonton Transit Service** in **Edmonton, AB** (Edmonton Metropolitan Region, Alberta).
> **Transit System:** ETS | **Location:** Edmonton, AB | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-23T07:00:19.455000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`22.95%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`80.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `61` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `24` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `14` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+60.8s` (`+1.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+13.0s` (`+0.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 32 | 52.5% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 4 | 6.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 4 | 6.6% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 14 | 23.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 511** | 7 | 2 | 4 | **`57.14%`** | `100.0%` | `+2.8 min` |
| **Route 004** | 14 | 5 | 4 | **`28.57%`** | `100.0%` | `+1.2 min` |
| **Route 009** | 12 | 4 | 3 | **`25.0%`** | `57.14%` | `+3.5 min` |
| **Route 002** | 14 | 5 | 3 | **`21.43%`** | `100.0%` | `+0.1 min` |
| **Route 008** | 8 | 4 | 0 | **`0.0%`** | `62.5%` | `-65.8s` |
| **Route 051** | 2 | 1 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 103** | `+9.1 min (+548.0s)` | `+9.1 min (+548s)` | 1 | `0.0%` |
| **Route 009** | `+3.5 min (+211.1s)` | `+6.4 min (+385s)` | 4 | `57.14%` |
| **Route 511** | `+2.8 min (+165.0s)` | `+2.8 min (+165s)` | 2 | `100.0%` |
| **Route 004** | `+1.2 min (+74.2s)` | `+4.0 min (+240s)` | 5 | `100.0%` |
| **Route 055** | `+0.6 min (+34.0s)` | `+0.6 min (+34s)` | 1 | `100.0%` |
| **Route 002** | `+0.1 min (+7.3s)` | `+0.7 min (+42s)` | 5 | `100.0%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.1 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `94.3 / 100` |
| **Route 009** | ~30.0m | ~30.0m | **`+0.0 min`** | `95.5 / 100` |
| **Route 004** | ~30.0m | ~30.0m | **`+0.0 min`** | `97.7 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.2 / 100` |
| **Route 008** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.3 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `98.8 / 100` |
| **Route 002** | ~30.0m | ~30.0m | **`+0.0 min`** | `99.3 / 100` |
| **Route 511** | ~30.0m | ~30.0m | **`+0.0 min`** | `100.0 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `32754189` | Route 004 | `25:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32752872` | Route 511 | `25:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753578` | Route 002 | `25:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32752874` | Route 511 | `26:05:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753581` | Route 002 | `26:34:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754197` | Route 004 | `26:51:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754188` | Route 004 | `25:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753940` | Route 009 | `25:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753941` | Route 009 | `26:08:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753942` | Route 009 | `26:38:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32752875` | Route 511 | `26:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32752873` | Route 511 | `25:35:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32754190` | Route 004 | `26:21:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `32753579` | Route 002 | `26:04:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-23 07:00:19` | `22.95%` | `80.0%` | 61 | 24 | `+60.8s` |
| `2026-11-23 06:30:18` | `23.53%` | `67.8%` | 85 | 44 | `+33.3s` |
| `2026-11-23 06:00:23` | `16.79%` | `73.74%` | 131 | 77 | `+27.7s` |
| `2026-11-23 05:30:19` | `15.68%` | `74.5%` | 185 | 90 | `+10.3s` |
| `2026-11-23 05:00:24` | `16.81%` | `81.22%` | 226 | 105 | `+36.9s` |
| `2026-11-23 04:30:24` | `18.18%` | `75.0%` | 253 | 110 | `+85.0s` |
| `2026-11-23 04:00:23` | `19.43%` | `77.38%` | 283 | 122 | `+89.5s` |
| `2026-11-23 03:30:18` | `21.94%` | `77.45%` | 310 | 129 | `+63.6s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-23T07:00:19.455000+00:00`.*
