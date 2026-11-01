# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Hamilton Street Railway** in **Hamilton, ON** (City of Hamilton, Ontario).
> **Transit System:** HSR | **Location:** Hamilton, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-11-01T07:00:18.719000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`99.41%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `170` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `1` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `169` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+0.0s` (`+0.0 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+0.0s` (`+0.0 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 0 | 0.0% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 0 | 0.0% |
| 🟡 **Minor Delay** | +5m to +15m late | 0 | 0.0% |
| 🔴 **Severe Delay** | Over 15m late | 0 | 0.0% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 169 | 99.4% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 5782** | 72 | 0 | 72 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5783** | 59 | 0 | 59 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 5795** | 37 | 0 | 37 | **`100.0%`** | `0.0%` | `+0.0s` |

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
| `2198175` | Route 5808 | `26:30:00` | `SCHEDULED` | Assigned vehicle 3681 is missing from active GPS transponder fleet |
| `2194132` | Route 5795 | `13:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194152` | Route 5795 | `23:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194136` | Route 5795 | `14:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194139` | Route 5795 | `16:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194144` | Route 5795 | `17:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194118` | Route 5795 | `19:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194146` | Route 5795 | `20:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194149` | Route 5795 | `22:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194119` | Route 5795 | `08:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194124` | Route 5795 | `10:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194131` | Route 5795 | `11:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194153` | Route 5795 | `24:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194128` | Route 5795 | `07:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2194127` | Route 5795 | `19:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 📈 Recent Reliability Trend (Git-Scraping History)

| Timestamp | Ghost Rate (%) | On-Time (%) | Scheduled Runs | Tracked Fleet | Mean Delay |
| :--- | :---: | :---: | :---: | :---: | :---: |
| `2026-11-01 07:00:18` | `99.41%` | `0.0%` | 170 | 1 | `+0.0s` |
| `2026-11-01 06:30:18` | `99.42%` | `0.0%` | 172 | 2 | `+0.0s` |
| `2026-11-01 06:00:20` | `92.82%` | `0.0%` | 181 | 15 | `+3854.0s` |
| `2026-11-01 05:30:19` | `82.52%` | `0.0%` | 206 | 39 | `+3951.6s` |
| `2026-11-01 05:00:20` | `70.83%` | `0.0%` | 240 | 70 | `+3805.6s` |
| `2026-11-01 04:30:19` | `68.36%` | `83.33%` | 256 | 81 | `+127.1s` |
| `2026-11-01 04:00:18` | `11.11%` | `81.82%` | 99 | 88 | `+126.8s` |
| `2026-11-01 03:30:18` | `15.32%` | `78.57%` | 111 | 94 | `+261.4s` |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-11-01T07:00:18.719000+00:00`.*
