# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-28T07:00:20.257000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`94.58%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `166` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `9` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `157` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-84.0s` (`-1.4 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-84.0s` (`-1.4 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.6% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 157 | 94.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5813** | 2 | 0 | 2 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 51 | 1 | 50 | **`98.04%`** | `0.0%` | `-84.0s` |
| **Route 5783** | 68 | 2 | 66 | **`97.06%`** | `0.0%` | `+0.0s` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| *All active tracked routes currently operating within nominal bounds* | - | - | - | - |

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
| `2199316` | Route 5813 | `26:32:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2199317` | Route 5813 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193781` | Route 5794 | `11:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193777` | Route 5794 | `13:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193773` | Route 5794 | `15:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193769` | Route 5794 | `17:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193766` | Route 5794 | `19:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193763` | Route 5794 | `20:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193760` | Route 5794 | `22:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193793` | Route 5794 | `05:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193790` | Route 5794 | `07:15:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193787` | Route 5794 | `08:45:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193783` | Route 5794 | `10:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193779` | Route 5794 | `12:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193775` | Route 5794 | `14:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-28 07:00:20` | `94.58%` | `0.0%` | 166 | 9 | `-84.0s` |
| `2026-11-28 06:30:17` | `76.7%` | `66.67%` | 206 | 48 | `-45.3s` |
| `2026-11-28 06:00:18` | `67.09%` | `50.0%` | 234 | 76 | `+316.2s` |
| `2026-11-28 05:30:20` | `64.78%` | `90.0%` | 247 | 86 | `+194.4s` |
| `2026-11-28 05:00:19` | `7.07%` | `100.0%` | 99 | 91 | `+72.3s` |
| `2026-11-28 04:30:17` | `9.8%` | `77.78%` | 102 | 91 | `+145.0s` |
| `2026-11-28 04:00:19` | `11.21%` | `81.82%` | 107 | 93 | `+213.6s` |
| `2026-11-28 03:30:19` | `13.91%` | `100.0%` | 115 | 99 | `+35.2s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-28T07:00:20.257000+00:00`.*
