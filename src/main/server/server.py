from flask import Flask

from src.main.routes.products_routes import products_routes_bp
from src.models.redis.settings.connection import redis_connection_handler
from src.models.sqlite.settings.connection import sqlitedb_connection_handler

redis_connection_handler.connect()
sqlitedb_connection_handler.connect()

app = Flask(__name__)

app.register_blueprint(products_routes_bp)
