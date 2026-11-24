# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Valley Metro** in **Phoenix, AZ** (Phoenix–Mesa Metropolitan Area, Arizona).
> **Transit System:** Valley Metro | **Location:** Phoenix, AZ | **Status:** 🟢 **HEALTHY** | **Last Scan:** `2026-11-24T07:00:19.823000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`0.0%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`60.94%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `64` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `365` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `0` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+185.2s` (`+3.1 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+17.5s` (`+0.3 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 39 | 60.9% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 15 | 23.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 8 | 12.5% |
| 🔴 **Severe Delay** | Over 15m late | 2 | 3.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 0 | 0.0% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19** | 3 | 4 | 0 | **`0.0%`** | `66.67%` | `+1.4 min` |
| **Route 35** | 5 | 6 | 0 | **`0.0%`** | `80.0%` | `-22.4s` |
| **Route 16** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-31.5s` |
| **Route 27** | 4 | 4 | 0 | **`0.0%`** | `50.0%` | `+19.3 min` |
| **Route 3** | 3 | 3 | 0 | **`0.0%`** | `100.0%` | `+2.3 min` |
| **Route 17** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.9 min` |
| **Route 70** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.9 min` |
| **Route 50** | 2 | 3 | 0 | **`0.0%`** | `100.0%` | `+0.3 min` |
| **Route 170** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `-2.0s` |
| **Route 0** | 2 | 2 | 0 | **`0.0%`** | `50.0%` | `+0.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 43** | `+25.0 min (+1500.0s)` | `+50.7 min (+3042s)` | 3 | `50.0%` |
| **Route 27** | `+19.3 min (+1155.5s)` | `+66.9 min (+4012s)` | 4 | `50.0%` |
| **Route 75** | `+12.8 min (+770.0s)` | `+12.8 min (+770s)` | 1 | `0.0%` |
| **Route FBUZ** | `+6.6 min (+394.0s)` | `+6.6 min (+394s)` | 1 | `0.0%` |
| **Route 154** | `+5.7 min (+341.0s)` | `+5.7 min (+341s)` | 1 | `0.0%` |
| **Route 51** | `+4.8 min (+288.0s)` | `+4.8 min (+288s)` | 1 | `100.0%` |
| **Route 77** | `+4.5 min (+272.0s)` | `+10.9 min (+652s)` | 2 | `0.0%` |
| **Route 3** | `+2.3 min (+139.0s)` | `+4.5 min (+269s)` | 3 | `100.0%` |
| **Route 32** | `+2.3 min (+138.0s)` | `+2.3 min (+138s)` | 1 | `100.0%` |
| **Route S** | `+2.0 min (+120.0s)` | `+2.0 min (+120s)` | 1 | `100.0%` |

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
| *Zero ghost trips detected! All scheduled runs have verified GPS transponders.* | - | - | - | - |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-24 07:00:19` | `0.0%` | `60.94%` | 64 | 365 | `+185.2s` |
| `2026-11-24 06:30:21` | `0.65%` | `70.39%` | 153 | 407 | `+187.9s` |
| `2026-11-24 06:00:18` | `3.77%` | `77.25%` | 265 | 424 | `+119.3s` |
| `2026-11-24 05:30:18` | `3.47%` | `79.08%` | 317 | 456 | `+171.6s` |
| `2026-11-24 05:00:20` | `3.91%` | `76.45%` | 358 | 502 | `+172.7s` |
| `2026-11-24 04:30:19` | `2.69%` | `74.37%` | 409 | 525 | `+188.0s` |
| `2026-11-24 04:00:19` | `3.07%` | `76.34%` | 423 | 576 | `+171.8s` |
| `2026-11-24 03:30:26` | `3.36%` | `79.35%` | 446 | 621 | `+176.9s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-24T07:00:19.823000+00:00`.*
