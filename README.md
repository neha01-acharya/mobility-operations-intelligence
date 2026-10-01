# Mobility Operations Intelligence

A Flask-based mobility analytics application that analyzes driver, trip, activity, demand, zone, cancellation, and anomaly data to generate operational insights.

The application is designed to demonstrate how structured mobility data can be processed using Python, object-oriented programming, data structures, searching, ranking, and analytical algorithms.

---

## 1. Problem Statement

Mobility platforms generate large amounts of operational data from drivers, trips, rider requests, driver activity, zones, and cancellations.

Raw data alone does not provide an operational view of the business. Operations teams need to understand:

* How many drivers and trips are being handled
* Which drivers are completing the most trips
* Which drivers generate the most revenue
* How efficiently drivers are utilized
* Which zones have high demand
* Which zones experience high cancellations
* When demand is highest
* Which trip or driver patterns may indicate anomalies
* What operational actions can be considered based on the observed patterns

The **Mobility Operations Intelligence** application processes these datasets and converts them into operational metrics and insights through a Flask-based analytics dashboard.

---

# 2. Setup Instructions

## Prerequisites

* Python 3.x
* Git
* Flask

## Clone the Repository

```bash
git clone https://github.com/neha01-acharya/mobility-operations-intelligence.git
cd mobility-operations-intelligence
```

## Install Dependencies

If a `requirements.txt` file is available:

```bash
pip install -r requirements.txt
```

Otherwise, install Flask:

```bash
pip install flask
```

## Run the Application

```bash
python app.py
```

The Flask application will start locally.

Open the application in a browser using the local Flask URL shown in the terminal.

---

# 3. Application Flow

The application follows the following flow:

```text
CSV Dataset Upload
        |
        v
     DataLoader
        |
        v
   Data Validation
        |
        v
+-----------------------------+
|       Analytics Layer       |
+-----------------------------+
| Demand Analyzer             |
| Trip Analyzer               |
| Zone Analyzer               |
| Driver Analyzer             |
| Utilization Analyzer        |
| Ranking Service             |
| Anomaly Detector            |
| Search Engine               |
+-----------------------------+
        |
        v
   Insights Engine
        |
        v
   Flask Dashboard
        |
        v
Operational Insights
```

### Step 1 — Upload Data

The user uploads:

* Drivers CSV
* Trips CSV
* Driver Activity CSV

### Step 2 — Load Data

`DataLoader` reads the CSV files and converts each row into the corresponding Python model object.

### Step 3 — Validate Data

The validation layer checks whether the uploaded data satisfies the expected structure and conditions.

### Step 4 — Analyze Data

Different analytical services process the loaded data.

Examples:

* Trip performance
* Driver rankings
* Driver utilization
* Zone performance
* Demand by time slot
* Cancellation analysis
* Anomaly detection

### Step 5 — Generate Insights

The `InsightsEngine` combines analytical outputs and generates operational observations.

### Step 6 — Display Results

The Flask application renders the results through the dashboard.

Users can also search for:

* Driver
* Trip
* Zone

---

# 4. Architecture

The project follows a modular, service-oriented architecture.

```text
mobility-operations-intelligence/
│
├── models/
│   ├── driver.py
│   ├── trip.py
│   ├── activity.py
│   └── zone.py
│
├── services/
│   ├── data_loader.py
│   ├── validator.py
│   ├── search_engine.py
│   ├── demand_analyzer.py
│   ├── trip_analyzer.py
│   ├── driver_analyzer.py
│   ├── zone_analyzer.py
│   ├── utilization_analyzer.py
│   ├── ranking_service.py
│   ├── anomaly_detector.py
│   └── insights_engine.py
│
├── templates/
│   ├── index.html
│   ├── dashboard.html
│   ├── driver.html
│   └── search.html
│
├── data/
│
├── app.py
└── README.md
```

## Architectural Layers

### Presentation Layer

Implemented using Flask routes and HTML templates.

Responsible for:

* File uploads
* Dashboard rendering
* Search interface
* Driver profiles

### Model Layer

Contains domain classes representing:

* Drivers
* Trips
* Driver activities
* Zones

### Service Layer

Contains the application's business logic and analytics.

Each service is responsible for a specific analytical area instead of placing all logic inside the Flask routes.

---

# 5. Classes

## Driver

Represents a driver in the mobility system.

Typical attributes include:

* `driver_id`
* `driver_name`
* `city`
* `vehicle_type`
* `rating`
* `status`

---

## Trip

Represents a mobility trip.

Typical attributes include:

* `trip_id`
* `driver_id`
* `rider_id`
* `city`
* `pickup_zone`
* `drop_zone`
* `request_time`
* `pickup_time`
* `drop_time`
* `distance_km`
* `fare`
* `status`
* `cancellation_reason`

The class also provides helper methods for determining trip status, such as completed and cancelled trips.

---

## DriverActivity

Represents the activity state of a driver at a particular timestamp.

Examples of activity states include:

* Online
* Busy
* Idle

This information is used to calculate driver utilization.

---

## Zone

Represents a geographical operating zone.

The zone information can be used to analyze:

* Demand
* Trip volume
* Cancellations
* Operational performance

---

## DataLoader

Responsible for reading CSV files and converting records into model objects.

Main methods include:

```text
load_drivers()
load_trips()
load_activity()
```

---

## DataValidator

Responsible for validating uploaded mobility datasets and checking expected data conditions.

---

## SearchEngine

Provides indexed searching for:

* Drivers
* Trips
* Zones

The search engine creates dictionaries for fast lookup instead of repeatedly scanning the complete dataset.

---

## DemandAnalyzer

Analyzes trip demand patterns.

Examples:

* Demand by time slot
* Zone-level demand
* Time-based demand patterns

