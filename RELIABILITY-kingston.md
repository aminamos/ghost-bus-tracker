# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Kingston Transit** in **Kingston, ON** (City of Kingston, Ontario).
> **Transit System:** Kingston | **Location:** Kingston, ON | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:50.217000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`77.65%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`74.14%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `264` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `135` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `205` | Disappeared or unassigned scheduled runs |
| **Mean Delay** | `+228.8s` (`+3.8 min`) | Average delay across all active tracked runs |
| **Median Delay** | `+105.0s` (`+1.8 min`) | Median schedule deviation |

---

## ⏱️ Delay & Reliability Breakdown

| Category | Threshold / Definition | Trip Count | Percentage |
| :--- | :--- | :--- | :--- |
| 🟢 **On-Time** | Within -60s to +300s | 43 | 16.3% |
| ⏩ **Early Departure** | More than 1 min ahead of schedule | 1 | 0.4% |
| 🟡 **Minor Delay** | +5m to +15m late | 11 | 4.2% |
| 🔴 **Severe Delay** | Over 15m late | 3 | 1.1% |
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 205 | 77.7% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route 19A** | 7 | 0 | 7 | **`100.0%`** | `0.0%` | `+0.0s` |
| **Route 22** | 10 | 1 | 9 | **`90.0%`** | `0.0%` | `-241.0s` |
| **Route 601** | 10 | 1 | 9 | **`90.0%`** | `100.0%` | `+4.6 min` |
| **Route 7** | 18 | 4 | 15 | **`83.33%`** | `50.0%` | `+6.2 min` |
| **Route 802** | 6 | 1 | 5 | **`83.33%`** | `100.0%` | `+0.0s` |
| **Route 801** | 6 | 1 | 5 | **`83.33%`** | `100.0%` | `+1.4 min` |
| **Route 14** | 6 | 1 | 5 | **`83.33%`** | `0.0%` | `+7.8 min` |
| **Route 702** | 17 | 3 | 14 | **`82.35%`** | `100.0%` | `+3.2 min` |
| **Route 501** | 22 | 4 | 18 | **`81.82%`** | `100.0%` | `+1.6 min` |
| **Route 6** | 11 | 2 | 9 | **`81.82%`** | `50.0%` | `+8.9 min` |

---

## 🐌 Most Delayed Routes

| Route | Avg Delay | Max Delay | Tracked Runs | On-Time Adherence |
| :--- | :---: | :---: | :---: | :---: |
| **Route 602** | `+14.3 min (+857.3s)` | `+27.3 min (+1636s)` | 3 | `0.0%` |
| **Route 6** | `+8.9 min (+535.0s)` | `+15.7 min (+944s)` | 2 | `50.0%` |
| **Route 13** | `+7.9 min (+474.0s)` | `+7.9 min (+474s)` | 1 | `0.0%` |
| **Route 14** | `+7.8 min (+468.0s)` | `+7.8 min (+468s)` | 1 | `0.0%` |
| **Route 502** | `+7.5 min (+448.0s)` | `+21.2 min (+1271s)` | 4 | `50.0%` |
| **Route 32** | `+7.0 min (+421.5s)` | `+10.2 min (+609s)` | 2 | `50.0%` |
| **Route 7** | `+6.2 min (+370.0s)` | `+7.6 min (+454s)` | 4 | `50.0%` |
| **Route 1** | `+5.0 min (+301.0s)` | `+12.9 min (+776s)` | 3 | `66.67%` |
| **Route 601** | `+4.6 min (+277.0s)` | `+4.6 min (+277s)` | 1 | `100.0%` |
| **Route 16** | `+4.2 min (+251.3s)` | `+10.7 min (+642s)` | 3 | `66.67%` |

---

## ⏱️ Headway Regularity & Excess Wait Time (EWT)

> **Excess Wait Time (EWT)** quantifies how much additional time passengers wait due to bus bunching or irregular headways beyond the scheduled interval.

| Route | Nominal Headway | Observed Headway | Excess Wait Time (EWT) | Regularity Score |
| :--- | :---: | :---: | :---: | :---: |
| **Route 502** | ~9.0m | ~9.0m | **`+0.1 min`** | `7.6 / 100` |
| **Route 602** | ~15.0m | ~15.0m | **`+0.0 min`** | `38.1 / 100` |
| **Route 6** | ~15.0m | ~15.0m | **`+0.0 min`** | `54.6 / 100` |
| **Route 1** | ~15.0m | ~15.0m | **`+0.0 min`** | `62.5 / 100` |
| **Route 16** | ~15.0m | ~15.0m | **`+0.0 min`** | `69.3 / 100` |
| **Route 2** | ~26.0m | ~26.0m | **`+0.0 min`** | `78.9 / 100` |
| **Route 701** | ~9.0m | ~9.0m | **`+0.0 min`** | `73.1 / 100` |
| **Route 501** | ~6.0m | ~6.0m | **`+0.0 min`** | `67.4 / 100` |
| **Route 7** | ~5.0m | ~5.0m | **`+0.0 min`** | `72.0 / 100` |
| **Route 32** | ~30.0m | ~30.0m | **`+0.0 min`** | `89.6 / 100` |

---

## 👻 Active Ghost Trips Sample

| Trip ID | Route | Scheduled Departure | Status | Diagnosis / Reason |
| :--- | :---: | :---: | :--- | :--- |
| `2291835:665953:667081` | Route 16 | `15:25:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2292377:664089:667081` | Route 6 | `16:00:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291879:661668:667081` | Route 501 | `16:36:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291940:665464:667081` | Route 501 | `17:09:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291690:663621:667086` | Route 602 | `15:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291683:661890:667086` | Route 601 | `15:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291694:664143:667086` | Route 602 | `16:18:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291687:665039:667086` | Route 601 | `16:52:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291269:662851:667174` | Route 15 | `16:02:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291982:664044:667174` | Route 4 | `17:10:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291002:665056:667266` | Route 31 | `15:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291043:665880:667266` | Route 31 | `16:30:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291686:665424:667293` | Route 601 | `15:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291689:663678:667293` | Route 602 | `15:48:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |
| `2291684:665890:667293` | Route 601 | `16:22:00` | `SCHEDULED` | No vehicle assigned and no active GPS broadcast |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:50.217000+00:00`.*
