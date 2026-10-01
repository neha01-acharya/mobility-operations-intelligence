# Mobility Operations Intelligence

A Flask-based analytics application for analyzing mobility operations data across **drivers, trips, zones, cancellations, utilization, demand, and anomalies**.

The application allows an operations user to upload mobility datasets, validate the data, and interactively explore operational performance through different analytics categories.

---

## Project Overview

**Mobility Operations Intelligence** is designed to help mobility operations teams understand operational performance and identify potential issues in mobility data.

The application provides analytics for:

* Driver performance
* Trip performance
* Zone-level demand
* Cancellation patterns
* Driver utilization
* Operational anomalies
* Top drivers, zones, and riders
* Demand patterns across time slots

The project follows an **object-oriented Python architecture**, with separate modules for data loading, validation, analytics, ranking, anomaly detection, utilization analysis, and demand analysis.

---

## Key Features

### 1. Data Upload

The application accepts three CSV datasets:

* **Drivers CSV**
* **Trips CSV**
* **Driver Activity CSV**

The uploaded data is loaded and validated before the analytics are displayed.

---

### 2. Data Validation

The application validates the uploaded data and identifies issues such as:

* Missing driver information
* Invalid driver ratings
* Unknown driver IDs
* Negative fares
* Negative distances
* Missing pickup/drop timestamps
* Invalid timestamps
* Drop time occurring before pickup time

Validation errors are displayed to the user so that data quality issues can be identified before analysis.

---

### 3. Dashboard KPIs

The dashboard provides an overview of the mobility operation through key performance indicators:

* Total drivers
* Active drivers
* Total riders
* Total trips
* Completed trips
* Cancelled trips
* Completion rate
* Cancellation rate
* Total revenue
* Average fare
* Average trip distance
* Average trip duration

---

## Driver Analytics

The application provides detailed driver-level analytics, including:

* Driver profile
* Total trips
* Completed trips
* Cancelled trips
* Completion rate
* Cancellation rate
* Total revenue
* Average fare
* Average distance
* Fare per kilometer
* Top drivers by completed trips
* Top drivers by revenue
* Driver utilization

Users can select a driver from the analytics results to view the driver's detailed profile.

---

## Trip Analytics

Trip-level analysis includes:

* Overall trip performance
* Top riders by trip count
* Cancellation intelligence
* Cancellation by reason
* Cancellation by zone
* Cancellation by driver
* Cancellation by time
* Trip anomaly detection

---

## Zone Analytics

Zone-level analytics include:

* Total trips by zone
* Completed trips
* Cancelled trips
* Completion rate
* Cancellation rate
* Revenue
* Average fare
* Top zones by demand
* Top zones by cancellation
* Demand by time slot
* Zone demand by time

---

## Top-K Analysis

The project uses Python's `heapq` data structure to perform Top-K analysis.

The application supports:

* Top drivers by completed trips
* Top drivers by revenue
* Top zones by demand
* Top zones by cancellation
* Top riders by trip count

Using a heap allows the application to efficiently maintain the required Top-K results.

---

## Driver Utilization

Driver activity data is used to calculate:

* Online hours
* Busy hours
* Idle hours
* Driver utilization

Utilization is calculated based on the driver's activity states over time.

---

## Anomaly Detection

The application identifies potential data and operational anomalies such as:

* Zero-distance trips
* Negative-fare trips
* Invalid-duration trips
* Trips with unknown drivers
* Extremely long trips

These anomalies can help operations teams identify data-quality problems or trips requiring further investigation.

---

## Application Flow

```text
┌─────────────────────┐
│    Upload Dataset   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Data Validation   │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│      Dashboard      │
└──────────┬──────────┘
           ↓
┌─────────────────────┐
│   Select Analysis   │
└──────────┬──────────┘
           ↓
┌────────────────────────────────┐
│ Driver / Trip / Zone Analytics │
└──────────┬─────────────────────┘
           ↓
┌─────────────────────┐
│   Detailed Results  │
└─────────────────────┘
```

---

## Project Structure

```text
mobility-operations-intelligence/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── test_activity.csv
│   ├── test_bad_trips.csv
│   ├── test_drivers.csv
│   └── test_trips.csv
│
├── models/
│   ├── activity.py
│   ├── driver.py
│   └── trip.py
│
├── services/
│   ├── anomaly_detector.py
│   ├── data_loader.py
│   ├── demand_analyzer.py
│   ├── driver_analyzer.py
│   ├── insights_engine.py
│   ├── ranking_service.py
│   ├── trip_analyzer.py
│   ├── utilization_analyzer.py
│   ├── validator.py
│   └── zone_analyzer.py
│
└── templates/
    ├── dashboard.html
    ├── driver.html
    └── index.html
```

---

## Technologies Used

