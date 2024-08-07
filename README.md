# sqlalchemy-challenge

[Part 1: Precipitation Analysis](README.md#precipitation-analysis)

[Part 1: Station Analysis]

[Part 2: Climate App]

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
