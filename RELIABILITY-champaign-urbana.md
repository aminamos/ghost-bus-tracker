# 🚌 Automated Public Transit Reliability & Ghost Bus Tracker

> Real-time monitoring and git-scraping reliability index for **Champaign-Urbana Mass Transit District** in **Champaign–Urbana, IL** (Champaign County, Illinois).
> **Transit System:** Champaign-Urbana | **Location:** Champaign–Urbana, IL | **Status:** 🔴 **CRITICAL GHOSTING** | **Last Scan:** `2026-10-22T19:17:43.616000+00:00` | **Source:** live GTFS-RT feed

---

## 📊 Executive Summary Scorecard

| Metric | Value | Status / Description |
| :--- | :--- | :--- |
| **Ghost Bus Rate** | **`17.62%`** | Scheduled runs with missing transponders or unannounced cuts |
| **On-Time Adherence** | **`0.0%`** | Departures within standard window (-1m to +5m) |
| **Scheduled Active Trips** | `193` | Total runs operating in current transit schedule window |
| **Tracked Fleet Vehicles** | `84` | GPS transponders broadcasting valid coordinates |
| **Confirmed Ghost Trips** | `34` | Disappeared or unassigned scheduled runs |
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
| 👻 **Ghost / Missing** | Scheduled but no GPS or vehicle transponder | 34 | 17.6% |
| ❌ **Agency Canceled** | Explicitly reported CANCELED | 0 | 0.0% |

---

## 🚨 Top Worst Routes by Ghost Bus Rate

