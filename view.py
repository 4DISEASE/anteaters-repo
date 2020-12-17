#imports
from flask import Flask, render_template
import sqlalchemy

#create flask
app = Flask(__name__)

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
@app.route ("music-maker")
def grid():
    return render_template('musicgrid')



if __name__ == "__main__":
    app.run(debug = True)