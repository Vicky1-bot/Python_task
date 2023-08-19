from log import setup_logging
from weather import WeatherAnalyzer

def main():
    try:
        # Configure logging
        logger = setup_logging()

        # Create WeatherAnalyzer instance
        analyzer = WeatherAnalyzer()
        analyzer.logger = logger
        
        # Analyze weather and calculate accuracy
        analyzer.analyze_weather()

        logger.info("Weather analysis and accuracy calculation completed.")

    except Exception as e:
        logger.exception(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()
