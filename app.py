from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

# Import API Functions 
from api import *

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///colors.db")

# Make sure responses aren't cached
@app.after_request
def after_request(response):
    """Disable caching"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response

# Load DB into variable
db = SQL("sqlite:///colors.db")


# Homepage
@app.route("/")
def index():
    """Show colors"""
    return render_template("index.html")

# Register
@app.route("/register", methods=["GET", "POST"])
def register():
    """Register new user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("sorry.html", message="Please enter a username")
        elif not request.form.get("password"):
            return render_template("sorry.html", message="Please enter a password")
        elif not request.form.get("confirm"):
            return render_template("sorry.html", message="Please confirm your password")
        elif request.form.get("password") != request.form.get("confirm"):
            return render_template("sorry.html", message="Passwords do not match")
        else:
            rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
            if len(rows) != 0:
                return render_template("sorry.html", message="Username already exists")
            else:
                db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get("username"), hash=generate_password_hash(request.form.get("password")))
                
                return render_template("login.html")
    return render_template("register.html")

# Login
@app.route("/login", methods=["GET", "POST"])
def login():
    """Login user"""
    if request.method == "POST":
        if not request.form.get("username"):
            return render_template("sorry.html", message="Please enter a username")
        elif not request.form.get("password"):
            return render_template("sorry.html", message="Please enter a password")
        else:
            rows = db.execute("SELECT * FROM users WHERE username = :username", username=request.form.get("username"))
            if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
                return render_template("sorry.html", message="Invalid username and/or password")
            else:
                session["user_id"] = rows[0]["id"]
                return redirect("console.html")
    
    
    return render_template("login.html")


# Console
@app.route("/console", methods=["GET", "POST"])
@login_required
def console():
    """Show console"""
    
    return render_template("console.html")


# Logout
@app.route("/logout", methods=["GET", "POST"])
def logout():
    # Forget any user_id
    session.clear()
    
    return redirect("/")


# My Colors
@app.route("/mycolors", methods=["GET", "POST"])
def mycolors():
    # Add color to user's list
    
    return render_template("mycolors.html")

# Scan Image
@app.route("/scan", methods=["GET", "POST"])
def scan():
    # Add color to user's list
    
    return render_template("scan.html")