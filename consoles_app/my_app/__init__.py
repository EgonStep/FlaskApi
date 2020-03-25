from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Api

app = Flask(__name__)
app.config['SQLAlchemy_DATABASE_URI'] = 'sqlite:///database\\application.db'
db = SQLAlchemy(app)
api = Api(app)

from my_app.console.views import console
from my_app.series.views import series

app.register_blueprint(console)
app.register_blueprint(series)

db.create_all()
