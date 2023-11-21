import os

from cs50 import SQL
from flask import Flask, flash, jsonify, redirect, render_template, request, session

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///birthdays.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Add the user's entry into the database
        name = request.form.get("name")
        month = int(request.form.get("month"))
        day = int(request.form.get("day"))
        if month not in list(i for i in range(1,13)) or day not in list(i for i in range(1,32)):
            return redirect("/")

        db.execute("INSERT INTO birthdays (name, month, day) VALUES(?, ?, ?)", name, month, day)
        return redirect("/")

    else:

        # Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays")
        return render_template("index.html", birthdays=birthdays)


@app.route("/remove", methods=["GET", "POST"])
def remove():

    # Remove birthday
    id = request.form.get("id")
    if id:
        db.execute("DELETE FROM birthdays WHERE id = ?", id)
    return redirect("/")


@app.route("/edit", methods=["GET", "POST"])
def edit():

    # Edit birthday entry
    id = request.form.get("id")
    if id:
        # Display the entries in the database on index.html
        birthdays = db.execute("SELECT * FROM birthdays WHERE id = ?", id)
        return render_template("edit.html", birthdays=birthdays)


@app.route("/update", methods=["GET", "POST"])
def update():

    id = request.form.get("id")
    name = request.form.get("name")
    month = int(request.form.get("month"))
    day = int(request.form.get("day"))
    if id:
        # Update birthday entry
        db.execute("UPDATE birthdays SET name = ?, month = ?, day = ? WHERE id = ?", name, month, day, id)
        return redirect("/")

