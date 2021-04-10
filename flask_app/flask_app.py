from flask import Flask
from database.database import db, ma
from flask_app.config import create_database, turn_off_warn


app = Flask(__name__)

turn_off_warn(app)
db.init_app(app)
ma.init_app(app)
create_database(app)








