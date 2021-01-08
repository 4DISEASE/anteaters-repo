#imports
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
#from models import USER

#create flask
app = Flask(__name__, static_url_path = "", static_folder = "static")
app.secret_key = "hello"

#database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

def __repr__(self):
    return f"User('{self.username}')"

#app routes
##temp

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

@app.route("/logintwo", methods=["POST", "GET"])
def logintwo():
    if request.method == "POST":
        user = request.form["nm"]
        session["user"] = user
        flash("You have been logged in")
        return redirect(url_for("user"))
    else:
        if "user" in session:
            flash("You are already logged in")
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user", methods=["POST", "GET"])
def user():
    email = None
    if "user" in session:
        user = session["user"]

        if request.method == "POST":
            email = request.form["email"]
            session["email"] = email
            flash("email has been submitted")
        else:
            if "email" in session:
                email = session["email"]

        return render_template("user.html", email=email)
    else:
        flash("You are not logged in!")
        return redirect(url_for("logintwo"))

@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("logintwo"))

#run
if __name__ == "__main__":
    app.run(debug = True)