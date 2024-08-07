# sqlalchemy-challenge

[Part 1: Precipitation Analysis](README.md#precipitation-analysis)

[Part 1: Station Analysis](README.md#station-analysis)

[Part 2: Climate App](README.md#part-2-design-climate-app)

---

## Part 1: Analyze and Explore the Climate Data

Use Python and SQLAlchemy to do a basic climate analysis and data exploration of climate database
  
1.) Use the SQLAlchemy create_engine() function to connect to SQLite database.

2.) Use the SQLAlchemy automap_base() function to reflect tables into classes

3.) Link Python to the database by creating a SQLAlchemy session

4.) Perform a precipitation analysis and then a station analysis

---

### Precipitation Analysis

- Find the most recent date in the dataset
- Get the previous 12 months of precipitation data by querying the previous 12 months of data
- Load the query results into a dataframe
- Sort the DataFrame values by "date"
- Plot the results

![Precipitation](https://github.com/caitlin-hartley/sqlalchemy-challenge/blob/main/output/precipitation.png)

---

### Station Analysis

- Query to calculate the total number of stations in the dataset
- Query to find the most-active stations

![Query](https://github.com/caitlin-hartley/sqlalchemy-challenge/blob/main/output/example_query.png)

- Query the previous 12 months of TOBS data for that station
- Plot the results

![Station](https://github.com/caitlin-hartley/sqlalchemy-challenge/blob/main/output/station.png)


## Part 2: Design Climate App

- Design a Flask API based on the queries in Part 1

1.) /
- Start at the homepage
- List all the available routes

2.) /api/v1.0/precipitation
- Convert the query results from precipitation analysis to a dictionary using date as the key and prcp as the value
- Return the JSON representation of dictionary

3.) /api/v1.0/stations
- Return a JSON list of stations from the dataset
  
![3](https://github.com/caitlin-hartley/sqlalchemy-challenge/blob/main/output/route_3.png)

4.) /api/v1.0/tobs
- Query the dates and temperature observations of the most-active station for the previous year of data
- Return a JSON list of temperature observations for the previous year

5.) /api/v1.0/<start>
- For a specified start (YYYY-MM-DD), calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date

6.) /api/v1.0/<start>/<end>
- For a specified start date and end date (YYYY-MM-DD/YYYY-MM-DD), calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive

![6](https://github.com/caitlin-hartley/sqlalchemy-challenge/blob/main/output/route_6.png)
