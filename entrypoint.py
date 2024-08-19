import json
import redis
from flask import Flask, request
from loguru import logger

app = Flask(__name__)

# Loguru logger setup (if not already configured elsewhere)
logger.add("file_{time}.log", rotation="1 day")

HISTORY_LENGTH = 10
DATA_KEY = "engine_temperature"

@app.route('/record', methods=['POST'])
def record_engine_temperature():
    # Extract JSON payload from the request
    payload = request.get_json(force=True)
    logger.info(f"(*) record request --- {json.dumps(payload)} (*)")

    # Extract engine temperature from the payload
    engine_temperature = payload.get("engine_temperature")
    logger.info(f"engine temperature to record is: {engine_temperature}")

    # Connect to Redis and store the temperature
    database = redis.Redis(host="redis", port=6379, db=0, decode_responses=True)
    database.lpush(DATA_KEY, engine_temperature)
    logger.info(f"stashed engine temperature in redis: {engine_temperature}")

    # Keep only the latest 10 values in the list
    while database.llen(DATA_KEY) > HISTORY_LENGTH:
        database.rpop(DATA_KEY)
    
    # Retrieve the list of temperatures from Redis
    engine_temperature_values = database.lrange(DATA_KEY, 0, -1)
    logger.info(f"engine temperature list now contains these values: {engine_temperature_values}")

    logger.info(f"record request successful")
    return {"success": True}, 200

# If the /collect endpoint is not needed, consider removing it
@app.route('/collect', methods=['POST'])
def collect_engine_temperature():
    return {"success": True}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000)