* **Python**
* **Flask**
* **HTML**
* **CSS**
* **Jinja2**
* **Object-Oriented Programming**
* **Python Data Structures**
* **`heapq`**
* **CSV Processing**

The project primarily uses Python's standard library for data processing and analytics.

---

## Dataset Format

The application expects three CSV files.

### Drivers.csv

Required columns:

| Column         | Description              |
| -------------- | ------------------------ |
| `driver_id`    | Unique driver identifier |
| `driver_name`  | Driver name              |
| `city`         | Driver's city            |
| `vehicle_type` | Type of vehicle          |
| `rating`       | Driver rating            |
| `status`       | Driver status            |

Example:

```csv
driver_id,driver_name,city,vehicle_type,rating,status
D001,Rahul,Bangalore,Sedan,4.7,active
D002,Priya,Mumbai,SUV,4.2,inactive
```

---

### Trips.csv

Required columns:

| Column                | Description                     |
| --------------------- | ------------------------------- |
| `trip_id`             | Unique trip identifier          |
| `driver_id`           | Driver associated with the trip |
| `rider_id`            | Rider associated with the trip  |
| `city`                | Trip city                       |
| `pickup_zone`         | Pickup zone                     |
| `drop_zone`           | Drop zone                       |
| `request_time`        | Trip request timestamp          |
| `pickup_time`         | Pickup timestamp                |
| `drop_time`           | Drop timestamp                  |
| `distance_km`         | Trip distance                   |
| `fare`                | Trip fare                       |
| `status`              | Trip status                     |
| `cancellation_reason` | Reason for cancellation         |

Example:

```csv
trip_id,driver_id,rider_id,city,pickup_zone,drop_zone,request_time,pickup_time,drop_time,distance_km,fare,status,cancellation_reason
T001,D001,R001,Bangalore,Indiranagar,Whitefield,2023-10-01T09:00:00,2023-10-01T09:10:00,2023-10-01T09:40:00,12.5,350,completed,
```

---

### Driver_activity.csv

Required columns:

| Column      | Description            |
| ----------- | ---------------------- |
| `driver_id` | Driver identifier      |
| `timestamp` | Activity timestamp     |
| `status`    | Driver activity status |

Example:

```csv
driver_id,timestamp,status
D001,2023-10-01T09:00:00,online
D001,2023-10-01T10:00:00,busy
D001,2023-10-01T11:00:00,idle
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/neha01-acharya/mobility-operations-intelligence.git
```

### 2. Navigate to the Project

```bash
cd mobility-operations-intelligence
```

### 3. Create a Virtual Environment

```bash
python -m venv venv
```

### 4. Activate the Virtual Environment

#### Linux / macOS

```bash
source venv/bin/activate
```

#### Windows

```bash
venv\Scripts\activate
```

### 5. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

Start the Flask application:

```bash
python app.py
```

The application will be available at:

```text
http://127.0.0.1:5000
```

Open the URL in a browser to access the application.

---

## Using the Application

### Step 1 — Upload Data

Upload:

1. Drivers CSV
2. Trips CSV
3. Driver Activity CSV

### Step 2 — Validate Data

The application validates the uploaded data and displays any detected issues.

### Step 3 — View Dashboard

The dashboard displays high-level operational KPIs.

### Step 4 — Select an Analysis

Users can choose from:

* Driver Analytics
* Trip Analytics
* Zone Analytics

### Step 5 — Explore Results

The selected analysis displays the corresponding operational metrics and Top-K results.

### Step 6 — View Driver Profile

From driver-related results, users can select a driver ID to view detailed driver-level performance.

---

## Sample Data

Sample datasets are included in the `data/` directory:

```text
data/
├── test_activity.csv
├── test_bad_trips.csv
├── test_drivers.csv
└── test_trips.csv
```

The `test_bad_trips.csv` dataset can be used to test the application's validation functionality.

Uploaded datasets generated while using the application are excluded from Git through `.gitignore`.

---

## Validation Examples

The application can identify issues such as:

```text
Negative fare in trip T00006
Unknown driver_id D9999 in trip T00026
Drop time is before pickup time in trip T00046
```

These validation issues are displayed to the operations user rather than being silently ignored.

---

## Objective

The objective of this project is to provide an interactive operations analytics tool that converts raw mobility data into useful operational metrics and insights.

The project demonstrates practical application of:

* Python Object-Oriented Programming
* Data processing
* Data validation
* Analytical problem solving
* Data structures and algorithms
* Top-K analysis
* Operational analytics
* Flask application development

---

## Future Enhancements

Potential future enhancements include:

* Interactive charts and visualizations
* Additional driver performance metrics
* Advanced utilization thresholds
* More sophisticated anomaly detection
* Search functionality using indexed data
* Expanded operational insights
* Additional filtering by city, zone, and time period

---