| Route | Total Scheduled | Tracked | Ghost Trips | Ghost Rate (%) | On-Time (%) | Avg Delay |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **Route NAVY** | 4 | 2 | 2 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route LAVENDER ALT** | 2 | 1 | 1 | **`50.0%`** | `0.0%` | `+0.0s` |
| **Route SILVER** | 15 | 4 | 7 | **`46.67%`** | `0.0%` | `+0.0s` |
| **Route TEAL** | 14 | 4 | 6 | **`42.86%`** | `0.0%` | `+0.0s` |
| **Route GOLDHOPPER** | 5 | 2 | 2 | **`40.0%`** | `0.0%` | `+0.0s` |
| **Route GOLD** | 13 | 6 | 4 | **`30.77%`** | `0.0%` | `+0.0s` |
| **Route YELLOWHOPPER** | 10 | 3 | 3 | **`30.0%`** | `0.0%` | `+0.0s` |
| **Route LINK** | 11 | 3 | 3 | **`27.27%`** | `0.0%` | `+0.0s` |
| **Route ORANGE** | 8 | 3 | 2 | **`25.0%`** | `0.0%` | `+0.0s` |
| **Route YELLOW** | 8 | 5 | 1 | **`12.5%`** | `0.0%` | `+0.0s` |

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
| `[@6.0.15252684@][1][1622671552500]/34__LN1_MF` | Route LINK | `14:45:00` | `SCHEDULED` | Assigned vehicle 1836 is broadcasting off-schedule with no vehicle covering [@6.0.15252684@][1][1622671552500]/34__LN1_MF |
| `[@2.0.86175868@][1458585713139]/9__O4_RUBY_MF` | Route ORANGE | `14:57:00` | `SCHEDULED` | Assigned vehicle 1606 is broadcasting off-schedule with no vehicle covering [@2.0.86175868@][1458585713139]/9__O4_RUBY_MF |
| `[@7.0.41893871@][4][1243540851671]/24__T4_UIMF` | Route TEAL | `14:56:00` | `SCHEDULED` | Assigned vehicle 2416 is broadcasting off-schedule with no vehicle covering [@7.0.41893871@][4][1243540851671]/24__T4_UIMF |
| `[@6.0.51699751@][32][1717268025732]/9__G4_MF[V:0001]` | Route GOLDHOPPER | `14:54:00` | `SCHEDULED` | Assigned vehicle 2201 is broadcasting off-schedule with no vehicle covering [@6.0.51699751@][32][1717268025732]/9__G4_MF[V:0001] |
| `[@6.0.15252684@][2][1622672028480]/76__LN1_MF` | Route LINK | `14:16:00` | `SCHEDULED` | Assigned vehicle 1836 is broadcasting off-schedule with no vehicle covering [@6.0.15252684@][2][1622672028480]/76__LN1_MF |
| `[@6.0.14331263@][2][1622139849262]/73__Y8_UIMF` | Route YELLOWHOPPER | `14:40:00` | `SCHEDULED` | Assigned vehicle 2646 is broadcasting off-schedule with no vehicle covering [@6.0.14331263@][2][1622139849262]/73__Y8_UIMF |
| `[@6.0.15252684@][2][1622672028480]/79__LN1_MF` | Route LINK | `15:01:00` | `SCHEDULED` | Assigned vehicle 1836 is broadcasting off-schedule with no vehicle covering [@6.0.15252684@][2][1622672028480]/79__LN1_MF |
| `[@7.0.41893871@][3][1243541396687]/94__T1_UIMTH` | Route TEAL | `15:15:00` | `SCHEDULED` | Assigned vehicle 2102 is broadcasting off-schedule with no vehicle covering [@7.0.41893871@][3][1243541396687]/94__T1_UIMTH |
| `[@6.0.51699751@][31][1717268857534]/20__G4_MF[V:0001]` | Route GOLDHOPPER | `15:15:00` | `SCHEDULED` | Assigned vehicle 2201 is broadcasting off-schedule with no vehicle covering [@6.0.51699751@][31][1717268857534]/20__G4_MF[V:0001] |
| `[@6.0.28932250@][2][1654215108501]/98__SV3_UIMF` | Route SILVER | `14:40:00` | `SCHEDULED` | Assigned vehicle 2415 is broadcasting off-schedule with no vehicle covering [@6.0.28932250@][2][1654215108501]/98__SV3_UIMF |
| `[@7.0.41893871@][4][1243540851671]/22__T4_UIMF` | Route TEAL | `14:16:00` | `SCHEDULED` | Assigned vehicle 2416 is broadcasting off-schedule with no vehicle covering [@7.0.41893871@][4][1243540851671]/22__T4_UIMF |
| `[@6.0.28932250@][1][1654214032262]/78__SV4_SCH_UIMTH` | Route SILVER | `14:16:00` | `SCHEDULED` | Assigned vehicle 2022 is broadcasting off-schedule with no vehicle covering [@6.0.28932250@][1][1654214032262]/78__SV4_SCH_UIMTH |
| `[@6.0.14329702@][2][1622063676826]/23__Y1_MF` | Route YELLOW | `14:23:00` | `SCHEDULED` | Assigned vehicle 2429 is broadcasting off-schedule with no vehicle covering [@6.0.14329702@][2][1622063676826]/23__Y1_MF |
| `[@7.0.41893871@][3][1243541488843]/125__T1_UIMTH` | Route TEAL | `14:25:00` | `SCHEDULED` | Assigned vehicle 2102 is broadcasting off-schedule with no vehicle covering [@7.0.41893871@][3][1243541488843]/125__T1_UIMTH |
| `[@6.0.14331263@][1][1622139626848]/27__Y8_UIMF` | Route YELLOWHOPPER | `14:22:00` | `SCHEDULED` | Assigned vehicle 2646 is broadcasting off-schedule with no vehicle covering [@6.0.14331263@][1][1622139626848]/27__Y8_UIMF |

---

## 🔬 Methodology & Definitions

- **Ghost Bus**: A transit run that is published in GTFS schedules or trip updates but never arrives because no physical vehicle is assigned or broadcasting GPS positions, or because it was dropped without timely passenger notification.
- **On-Time Adherence**: Departures between 1 minute before scheduled time and up to 5 minutes after scheduled time.
- **Early Departure**: Vehicles departing more than 60 seconds early. In transit operations, early departures are treated as major service failures because passengers arrive on time only to find the vehicle already gone.
- **Excess Wait Time (EWT)**: Transit standard metric measuring variance in vehicle headway caused by vehicle bunching.
- **Git-Scraping**: Every run fetches upstream GTFS-RT binary protobuf feeds, computes reliability metrics, commits versioned JSON snapshots, and renders this dashboard automatically.

*Generated by Ghost Bus Tracker v0.1.0 at `2026-10-22T19:17:43.616000+00:00`.*
