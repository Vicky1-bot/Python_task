# Weather Analysis Project

## Overview

This Python project performs weather analysis and temperature forecasting using the Prophet model. It includes components for data loading, preprocessing, forecasting, and accuracy calculation.

## Features

- Load historical weather data from a CSV file.
- Preprocess the data to extract year and month information.
- Forecast temperature values using the Prophet model.
- Calculate the Mean Absolute Error (MAE) to measure forecast accuracy.
- Configure logging for detailed information and error handling.

## Setup

1. Install required packages:
   
      pip install -r requirements.txt

3. Create a `config.ini` file:
    ```ini
    [WeatherAnalysis]
    DATA_FILE = path/to/your/weather_data.csv
    LOG_FILE = Logs/weather_analysis.log

3.Configure logging using logging.conf.

4.Run the analysis script:

     python main.py


## Project Structure

- `main.py`: Main script to execute the weather analysis.
- `weather.py`: Contains the `WeatherAnalyzer` class for weather analysis and forecasting.
- `log.py`: Configures logging for the project.
- `config.ini`: Configuration file for project settings.
- `logging.conf`: Logging configuration settings.
- `requirements.txt`: List of required Python packages and versions.
- `Logs/`: Directory to store log files.
- `DailyDelhiClimate.csv`: weather data for analysis.

## License

This project is licensed under the [MIT License](LICENSE).
