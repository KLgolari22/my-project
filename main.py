import logging
import logging.handlers
import os
import requests
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# File handler
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)

# Console (stdout) handler for GitHub Actions
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)  # or DEBUG if needed

# Formatter
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
console_handler.setFormatter(formatter)

# Add both handlers
logger.addHandler(logger_file_handler)
logger.addHandler(console_handler)

now = datetime.now()
formatted = now.strftime("%Y-%m-%d %H:%M:%S")

# Read secret
try:
    SOME_SECRET = os.environ["SOME_SECRET"]
    WHTR_API_KEY = os.environ["WHTR_API_KEY"]
except KeyError:
    SOME_SECRET = "Token not available!"
    logger.warning("Token not available!")



if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    # api_key = 'ec07f5b8954749b6861203448250105'  
    api_key = WHTR_API_KEY
    city = 'Hyderabad'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'

    try:
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            logger.info(f"Location: {data['location']['name']}, {data['location']['region']}")
            logger.info(f"Temperature (C): {data['current']['temp_c']}")
            logger.info(f"Condition: {data['current']['condition']['text']}")
            logger.info(f"Formatted date and time: {formatted}")
        else:
            logger.error(f"Failed to fetch weather data. Status code: {response.status_code}")
    except Exception as e:
        logger.exception("An error occurred while fetching weather data")

