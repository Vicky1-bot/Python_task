import pandas as pd
from prophet import Prophet
import configparser
from log import setup_logging

class WeatherAnalyzer:
    def __init__(self, config_file="config.ini"):
        # Load configuration from config.ini
        self.config = configparser.ConfigParser()
        self.config.read(config_file)
        
        # Configure logging
        self.logger = setup_logging()

    def load_data(self, file_path):
        self.logger.info("Loading data...")
        data = pd.read_csv(file_path)
        return data

    def preprocess_data(self, data):
        self.logger.info("Preprocessing data...")
        data["date"] = pd.to_datetime(data["date"], format='%Y-%m-%d')
        data['year'] = data['date'].dt.year
        data["month"] = data["date"].dt.month
        return data

    def forecast_temperature(self, data):
        self.logger.info("Forecasting temperature using Prophet...")
        forecast_data = data.rename(columns={"date": "ds", "meantemp": "y"})
        model = Prophet()
        model.fit(forecast_data)
        forecasts = model.make_future_dataframe(periods=365)
        predictions = model.predict(forecasts)
        return predictions

    def calculate_accuracy(self, predictions, actual_values):
        mae = (abs(predictions - actual_values)).mean()
        return mae

    def analyze_weather(self):
        try:
            data_file = self.config.get("WeatherAnalysis", "DATA_FILE")
            data = self.load_data(data_file)
            data = self.preprocess_data(data)

            temperature_forecasts = self.forecast_temperature(data)

            # Assuming 'y' column contains actual temperature values
            actual_temperature = data['meantemp']
            forecasted_temperature = temperature_forecasts['yhat']

            mae = self.calculate_accuracy(forecasted_temperature, actual_temperature)
            self.logger.info(f"Mean Absolute Error (MAE): {mae}")

            self.logger.info("Temperature forecasting completed.")

        except Exception as e:
            self.logger.exception(f"An error occurred: {str(e)}")

# if __name__ == "__main__":
#     analyzer = WeatherAnalyzer()
#     analyzer.analyze_weather()
