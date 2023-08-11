# Weather Data Retrieval Module with Logging and MongoDB Storage

This project introduces a module for retrieving weather data, incorporating logging, and storing the data in MongoDB.

## Features

- Request weather data through a dedicated module.
- Implement logging for tracking events and errors.
- Store the retrieved data in MongoDB for future access.

## Prerequisites

- Python 3.x
- Flask
- MongoDB

## Installation

1. Clone this repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Configure MongoDB connection in the app.
4. Run the Flask app: `python main.py`.

## Module Details

### Weather Data Retrieval and Storage

The `weather_retrieval.py` module provides a method to request weather data and store it in MongoDB. Logging is integrated for effective event monitoring.

### How to Use

1. Import the `weather_retrieval` module.
2. Call the `request_and_store_weather_data` method with desired parameters.
3. Observe the log messages and verify data in MongoDB.

## API Endpoints

### Request and Store Weather Data

**Endpoint**: `/weather?country=[country]&city=[city]`

**Description**: Request weather data from the API and store it in the MongoDB database.

## Screenshots

![Screenshot 1](/Assignment_3/output/Weather%20API%20request%20%20call.png)
*Logging events and storing weather data.*

![Screenshot 2](/Assignment_3/output/sample%20record%20visualization.png)
*Sample DB record visualization .*

## License

This project is licensed under the MIT License.

---
