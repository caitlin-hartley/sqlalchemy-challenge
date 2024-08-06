# Import the dependencies.

import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################

# create engine to hawaii.sqlite
engine = create_engine("sqlite:///../resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Station = Base.classes.station
Measurement = Base.classes.measurement

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################


app = Flask(__name__)


#################################################
# Flask Routes
#################################################

## Create routes for app

# 1. '/'
# Start at the homepage.
# List all the available routes.

@app.route("/")
def welcome():
    return (
        f"Welcome to the Hawaii Climate Analysis API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start (enter as YYYY-MM-DD)<br/>"
        f"/api/v1.0/start/end (enter as YYYY-MM-DD/YYYY-MM-DD)"

    )

##

# 2. /api/v1.0/precipitation
# Convert the query results from your precipitation analysis (i.e. retrieve only the last 12 months of data) to a dictionary 
# using date as the key and prcp as the value.
# Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")

def precipitation():

    session = Session(engine)

    # Calculate the date one year from the last date in data set.
    one_year_ago = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores

    query = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= one_year_ago)

    # Close session
    session.close()

    # Convert query to a dictionary using date as the key and prcp as the value
    precipitation_dict = {date: prcp for date, prcp in query}

    # Return json results of dictionary
    return jsonify(precipitation_dict) 

##

# 3. /api/v1.0/stations
# Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def stations():
    
    # Create a session
    session = Session(engine)

    # Query all station names
    query = session.query(Station.station).all()

    # Close session
    session.close()

    # Convert query results to a list of dictionaries
    stations = [{"Station": station[0]} for station in query]
    
    # Return JSON response
    return jsonify(stations)

##

# 4. /api/v1.0/tobs
# Query the dates and temperature observations of the most-active station for the previous year of data.
# Return a JSON list of temperature observations for the previous year.

@app.route("/api/v1.0/tobs")
def tobs():

    # Create a session
    session = Session(engine)

    # Query data
    query = session.query( Measurement.date, Measurement.tobs).\
        filter(Measurement.station=='USC00519281').\
        filter(Measurement.date>='2016-08-23').all()

    # Close session
    session.close()

    # Convert query results to a list of dictionaries
    temperature_data = [{"date": date, "tobs": tobs} for date, tobs in query]

    # Return JSON response
    return jsonify(temperature_data)

##

# 5. /api/v1.0/<start>
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start range.
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.

@app.route("/api/v1.0/<start>")
def get_temps_start(start):

    # Create session
    session = Session(engine)

    # Query min, avg, max temps from start date till end of dataset
    results = session.query(
        func.min(Measurement.tobs).label('min_temp'),
        func.avg(Measurement.tobs).label('avg_temp'),
        func.max(Measurement.tobs).label('max_temp')).\
        filter(Measurement.date >= start).\
        group_by(Measurement.date).all()

    # Close session
    session.close()
    
    # Construct a list of dictionaries with temperature data
    temperatures = []
    for min_temp, avg_temp, max_temp in results:
        temp_dict = {}
        temp_dict['TMIN'] = min_temp
        temp_dict['TAVG'] = avg_temp
        temp_dict['TMAX'] = max_temp
        temperatures.append(temp_dict)


    # Return JSON response
    return jsonify(temperatures)


##

# 6. /api/v1.0/<start>/<end>
# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start - end range.
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive.


@app.route("/api/v1.0/<start>/<end>")
def get_temps_start_end(start, end):

    # Create session
    session = Session(engine)

    # Query min, avg, max temps, filtered by start and end date input from user
    results = session.query(
        func.min(Measurement.tobs).label('min_temp'),
        func.avg(Measurement.tobs).label('avg_temp'),
        func.max(Measurement.tobs).label('max_temp')).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).\
        group_by(Measurement.date).all()

    # Close session
    session.close()
    
    # Construct a list of dictionaries with temperature data from date range
    temperatures = []
    for min_temp, avg_temp, max_temp in results:
        temp_dict = {}
        temp_dict['TMIN'] = min_temp
        temp_dict['TAVG'] = avg_temp
        temp_dict['TMAX'] = max_temp
        temperatures.append(temp_dict)


    # Return JSON response
    return jsonify(temperatures)



if __name__ == '__main__':
    app.run(debug=True)