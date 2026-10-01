# Mobility Operations Intelligence

A Flask-based analytics application for analyzing mobility operations data across drivers, trips, zones, cancellations, utilization, demand, and anomalies.

The application allows an operations user to upload mobility datasets and interactively explore operational performance through different analytics categories.

---

## Project Overview

Mobility Operations Intelligence is designed to help mobility operations teams understand:

- Driver performance
- Trip performance
- Zone-level demand
- Cancellation patterns
- Driver utilization
- Operational anomalies
- Top-performing drivers, zones, and riders
- Demand patterns across time slots

The application follows an object-oriented Python architecture with separate modules for data loading, validation, analytics, ranking, anomaly detection, and demand analysis.

---

## Features

### Data Upload

The application accepts three CSV files:

1. Drivers CSV
2. Trips CSV
3. Driver Activity CSV

Uploaded data is validated before analytics are displayed.

### Data Validation

The application checks for issues such as:

- Missing driver information
- Invalid driver ratings
- Unknown driver IDs
- Negative fares
- Negative distances
- Missing pickup/drop timestamps
- Invalid timestamps
- Drop time occurring before pickup time

Validation issues are displayed to the user.

### Dashboard KPIs

The dashboard provides:

- Total drivers
- Active drivers
- Total riders
- Total trips
- Completed trips
- Cancelled trips
- Completion rate
- Cancellation rate
- Total revenue
- Average fare
- Average trip distance
- Average trip duration

### Driver Analytics

The application provides:

- Driver profiles
- Total trips
- Completed trips
- Cancelled trips
- Completion rate
- Cancellation rate
- Revenue
- Average fare
- Average distance
- Fare per kilometer
- Top drivers by completed trips
- Top drivers by revenue
- Driver utilization

### Trip Analytics

The application provides:

- Overall trip performance
- Top riders by trip count
- Cancellation intelligence
- Cancellation by reason
- Cancellation by zone
- Cancellation by driver
- Cancellation by time
- Trip anomaly detection

### Zone Analytics

The application provides:

- Zone-level trip performance
- Completed and cancelled trips
- Completion rate
- Cancellation rate
- Revenue
- Average fare
- Top zones by demand
- Top zones by cancellation
- Demand by time slot
- Zone demand by time

### Ranking

The project uses `heapq` to support Top-K analysis for:

- Drivers by completed trips
- Drivers by revenue
- Zones by demand
- Zones by cancellation
- Riders by trip count

### Anomaly Detection

The application identifies:

- Zero-distance trips
- Negative-fare trips
- Invalid-duration trips
- Trips with unknown drivers
- Extremely long trips

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

Technologies Used
Python
Flask
HTML
CSS
Jinja2
Object-Oriented Programming
Data Structures
heapq
CSV processing
Data Format
Drivers.csv

Required columns:

driver_id
driver_name
city
vehicle_type
rating
status
Trips.csv

Required columns:

trip_id
driver_id
rider_id
city
pickup_zone
drop_zone
request_time
pickup_time
drop_time
distance_km
fare
status
cancellation_reason
Driver_activity.csv

Required columns:

driver_id
timestamp
status
Installation
1. Clone the repository
git clone https://github.com/neha01-acharya/mobility-operations-intelligence.git
2. Navigate to the project
cd mobility-operations-intelligence
3. Create a virtual environment
python -m venv venv
4. Activate the virtual environment

Linux/macOS:

source venv/bin/activate

Windows:

venv\Scripts\activate
5. Install dependencies
pip install -r requirements.txt
Running the Application

Start the Flask application:

python app.py

The application will start on:

http://127.0.0.1:5000

Open the URL in a browser.

Application Flow
Upload Dataset
       ↓
Data Validation
       ↓
Dashboard
       ↓
Select Analysis
       ↓
Driver / Trip / Zone Analytics
       ↓
Detailed Results

Users can also select an individual driver from driver-related analytics to view the driver's detailed profile.

Sample Data

The repository contains sample CSV files under the data/ directory for testing the application.

The uploaded datasets generated while using the application are excluded from Git through .gitignore.

Validation Examples

The application can detect issues such as:

Negative fare in trip T00006
Unknown driver_id D9999 in trip T00026
Drop time is before pickup time in trip T00046

These validation errors are displayed to the operations user instead of being silently ignored.

Objective

The objective of this project is to provide an interactive operations analytics tool that converts raw mobility data into useful operational metrics and insights.

The project demonstrates:

Python OOP
Data processing
Data validation
Analytical problem solving
Data structures and algorithms
Top-K analysis
Operational analytics
Flask application development

