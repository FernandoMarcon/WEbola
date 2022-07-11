from flask import Flask
from flask_sse import sse

app = Flask(__name__)

app.config["CACHE_TYPE"] = "null"
app.config["REDIS_URL"] = "redis://localhost"
# app.config['REDIS_PORT'] = 6379
app.register_blueprint(sse, url_prefix='/stream')

from application import routes
