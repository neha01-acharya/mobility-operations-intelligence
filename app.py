from flask import Flask, render_template, request

from services.data_loader import DataLoader
from services.validator import DataValidator
from services.trip_analyzer import TripAnalyzer
from services.driver_analyzer import DriverAnalyzer
from services.zone_analyzer import ZoneAnalyzer
from services.utilization_analyzer import UtilizationAnalyzer
from services.anomaly_detector import AnomalyDetector
from services.ranking_service import RankingService
from services.demand_analyzer import DemandAnalyzer


app = Flask(__name__)


# ============================================================
# HOME / UPLOAD PAGE
# ============================================================

@app.route("/")
def home():
    return render_template("index.html")


# ============================================================
# UPLOAD DATA
# ============================================================

@app.route("/upload", methods=["POST"])
def upload():

    drivers_file = request.files.get("drivers_file")
    trips_file = request.files.get("trips_file")
    activity_file = request.files.get("activity_file")

    if (
        not drivers_file
        or not trips_file
        or not activity_file
    ):
        return render_template(
            "index.html",
            errors=[
                "Please select all three CSV files."
            ]
        )

    drivers_path = "data/uploaded_drivers.csv"
    trips_path = "data/uploaded_trips.csv"
    activity_path = "data/uploaded_activity.csv"

    drivers_file.save(drivers_path)
    trips_file.save(trips_path)
    activity_file.save(activity_path)

    loader = DataLoader()

    try:

        drivers = loader.load_drivers(
            drivers_path
        )

        trips = loader.load_trips(
            trips_path
        )

        activities = loader.load_activity(
            activity_path
        )

    except Exception as error:

        return render_template(
            "index.html",
            errors=[
                f"Unable to read uploaded files: {error}"
            ]
        )

    validator = DataValidator()

    errors = validator.validate(
        drivers,
        trips
    )

    return build_dashboard(
        drivers,
        trips,
        activities,
        errors
    )


# ============================================================
# DASHBOARD
# ============================================================

@app.route("/dashboard")
def dashboard():

    loader = DataLoader()

    try:

        drivers = loader.load_drivers(
            "data/uploaded_drivers.csv"
        )

        trips = loader.load_trips(
            "data/uploaded_trips.csv"
        )

        activities = loader.load_activity(
            "data/uploaded_activity.csv"
        )

    except Exception as error:

        return render_template(
            "index.html",
            errors=[
                "No uploaded dataset found. "
                f"Please upload the CSV files first. Error: {error}"
            ]
        )

    validator = DataValidator()

    errors = validator.validate(
        drivers,
        trips
    )

    return build_dashboard(
        drivers,
        trips,
        activities,
        errors
    )


# ============================================================
# BUILD DASHBOARD
# ============================================================

def build_dashboard(
    drivers,
    trips,
    activities,
    errors
):

    # --------------------------------------------------------
    # Create analyzers
    # --------------------------------------------------------

    trip_analyzer = TripAnalyzer(
        trips
    )

    zone_analyzer = ZoneAnalyzer(
        trips
    )

    utilization_analyzer = UtilizationAnalyzer(
        activities
    )

    anomaly_detector = AnomalyDetector(
        trips,
        drivers
    )

    ranking_service = RankingService(
        drivers,
        trips
    )

    demand_analyzer = DemandAnalyzer(
        trips
    )

    # --------------------------------------------------------
    # Trip summary
    # --------------------------------------------------------

    trip_summary = trip_analyzer.summary()

    # --------------------------------------------------------
    # Driver counts
    # --------------------------------------------------------

    total_drivers = len(drivers)

    active_drivers = 0

    for driver in drivers:

        if driver.is_active():
            active_drivers += 1

    # --------------------------------------------------------
    # Rider count
    # --------------------------------------------------------

    riders = set()

    for trip in trips:

        if trip.rider_id:
            riders.add(trip.rider_id)

    total_riders = len(riders)

    # --------------------------------------------------------
    # Rankings
    # --------------------------------------------------------

    top_drivers = ranking_service.top_drivers_by_completed_trips(
        5
    )

    top_revenue_drivers = ranking_service.top_drivers_by_revenue(
        5
    )

    top_zones = ranking_service.top_zones_by_demand(
        5
    )

    top_riders = ranking_service.top_riders_by_trip_count(
        5
    )

    top_cancel_zones = ranking_service.top_zones_by_cancellation(
        5
    )

    # --------------------------------------------------------
    # Zone analytics
    # --------------------------------------------------------

    zones = zone_analyzer.all_zone_summaries()

    # --------------------------------------------------------
    # Demand analytics
    # --------------------------------------------------------

    demand_by_time_slot = (
        demand_analyzer.demand_by_time_slot()
    )

    demand_by_zone_and_time = (
        demand_analyzer.demand_by_zone_and_time()
    )

    # --------------------------------------------------------
    # Utilization
    # --------------------------------------------------------

    utilization = (
        utilization_analyzer.all_driver_utilization()
    )

    # --------------------------------------------------------
    # Anomalies
    # --------------------------------------------------------

    anomalies = (
        anomaly_detector.get_all_anomalies()
    )

    # --------------------------------------------------------
    # Cancellation intelligence
    # --------------------------------------------------------

    cancellation_by_reason = (
        anomaly_detector.cancellation_by_reason()
    )

    cancellation_by_zone = (
        anomaly_detector.cancellation_by_zone()
    )

    cancellation_by_driver = (
        anomaly_detector.cancellation_by_driver()
    )

    cancellation_by_time = (
        anomaly_detector.cancellation_by_time()
    )

    # --------------------------------------------------------
    # Render dashboard
    # --------------------------------------------------------

    return render_template(
        "dashboard.html",

        total_drivers=total_drivers,

        active_drivers=active_drivers,

        total_riders=total_riders,

        trip_summary=trip_summary,

        top_drivers=top_drivers,

        top_revenue_drivers=top_revenue_drivers,

        top_zones=top_zones,

        top_riders=top_riders,

        top_cancel_zones=top_cancel_zones,

        zones=zones,

        demand_by_time_slot=demand_by_time_slot,

        demand_by_zone_and_time=demand_by_zone_and_time,

        utilization=utilization,

        anomalies=anomalies,

        cancellation_by_reason=cancellation_by_reason,

        cancellation_by_zone=cancellation_by_zone,

        cancellation_by_driver=cancellation_by_driver,

        cancellation_by_time=cancellation_by_time,

        errors=errors
    )


# ============================================================
# DRIVER PROFILE
# ============================================================

@app.route("/driver/<driver_id>")
def driver_profile(driver_id):

    loader = DataLoader()

    try:

        drivers = loader.load_drivers(
            "data/uploaded_drivers.csv"
        )

        trips = loader.load_trips(
            "data/uploaded_trips.csv"
        )

    except Exception as error:

        return render_template(
            "driver.html",
            profile=None,
            error=(
                "Unable to load uploaded dataset. "
                f"Error: {error}"
            )
        )

    driver_analyzer = DriverAnalyzer(
        drivers,
        trips
    )

    profile = driver_analyzer.get_profile(
        driver_id
    )

    if profile is None:

        return render_template(
            "driver.html",
            profile=None,
            error=(
                f"Driver {driver_id} was not found."
            )
        ), 404

    return render_template(
        "driver.html",
        profile=profile,
        error=None
    )


# ============================================================
# RUN APPLICATION
# ============================================================

if __name__ == "__main__":

    app.run(
        debug=True
    )