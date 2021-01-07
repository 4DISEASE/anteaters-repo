#imports
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
#from models import USER

#create flask
app = Flask(__name__, static_url_path = "", static_folder = "static")

#database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

def __repr__(self):
    return f"User('{self.username}')"

#app routes
##temp
@app.route ("/grid")
def grid():
    return render_template('grid.html')

##home
@app.route ("/")
def home():
    return render_template('home.html')

##music grid
@app.route ("/music-maker")
def musicgrid():
    return render_template('musicgrid.html')

@app.route ("/login")
def login():
    return render_template('account.html')

#run
if __name__ == "__main__":
    app.run(debug = True)