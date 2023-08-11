
from __future__ import  absolute_import
from flask import Flask, request, jsonify
import requests
import configparser
from pymongo import MongoClient 
from bson import ObjectId  # Import ObjectId from pymongo
from bson import json_util
import sys, os
import sys

# Now you can import setup_logger directly from logger_setup
from logger_setup import setup_logger

app = Flask(__name__)
# Configure logging
# Call the setup_logger function to set up the logger
logger = setup_logger()

# Load configuration from config.ini
config = configparser.ConfigParser()
config.read('config.ini')
api_key = config.get('WeatherAPI', 'api_key')
mongodb_url = config.get('WeatherAPI', 'mongodb_url')  # Get the MongoDB URL from the config

#MongoDB connection
client=MongoClient(mongodb_url)
db= client["weather_db"] # create or connect to the weather_db  databse
weather_collection= db["weather_data"]  # create or connect to the weather_data collection


@app.route('/weather', methods=['GET'])
def get_weather():
    logger.debug("Received request to /weather endpoint")

    country = request.args.get('country') 
    city = request.args.get('city')      


    if not country or not city:
        logger.error("Country and city parameters are required")
        return jsonify({'error': 'Country and city parameters are required'}), 400

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city},{country}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        #store the data in mongodb
        inserted_id=weather_collection.insert_one(data).inserted_id
        logger.debug(f"Inserted document with ID: {inserted_id}")
        #print("Inserted document ID:", inserted_id)

        #Convert the objectid to a string
        data['_id'] = str(inserted_id)

        return jsonify(data), 200
    else:
        logger.error("Weather data not found")
        return jsonify({'error': 'Weather data not found'}), 404
    



if __name__ == '__main__':
    app.run(debug=True)
