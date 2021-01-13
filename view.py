#imports
from flask import Flask, render_template, redirect, url_for, request, session, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import func
#from models import USER
#from flask_table import Col
from datetime import timedelta
#from models import USER


#create flask
app = Flask(__name__, static_url_path = "", static_folder = "static")
app.secret_key = "hello"
app.permanent_session_lifetime = timedelta(days = 7)
#database config
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

#more login stuff
class User():
    def __init__(self, id, username, password):
        self.id = id
        self.username = username
        self.password = password

def __repr__(self):
    return f"User('{self.username}')"

#def databases():
#    records= []
#    users = USER.query.all()
#    for user in users:
#        user_dict = {'id':user.UserID, 'name':user.username, 'password': user.password}
#        records.append(user_dict)

#def create():
#    if request.form:
#        user = USER(username=request.form.get("username"), password= request.form.get("password"))
#        db.session.add(user)
#        db.session.commit()
#        userid = db.session.query(func.max(USER.UserID))

users = []
users.append(User(id=1, username ='test', password = "password"))
users.append(User(id=2, username ='anothertest', password = "password"))

##home
@app.route ("/")
def home():
    if "user" in session:
        user = session["user"]
        return render_template('home.html', user = user)
    else:
        return render_template('home.html')

##music grid
@app.route ("/music-maker")
def musicgrid():
    if "user" in session:
        user = session["user"]
        return render_template('musicgrid.html', user=user)
    else:
        flash("Log in to access this function")
        return redirect(url_for("logintwo"))

@app.route ("/login")
def login():
    return render_template('account.html')

@app.route("/logintwo", methods=["POST", "GET"])
def logintwo():
    if request.method == "POST":
        session.pop('user_id', None)
        session.permanent = True

        username = request.form["username"]
        password = request.form['password']

        user = [x for x in users if x.username == username][0]
        if user and user.password == password:
            session["user"] = user.id
            flash("You have been logged in")
            return redirect(url_for("user"))

        flash("Password is incorrect or user does not exist.")
        return redirect(url_for('logintwo'))
    
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
        return render_template("user.html", email=email, user = user)
    else:
        flash("You are not logged in!")
        return redirect(url_for("logintwo"))

@app.route("/logout")
def logout():
    flash("You have been logged out", "info")
    session.pop("user", None)
    session.pop("email", None)
    return redirect(url_for("logintwo"))

@app.route("/newuser")
def newuser():
    flash("Create a new account")
    return render_template("newuser.html")

#run
if __name__ == "__main__":
    app.run(debug = True)