
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

![Screenshot 1](/path/to/screenshot_1.png)
*Retrieving weather data for Hyderabad, India.*

