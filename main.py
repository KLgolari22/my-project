
import logging
import logging.handlers
import os
import requests
from datetime import datetime

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
logger_file_handler = logging.handlers.RotatingFileHandler(
    "status.log",
    maxBytes=1024 * 1024,
    backupCount=1,
    encoding="utf8",
)
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger_file_handler.setFormatter(formatter)
logger.addHandler(logger_file_handler)

try:
    SOME_SECRET = os.environ["SOME_SECRET"]
except KeyError:
    SOME_SECRET = "Token not available!"
    #logger.info("Token not available!")
    #raise
if __name__ == "__main__":
    logger.info(f"Token value: {SOME_SECRET}")

    # r = requests.get('https://weather.talkpython.fm/api/weather/?city=Berlin&country=DE')
    # if r.status_code == 200:
    #     data = r.json()
    #     temperature = data["forecast"]["temp"]
    #     logger.info(f'status_code is{r.status_code}')
    #     logger.info(f'Weather in Berlin: {temperature}')
    now = datetime.now()

    # Format: YYYY-MM-DD HH:MM:SS
    formatted = now.strftime("%Y-%m-%d %H:%M:%S")


    api_key = 'ec07f5b8954749b6861203448250105'  
    city = 'Hyderabad'
    url = f'http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}'
    response = requests.get(url)
    if response.status_code ==200:        
        data = response.json()
        # Print key weather details
        logger.info(f"Location: {data['location']['name']}, {data['location']['region']}")
        logger.info(f"Temperature (C): {data['current']['temp_c']}")
        logger.info(f"Condition: {data['current']['condition']['text']}")
        logger.info("Formatted date and time:", formatted)
