#import flask and database
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
##import time
from datetime import timedelta

#create flask app
app = Flask(__name__, static_url_path = '', static_folder = 'static')
app.permanent_session_lifetime = timedelta(days = 7)
app.config['SECRET_KEY'] = 'ineedsleep'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

from bulkofproject import routes