
# Weather API using Flask and MongoDB

This project implements a Weather API using Flask and MongoDB to store and retrieve weather data.

## Features

- Store and retrieve weather data for cities.
- Single record retrieval based on country and city.

## Prerequisites

- Python 3.x
- Flask
- MongoDB

## Installation

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Configure MongoDB connection in the app.
4. Run the Flask app: `python app.py`.

## API Endpoints

### Request and Store Weather Data

**Endpoint**: `/weather?country=[country]&city=[city]`

**Description**: Request weather data from the API and store it in the MongoDB database.

### Retrieve Weather Data

**Endpoint**: `/get_weather_data?country=[country]&city=[city]`

**Description**: Retrieve weather data from the MongoDB database based on country and city.

## Screenshots

![Screenshot 1](/Assignment_3/output/Weather%20API%20request%20%20call.png)
*Requesting weather data for Hyderabad, India.*

![Screenshot 1](/Assignment_3/output/Retrieving%20Data%20from%20mongodb.png)
*Retrieving weather data for Hyderabad, India.*

![Screenshot 1](/Assignment_3/output/sample%20record%20visualization.png)
*sample DB record visualization for chennai, India.*

