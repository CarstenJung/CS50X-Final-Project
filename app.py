from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename
# Import os for file upload
import os

# Import Helper Functions
from helper import *

# Global Variables
global_image_colors = ()


# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"

# Set up File Uploads
app.config['UPLOAD_FOLDER'] = 'static/uploads'
""" app.config['MAX_CONTENT_PATH'] = 1024 * 1024 """

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
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                              username=request.form.get("username"))
            if len(rows) != 0:
                return render_template("sorry.html", message="Username already exists")
            else:
                db.execute("INSERT INTO users (username, hash) VALUES (:username, :hash)", username=request.form.get(
                    "username"), hash=generate_password_hash(str(request.form.get("password"))))

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
            rows = db.execute("SELECT * FROM users WHERE username = :username",
                              username=request.form.get("username"))
            if len(rows) != 1 or not check_password_hash(rows[0]["hash"], str(request.form.get("password"))):
                return render_template("sorry.html", message="Invalid username and/or password")
            else:
                session["user_id"] = rows[0]["id"]

                # Load Colors From API
                global result
                result = load_more()

                return render_template("console.html", colors=result)

    return render_template("login.html")


# Console
@app.route("/console", methods=["GET", "POST"])
@login_required
def console():
    """Show console"""
    # Load Colors From API
    if request.method == "GET":
        global result
        result = load_more()

        return render_template("console.html", colors=result)

    # Reload API when button is clicked
    if request.method == "POST":
        if 'refresh' in request.form:
            result = load_more()
            return render_template("console.html", colors=result)

        if 'save' in request.form:
            for color in result:
                db.execute("INSERT INTO colors (r, g, b, session) VALUES (?, ?, ?, ?)",
                           color[0], color[1], color[2], session["user_id"])

    return render_template("console.html", colors=result)


# Logout
@app.route("/logout", methods=["GET", "POST"])
def logout():
    # Forget any user_id
    session.clear()

    return redirect("/")


# My Colors
@app.route("/mycolors", methods=["GET", "POST"])
@login_required
def mycolors():
    # Add color to user's list
    if request.method == "POST":
        if 'clear_schemes' in request.form:
            db.execute("DELETE FROM colors WHERE session=?",
                       session["user_id"])

        if 'clear_imgColors' in request.form:
            db.execute("DELETE FROM img_colors WHERE session=?",
                       session["user_id"])

        return redirect(url_for("mycolors"))

    else:
        color_db = db.execute(
            "SELECT * FROM colors WHERE session=?", session["user_id"])
        img_colors = db.execute(
            "SELECT * FROM img_colors WHERE session=?", session["user_id"])

        return render_template("mycolors.html", colors=color_db, img_colors=img_colors)


# Scan Image
@app.route("/scan", methods=["GET", "POST"])
@login_required
def scan():
    # Add color to user's list
    return render_template("scan.html")


@app.route('/scanned', methods=['GET', 'POST'])
@login_required
def upload_file():
    if request.method == 'POST':
        if 'img_submit' in request.form:
            # Get image
            f = request.files['image']
            # Save image
            f.save(os.path.join(
                app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))

            with open('static/uploads/' + f.filename, 'rb') as image:
                global global_image_colors
                global_image_colors = scan_image(image)

            return render_template("scanned.html", color=global_image_colors)

        if 'img_color_save' in request.form:
            for colors in global_image_colors:
                db.execute("INSERT INTO img_colors (r, g, b, session) VALUES (?, ?, ?, ?)",
                           colors[0], colors[1], colors[2], session["user_id"])

            return redirect(url_for("mycolors"))

    return render_template("mycolors.html")


# Analyse Colors
@app.route('/analyse', methods=['GET', 'POST'])
def analyse():
    if request.method == 'GET':
        return render_template("analyse.html")

    if request.method == 'POST':
        if not request.form.get("analyse_color"):
            return render_template("sorry.html", message="Please enter a color")

        if 'color_search' in request.form:
            # Get color
            color = request.form.get("analyse_color")
            # Analyse color
            color = analyse_color(color)

            return render_template("analyse.html", color=color)

    return render_template("analyse.html")


if __name__ == '__main__':
    app.run(debug=True)
