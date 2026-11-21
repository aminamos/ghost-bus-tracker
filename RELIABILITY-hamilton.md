# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-21T07:00:18.754000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`95.28%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `212` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `11` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `202` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `-73.0s` (`-1.2 min`) | Average delay across all active tracked runs |
| **Median Delay** | `-73.0s` (`-1.2 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.5% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 202 | 95.3% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5794** | 39 | 0 | 39 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5782** | 97 | 1 | 96 | **`98.97%`** | `0.0%` | `-73.0s` |
| **Route 5783** | 68 | 2 | 66 | **`97.06%`** | `0.0%` | `+0.0s` |
| **Route 5808** | 2 | 2 | 0 | **`0.0%`** | `0.0%` | `+0.0s` |

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
| `2199317` | Route 5813 | `26:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193757` | Route 5794 | `23:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193760` | Route 5794 | `22:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193763` | Route 5794 | `20:50:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193766` | Route 5794 | `19:20:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193769` | Route 5794 | `17:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193773` | Route 5794 | `15:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193777` | Route 5794 | `13:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193781` | Route 5794 | `11:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193785` | Route 5794 | `09:44:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193770` | Route 5794 | `17:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193774` | Route 5794 | `15:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193778` | Route 5794 | `13:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193782` | Route 5794 | `11:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2193786` | Route 5794 | `09:14:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-21 07:00:18` | `95.28%` | `0.0%` | 212 | 11 | `-73.0s` |
| `2026-11-21 06:00:18` | `71.89%` | `100.0%` | 281 | 78 | `+54.6s` |
| `2026-11-21 05:30:18` | `70.55%` | `100.0%` | 292 | 87 | `+31.0s` |
| `2026-11-21 05:00:20` | `6.12%` | `85.71%` | 98 | 91 | `+147.0s` |
| `2026-11-21 04:30:18` | `7.92%` | `85.71%` | 101 | 92 | `+118.7s` |
| `2026-11-21 04:00:18` | `10.28%` | `85.71%` | 107 | 94 | `+117.6s` |
| `2026-11-21 03:30:18` | `12.17%` | `87.5%` | 115 | 100 | `+136.5s` |
| `2026-11-21 03:00:18` | `13.95%` | `87.5%` | 129 | 110 | `+175.8s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-21T07:00:18.754000+00:00`.*
