# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Central Florida Regional Transportation Authority** in **Orlando, FL** (Orlando Metropolitan Area, Florida).
> **Transit System:** LYNX | **Location:** Orlando, FL | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-30T04:30:18.027000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`3.33%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`55.17%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `30` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `25` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `1` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+369.1s` (`+6.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+232.0s` (`+3.9 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 16 | 53.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 10 | 33.3% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 10.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 1 | 3.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 17574** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+9.9 min` |
| **Route 17567** | 7 | 5 | 0 | **`0.0%`** | `71.43%` | `+3.3 min` |
| **Route 17585** | 3 | 3 | 0 | **`0.0%`** | `66.67%` | `+4.9 min` |
| **Route 17579** | 3 | 2 | 0 | **`0.0%`** | `66.67%` | `+2.6 min` |
| **Route 17608** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+14.6 min` |
| **Route 17604** | 2 | 2 | 0 | **`0.0%`** | `100.0%` | `+3.1 min` |
| **Route 17600** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+9.2 min` |
| **Route 17591** | 2 | 1 | 0 | **`0.0%`** | `100.0%` | `+0.0 min` |
| **Route 17602** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+11.4 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 17603** | `+20.3 min (+1216.0s)` | `+20.3 min (+1216s)` | 1 | `0.0%` |
| **Route 17608** | `+14.6 min (+877.5s)` | `+16.0 min (+958s)` | 2 | `0.0%` |
| **Route 17583** | `+14.6 min (+875.0s)` | `+14.6 min (+875s)` | 1 | `0.0%` |
| **Route 17602** | `+11.4 min (+684.0s)` | `+20.9 min (+1253s)` | 2 | `50.0%` |
| **Route 17574** | `+9.9 min (+597.0s)` | `+9.9 min (+597s)` | 1 | `0.0%` |
| **Route 17600** | `+9.2 min (+554.5s)` | `+11.6 min (+696s)` | 2 | `0.0%` |
| **Route 17614** | `+7.5 min (+447.0s)` | `+7.5 min (+447s)` | 1 | `0.0%` |
| **Route 17585** | `+4.9 min (+296.7s)` | `+11.1 min (+664s)` | 3 | `66.67%` |
| **Route 17577** | `+3.5 min (+207.0s)` | `+3.5 min (+207s)` | 1 | `100.0%` |
| **Route 17567** | `+3.3 min (+200.9s)` | `+8.9 min (+534s)` | 5 | `71.43%` |

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
| `2200213` | Route 17574 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-10-30 04:30:18` | `3.33%` | `55.17%` | 30 | 25 | `+369.1s` |
| `2026-10-30 03:30:18` | `5.88%` | `79.49%` | 85 | 53 | `+233.0s` |
| `2026-10-30 02:00:18` | `3.02%` | `79.56%` | 232 | 99 | `+192.2s` |
| `2026-10-30 01:00:18` | `2.37%` | `85.45%` | 338 | 123 | `+91.0s` |
| `2026-10-29 23:30:26` | `0.19%` | `83.88%` | 525 | 166 | `+189.3s` |
| `2026-10-29 23:00:18` | `1.68%` | `82.44%` | 597 | 180 | `+212.6s` |
| `2026-10-29 22:30:18` | `2.56%` | `79.59%` | 665 | 189 | `+230.0s` |
| `2026-10-29 22:00:18` | `2.49%` | `80.51%` | 684 | 189 | `+209.5s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-30T04:30:18.027000+00:00`.*
