from flask_app.flask_app import db
from os.path import dirname, join, abspath


def turn_off_warn(app):
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SQLALCHEMY_DATABASE_URI'] = False

def create_database(app):
    try:

        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:12345@localhost/user'
        db.create_all(app=app)
    except:

        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + join(dirname(dirname(abspath(__file__))), 'db.sqlite')
        db.create_all(app=app)



