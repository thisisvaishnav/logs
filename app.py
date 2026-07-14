import logging
import time
from flask import Flask

app = Flask(__name__)
logger = logging.getLogger(__name__)
logging.basicConfig(level=logging.INFO)

@app.route("/")
def home():
    logger.info("Handling home request")
    time.sleep(0.1)  # fake work so the trace has duration
    return "Hello SigNoz!"

if __name__ == "__main__":
    app.run(port=5000)
