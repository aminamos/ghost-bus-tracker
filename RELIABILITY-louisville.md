# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Transit Authority of River City** in **Louisville, KY** (Louisville Metropolitan Area, Kentucky).
> **Transit System:** Louisville | **Location:** Louisville, KY | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-10-22T19:17:57.288000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`3.32%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`81.19%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `211` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `67` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `7` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+152.9s` (`+2.5 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 164 | 77.7% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 30 | 14.2% |
| 🔴 **Severe Delay** | Over 15m late | 7 | 3.3% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 7 | 3.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 20** | 18 | 5 | 5 | **`27.78%`** | `76.92%` | `+3.1 min` |
| **Route 1** | 31 | 14 | 1 | **`3.23%`** | `86.67%` | `+1.7 min` |
| **Route 3** | 36 | 13 | 1 | **`2.78%`** | `80.0%` | `+2.4 min` |
| **Route 8** | 21 | 8 | 0 | **`0.0%`** | `80.95%` | `+2.8 min` |
| **Route 5** | 17 | 5 | 0 | **`0.0%`** | `82.35%` | `+1.6 min` |
| **Route 10** | 27 | 8 | 0 | **`0.0%`** | `66.67%` | `+5.5 min` |
| **Route 76** | 8 | 1 | 0 | **`0.0%`** | `71.43%` | `+2.7 min` |
| **Route 81** | 8 | 1 | 0 | **`0.0%`** | `62.5%` | `+5.9 min` |
| **Route 4** | 22 | 6 | 0 | **`0.0%`** | `95.45%` | `+0.8 min` |
| **Route 72** | 8 | 3 | 0 | **`0.0%`** | `87.5%` | `+1.0 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 81** | `+5.9 min (+352.2s)` | `+16.6 min (+994s)` | 1 | `62.5%` |
| **Route 10** | `+5.5 min (+328.5s)` | `+26.6 min (+1594s)` | 8 | `66.67%` |
| **Route 20** | `+3.1 min (+183.1s)` | `+15.0 min (+902s)` | 5 | `76.92%` |
| **Route 8** | `+2.8 min (+169.7s)` | `+18.9 min (+1133s)` | 8 | `80.95%` |
| **Route 76** | `+2.7 min (+161.7s)` | `+9.4 min (+566s)` | 1 | `71.43%` |
| **Route 3** | `+2.4 min (+146.8s)` | `+15.0 min (+901s)` | 13 | `80.0%` |
| **Route 1** | `+1.7 min (+101.1s)` | `+14.8 min (+889s)` | 14 | `86.67%` |
| **Route 5** | `+1.6 min (+98.9s)` | `+8.2 min (+495s)` | 5 | `82.35%` |
| **Route 71** | `+1.2 min (+70.2s)` | `+6.4 min (+382s)` | 3 | `87.5%` |
| **Route 72** | `+1.0 min (+59.1s)` | `+6.6 min (+397s)` | 3 | `87.5%` |

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
| `t535-b4E27-slF-vC` | Route 20 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t53B-b3F6-slF-vC` | Route 1 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t5F3-b4E91-slF-vC` | Route 20 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t5FD-b4E92-slF-vC` | Route 20 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t653-bC2B-slF-vC` | Route 3 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t6A7-b4E91-slF-vC` | Route 20 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `t6BE-b4E92-slF-vC` | Route 20 | `N/A` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:57.288000+00:00`.*
