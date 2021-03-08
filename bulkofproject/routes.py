#imports
##import flask and database
from flask import flash, redirect, render_template, request, session, url_for
from bulkofproject import app, db
##import api
import bulkofproject.billboardAPI as billboardAPI
from bulkofproject.models import database

#app routes
##create user
@app.route('/register', methods = ['POST', 'GET'])
def register():
    if request.method == "POST":
        #retrieve username and password from html
        usr = request.form.get('username')
        pw = request.form.get('password')
        #commit username and password to database
        dbcommit = database(username = usr, password = pw, song = "none", artist = "artist")
        db.session.add(dbcommit)
        db.session.commit()
        flash("New account successfully created")
        #send user back to login
        return redirect(url_for('login'))
    #render template
    flash("Create a new account")
    return render_template('register.html')

##login
@app.route('/login', methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        #query database and set up session
        users = database.query.all()
        session.pop('user_id', None)
        session.permanent = True

        #retrieve username and password from html
        username = request.form['username']
        password = request.form['password']

        #check if username and password match
        try:
            user = [user for user in users if user.username == username][0]
            #successful login
            if user and user.password == password:
                session['user'] = user.username
                flash("You have been logged in")
                return redirect(url_for('user'))
            #incorrect username/password
            else:
                flash("Password is incorrect or user does not exist.")
        except:
            flash("User is incorrect or does not exist.")
    else:
        if 'user' in session:
            flash("You are already logged in")
            return redirect(url_for('user'))
        return render_template("login.html")

##logout
@app.route('/logout')
def logout():
    flash("You have been logged out")
    session.pop('user', None)
    session.pop('email', None)
    return redirect(url_for('login'))

##user/session
@app.route('/user', methods = ["GET", "POST"])
def user():
    if 'user' in session:
        user = session['user']
        return render_template('user.html', user = user, insession = True)
    else:
        flash("You are not logged in")
        return redirect(url_for('login'))

##home
@app.route('/')
def home():
    if 'user' in session:
        user = session['user']
        return render_template('home.html', user = user, insession = True)
    else:
        return render_template('home.html', insession = False)

##piano
@app.route('/piano')
def piano():
    if 'user' in session:
        user = session['user']
        return render_template('piano.html', user = user, insession = True)
    else:
        flash("Log in to access this function")
        return redirect(url_for('login'))

##favorite song/artist
@app.route('/favorites')
def favorites():
    if 'user' in session:
        user = session['user']
        return render_template('favorites.html', user = user, insession = True)
    else:
        return render_template('favorites.html', insession = False)

##billboard
@app.route('/billboard')
def billboard():
    if 'user' in session:
        user = session['user']
        return render_template('billboard.html', user = user, insession = True, data = billboardAPI.billboarddata())
    else:
        return render_template('billboard.html', data = billboardAPI.billboarddata())
##easter egg
@app.route('/references')
def references():
    if 'user' in session:
        user = session['user']
        return render_template('references.html', user = user, insession = True)
    else:
        return render_template('references.html', insession = False)