---

## TripAnalyzer

Analyzes trip-level operational metrics.

Examples:

* Trip performance
* Top riders
* Cancellation by reason
* Cancellation by zone
* Cancellation by driver
* Cancellation by time

---

## DriverAnalyzer

Analyzes driver-related operational metrics and performance.

---

## ZoneAnalyzer

Analyzes zone-level performance.

Examples:

* Zone demand
* Zone performance
* Zone cancellation patterns

---

## UtilizationAnalyzer

Uses driver activity records to calculate:

* Online hours
* Busy hours
* Idle hours
* Utilization percentage

Utilization is calculated based on the proportion of active time spent in the busy state.

```text
Utilization =
Busy Hours / Total Active Hours × 100
```

---

## RankingService

Ranks drivers or other entities based on operational metrics.

Examples:

* Completed trips
* Revenue

---

## AnomalyDetector

Identifies potentially unusual operational patterns from the available trip and driver data.

---

## InsightsEngine

Combines outputs from multiple analytical services and converts them into higher-level operational insights.

---

# 6. DSA Concepts Used

The project applies multiple Data Structures and Algorithms concepts.

## Dictionaries / Hash Maps

Dictionaries are used for fast entity lookup.

For example:

```python
driver_index[driver_id] = driver
```

This allows a driver to be retrieved directly using the driver ID.

Average lookup complexity:

```text
O(1)
```

---

## Lists

Lists are used extensively to store:

* Drivers
* Trips
* Activities
* Analysis results

They also support sequential processing of datasets.

---

## defaultdict

`defaultdict` is used to group driver activity records.

For example:

```python
grouped[activity.driver_id].append(activity)
```

This simplifies grouping records by driver.

---

## Sorting

Activity records are sorted by timestamp before calculating the duration between consecutive activity states.

```python
activities.sort(
    key=lambda activity: activity.get_datetime()
)
```

---

## Grouping

The project groups data by different dimensions such as:

* Driver
* Zone
* Time
* Cancellation reason
* Rider

This enables aggregation-based analytics.

---

## Searching

The `SearchEngine` uses indexes for direct lookup of drivers, trips, and zones.

This avoids repeatedly scanning the entire dataset.

---

## Ranking

Driver and zone results can be ordered according to metrics such as:

* Completed trips
* Revenue
* Demand
* Cancellation

---

## Sequential / Time-Series Processing

Driver activity records are processed chronologically.

The duration between two consecutive activity records is calculated as:

```text
next timestamp - current timestamp
```

The duration is then assigned to the corresponding activity state.

---

# 7. Complexity

Let:

* `D` = number of drivers
* `T` = number of trips
* `A` = number of activity records
* `Z` = number of zones

## Data Loading

Drivers:

```text
O(D)
```

Trips:

```text
O(T)
```

Activities:

```text
O(A)
```

Overall data loading:

```text
O(D + T + A)
```

---

## Search

Dictionary-based driver, trip, and zone lookup:

```text
Average: O(1)
```

---

## Activity Grouping

Grouping activities by driver:

```text
O(A)
```

Sorting activities for each driver results in approximately:

```text
O(A log A)
```

in the worst case.

---

## Trip Analysis

Most aggregation operations require a scan through the trips:

```text
O(T)
```

---

## Ranking

If results containing `N` entities are sorted:

```text
O(N log N)
```

---

## Space Complexity

The application stores loaded datasets and indexes in memory.

Approximate space requirement:

```text
O(D + T + A + Z)
```

---

# 8. Assumptions

The application makes the following assumptions:

1. Uploaded files follow the expected CSV structure.
2. Driver IDs uniquely identify drivers.
3. Trip IDs uniquely identify trips.
4. Activity records contain valid driver IDs.
5. Timestamp values are parseable as datetime values.
6. Fare and distance values are numeric.
7. Trip status values follow the expected status conventions.
8. Activity records are sufficiently complete to estimate driver state durations.
9. The activity state at a timestamp remains valid until the next activity record for that driver.
10. Driver utilization is calculated from the available activity records rather than from a real-time driver tracking system.
11. Cancellation rate is calculated as:

```text
Cancelled Trips / Total Trips × 100
```

12. Historical data is treated as representative of the period being analyzed.
13. The dashboard is intended for operational analysis and not as a real-time dispatch system.

---

# 9. Known Limitations

### 1. Batch Processing

The application analyzes uploaded CSV files and does not process live mobility events.

### 2. No Real-Time Driver Tracking

Driver status and utilization are calculated from historical activity records.

### 3. Activity Data Dependency

Utilization accuracy depends on the completeness and correctness of driver activity timestamps.

### 4. Limited Geographic Analysis

The project uses zone information from the dataset and does not integrate external mapping or geospatial services.

### 5. No Predictive Demand Model

The current application focuses primarily on descriptive and diagnostic analytics rather than forecasting future demand.

### 6. No Persistent Database

Data is loaded from CSV files rather than stored in a production database.

### 7. Dataset-Dependent Insights

The quality of generated insights depends on the quality, volume, and coverage of the uploaded data.

### 8. Basic Anomaly Detection

Anomaly detection is based on implemented analytical rules and does not represent a production-grade machine-learning anomaly detection system.

### 9. Single-Application Deployment

The current Flask application is designed as an analytics project and is not optimized for large-scale production traffic.

---

# 10. Conclusion

Mobility Operations Intelligence provides a modular framework for analyzing mobility operations data.

The application demonstrates the use of:

* Python
* Flask
* Object-oriented programming
* Data structures
* Searching
* Sorting
* Aggregation
* Time-series analysis
* Ranking
* Anomaly detection
* Operational insight generation

The project converts raw driver, trip, activity, and zone data into metrics that can support operational analysis and decision-making.
