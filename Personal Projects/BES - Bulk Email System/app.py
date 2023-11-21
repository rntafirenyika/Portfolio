import os
import datetime
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, zar, requires_access_level, is_valid_email, message, extract_emails, extract_emails_from_docx, extract_emails_from_pdf, extract_emails_from_spreadsheet, extract_emails_from_images, encrypt_key, decrypt_key, is_past_24_hours, allowed_file
from cryptography.fernet import Fernet
import pytz
from datetime import datetime, timezone
from dateutil import parser
from dateutil import tz
from flask_paginate import Pagination

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

import docx
import PyPDF2
from werkzeug.utils import secure_filename
import cv2
import pytesseract

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["zar"] = zar

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///emails.db")

# Read encryption key from a text file
with open('encryption_key.txt', 'r') as file:
    encryption_key = file.read().strip()
    os.environ['ENCRYPTION_KEY'] = encryption_key

# Make sure ENCRYPTION_KEY is set
if not os.environ.get("ENCRYPTION_KEY"):
    raise RuntimeError("ENCRYPTION_KEY not set")

# Maximum login attempts
MAX_LOGIN_ATTEMPTS = 5

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show Dashboard"""

    return render_template("index.html")


@app.route("/addemails", methods=["GET", "POST"])
@login_required
def addemails():
    """add new emails to database"""
    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
	    ...
    return render_template("addemails.html")


@app.route("/history", methods=['GET'])
@login_required
def history():
    """Show history of emails sent"""
    page = request.args.get('page', 1, type=int)
    per_page = 150  # Number of history items per page

    userid = session.get("user_id")

    # Fetch total history items
    total_history_items = db.execute("SELECT COUNT(*) FROM history WHERE user_id = ?", userid)[0]["COUNT(*)"]

    # Calculate the number of pages
    num_pages = (total_history_items + per_page - 1) // per_page

    # Calculate the offset
    offset = (page - 1) * per_page

    # Fetch history data
    history_data = db.execute(
        "SELECT DTStamp AS date, hist_subject, email, category, country_name AS country FROM history JOIN categories ON categories.category_id = history.category_id JOIN countries ON countries.country_id = history.country_id WHERE user_id = ? ORDER BY date ASC LIMIT ? OFFSET ?",
        userid, per_page, offset
    )

    # Calculate start_page and end_page for pagination
    visible_pages = 10
    start_page = max(1, page - (visible_pages // 2))
    end_page = min(start_page + visible_pages - 1, num_pages)

    # Check if "..." was clicked and update start_page and end_page accordingly
    if request.args.get('more', None) == 'true':
        new_start_page = min(end_page + 1, num_pages - visible_pages + 1)
        new_end_page = min(new_start_page + visible_pages - 1, num_pages)
        start_page, end_page = new_start_page, new_end_page

    return render_template("history.html", history_data=history_data, num_pages=num_pages, current_page=page, start_page=start_page, end_page=end_page, visible_pages=visible_pages)


@app.route("/emaillist", methods=["GET", "POST"])
@login_required
def emaillist():
    """Show all emails in database"""
    return render_template("emaillist.html")


@app.route("/edb", methods=["GET", "POST"])
@login_required
def edb():
    """Send emails from database"""
    userid = session.get("user_id")
    categories = db.execute("SELECT * FROM categories")
    countries = db.execute("SELECT * FROM countries")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        category_id = int(request.form.get("category"))
        country_id = int(request.form.get("country"))
        subject = request.form.get("subject")
        messagebody = request.form.get("message")
        localTime = request.form.get("localTime")

        # Get the current datetime
        current_datetime = datetime.now()

        # Format the datetime
        utcTime = current_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')

        # Get the uploaded file
        attachment = request.files['file'] if 'file' in request.files else None

        if not allowed_file(attachment.filename):
            return apology("Invalid file type", 400)

        # Prepare the email message
        msg = message(subject, messagebody, attachment=attachment)

        # Retrieve email addresses in batches
        batch_size = 100
        total_emails_sent = 0
        daily_limit = 900
        lastSent_email_id = None

        # initialize connection to our email server, we will use gmail here
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()

            SMTP_USERNAME = (db.execute("SELECT email FROM users WHERE user_id = ?", userid))[0]['email']
            SMTP_PASSWORD = decrypt_key((db.execute("SELECT encrypted_key FROM users WHERE user_id = ?", userid))[0]['encrypted_key'])

            if not SMTP_PASSWORD or SMTP_PASSWORD == 'NULL':
                return apology("Key not set.", 400)

            # Login with your email and password
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)

            while total_emails_sent < daily_limit:
                batch_emails = [entry['email'] for entry in (db.execute(f"SELECT email FROM emaillist WHERE country_id = ? AND category_id = ?  AND activity_id = ? LIMIT {batch_size} OFFSET {total_emails_sent}", country_id, category_id, 1))]

                # Provide some data to the sendmail function!
                smtp.sendmail(from_addr=SMTP_USERNAME, to_addrs=batch_emails, msg=msg.as_string())

                for email in batch_emails:

                    db.execute("INSERT INTO history (hist_subject, email, category_id, country_id, user_id, DTStamp, utcDTStamp) VALUES(?, ? ,?, ?, ?, ?, ?)", subject, email, category_id, country_id, userid, localTime, utcTime)
                    total_emails_sent += 1

                    if total_emails_sent == daily_limit:
                        lastSent_email_id = (db.execute("SELECT email_id FROM emaillist WHERE email = ?", email))[0]['email_id']

                if len(batch_emails) < batch_size:
                    break

        #If any emails remain from the total emails that can be sent then make a database entry for the remaining emails to be sent after 24 hours.
        total_db_emails = (db.execute("SELECT COUNT(email) FROM emaillist WHERE country_id = ? AND category_id = ? AND activity_id = ?", country_id, category_id, 1))[0]['COUNT(email)']
        if total_emails_sent != total_db_emails:
            cv_name = None
            cv_type = None
            wip_type = 'd' # d for emails sent using database emails
            if attachment:
                if attachment.filename != '':
                    cv_data = attachment.read()
                    cv_name, cv_type = attachment.filename.rsplit('.', 1)
                else:
                    cv_data = None
            else:
                cv_data = None
            db.execute("INSERT INTO wip (user_id, email_id, category_id, country_id, wip_status, wip_type, wip_message, wip_subject, cv_name, cv_type, cv_data, DTStamp, utcDTStamp) VALUES(?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", userid, lastSent_email_id, category_id, country_id, 'Incomplete', wip_type, messagebody, subject, cv_name, cv_type, cv_data, localTime, utcTime)

        flash('Done - all emails sent!')

        # Redirect user
        return redirect("/edb")

    return render_template("edb.html", categories=categories, countries=countries)


@app.route("/efile", methods=["GET", "POST"])
@login_required
def efile():
    """Send emails from file"""
    userid = session.get("user_id")
    categories = db.execute("SELECT * FROM categories")
    countries = db.execute("SELECT * FROM countries")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        category_id = int(request.form.get("category"))
        country_id = int(request.form.get("country"))
        subject = request.form.get("subject")
        messagebody = request.form.get("message")
        localTime = request.form.get("localTime")

        # Get the current datetime
        current_datetime = datetime.now()

        # Format the datetime
        utcTime = current_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')

        # Get the uploaded files
        file = request.files['efile']
        attachment = request.files['file'] if 'file' in request.files else None

        if not allowed_file(attachment.filename) or not allowed_file(file.filename):
            return apology("Invalid file type", 400)

        # Extract the file extension
        filename = secure_filename(file.filename)
        file_extension = filename.rsplit('.', 1)[-1].lower()

        if file_extension not in ['csv', 'xls', 'xlsx', 'docx', 'pdf', 'jpg', 'jpeg', 'png', 'bmp', 'tif', 'tiff', 'gif', 'webp', 'pbm', 'pgm', 'ppm']:
            return apology("File type not supported", 400)

        # Save the uploaded file with the correct extension
        file_path = 'uploaded_file.' + file_extension
        file.save(file_path)

        # Extract email addresses based on file type
        emails = []
        if file_path.endswith('.docx'):
            emails = extract_emails_from_docx(file_path)
        elif file_path.endswith('.pdf'):
            emails = extract_emails_from_pdf(file_path)
        elif file_path.endswith(('.xls', '.xlsx', '.csv')):
            emails = extract_emails_from_spreadsheet(file_path)
        elif file_path.endswith(('.jpg', '.jpeg', '.png', '.bmp', '.tif', '.tiff', '.gif', '.webp', '.pbm', '.pgm', '.ppm')):
            emails = extract_emails_from_images(file_path)

        # initialize connection to our email server, we will use gmail here
        with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.ehlo()
            smtp.starttls()

            SMTP_USERNAME = (db.execute("SELECT email FROM users WHERE user_id = ?", userid))[0]['email']
            SMTP_PASSWORD = decrypt_key((db.execute("SELECT encrypted_key FROM users WHERE user_id = ?", userid))[0]['encrypted_key'])

            if not SMTP_PASSWORD or SMTP_PASSWORD == 'NULL':
                return apology("Key not set.", 400)

            # Login with your email and password
            smtp.login(SMTP_USERNAME, SMTP_PASSWORD)

            msg = message(subject, messagebody, attachment=attachment)

            # Send email to the email addresses.
            for email in emails:
                # Provide some data to the sendmail function!
                smtp.sendmail(from_addr=SMTP_USERNAME, to_addrs=email, msg=msg.as_string())
                db.execute("INSERT INTO history (hist_subject, email, category_id, country_id, user_id, DTStamp, utcDTStamp) VALUES(?, ? ,?, ?, ?, ?, ?)", subject, email, category_id, country_id, userid, localTime, utcTime)

        # Flash message and delete the files after processing
        flash('Done - all emails sent!')
        os.remove(file_path)

        # Redirect user
        return redirect("/efile")

    return render_template("efile.html", categories=categories, countries=countries)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    if "login_attempts" not in session:
        session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":

        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username").strip())

        # Ensure username exists
        if len(rows) != 1:
            return apology("Username does not exist", 403)

        # Ensure username is an active member
        if rows[0]["activity_id"] == 2:
            return apology("User Inactive", 403)

        # Ensure password is correct
        if check_password_hash(rows[0]["hash"], request.form.get("password")):
            # Successful login, reset login attempt count
            if "login_attempts" in session:
                del session["login_attempts"]

            # Remember which user has logged in
            session["user_id"] = rows[0]["user_id"]

            # Remember user role
            session["userrole"] = db.execute("SELECT userrole FROM users WHERE user_id = ?", session["user_id"])[0]["userrole"]

            user = (db.execute("SELECT (SELECT titles.title || ' ' || first_name || ' ' || surname FROM users JOIN titles ON titles.title_id = users.title_id WHERE users.user_id = ?) AS name FROM users", session["user_id"]))[0]["name"]

            flash(f'Welcome {user}')

            # Redirect user to home page
            return redirect("/")

        else:
            # Increment login attempt count
            login_attempts = session.get("login_attempts", 0)
            session["login_attempts"] = login_attempts + 1
            if login_attempts + 1 >= MAX_LOGIN_ATTEMPTS:
                # Maximum attempts reached, deactivate user
                flash("Maximum login attempts reached. Your account has been locked, contact support.")
                db.execute("UPDATE users SET activity_id = ? WHERE username = ?", 2, request.form.get("username"))
            else:
                flash(f"Incorrect password. Account will be locked after {MAX_LOGIN_ATTEMPTS - int(session.get('login_attempts'))} attempts.")
            return render_template("login.html")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user details
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    """Change user password"""

    user_id = session.get("user_id")

    if request.method == "POST":
        oldpassword = request.form.get("oldpassword")
        newpassword = request.form.get("newpassword")
        confirmation = request.form.get("confirmation")
        rows = db.execute("SELECT * FROM users WHERE user_id = ?", user_id)

        # Ensure old password was submitted
        if not oldpassword:
            return apology("must provide old password", 400)

        # Ensure new password is not blank.
        elif not newpassword:
            return apology("new password may not be blank", 400)

        # Ensure passwords match
        elif newpassword != confirmation:
            return apology("Passwords(new) must match", 400)

        # Ensure old password is correct
        elif not check_password_hash(rows[0]["hash"], oldpassword):
            return apology("old password incorrect", 400)

        # Insert username and hash into database
        db.execute("UPDATE users SET hash = ? WHERE user_id = ?", generate_password_hash(newpassword), user_id)

        flash('Password change successful!')

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("changepassword.html")


@app.route("/config", methods=["GET", "POST"])
@login_required
def config():

    user_id = session.get("user_id")

    if request.method == "POST":

        # Add the user's entry into the database
        date = request.form.get("localTime")
        akey = request.form.get("akey")
        if akey:
            db.execute("UPDATE users SET encrypted_key = ?, datekey = ? WHERE user_id = ?", encrypt_key(akey), date, user_id)

        return redirect("/config")

    else:

        # Display the entries in the database
        data = db.execute("SELECT encrypted_key, datekey FROM users WHERE user_id = ?", user_id)
        #if decrypt_key(data[0]['encrypted_key']) == 'NULL':
        if not data:
            data = []
        return render_template("config.html", data=data)


@app.route("/removek", methods=["GET", "POST"])
@login_required
def removek():

    user_id = session.get("user_id")

    # Remove key
    if user_id:
        date = request.form.get("localTime")
        db.execute("UPDATE users SET encrypted_key = ?, datekey = ? WHERE user_id = ?", encrypt_key('NULL'), date, user_id)
    return redirect("/config")


@app.route("/useradd", methods=["GET", "POST"])
@login_required
@requires_access_level(["admin"])
def useradd():
    """Add new user"""
    user_id = session.get("user_id")
    current_user_role = session.get("userrole")
    titles = db.execute("SELECT * FROM titles")
    genders = db.execute("SELECT * FROM genders")
    status = db.execute("SELECT * FROM activity")
    countries = db.execute("SELECT * FROM countries")

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Retrive form data
        title = request.form.get("title")
        firstname = request.form.get("firstname")
        surname = request.form.get("surname")
        dob = request.form.get("dob")
        gender = int(request.form.get("gender"))
        activity = int(request.form.get("activity"))
        cellnumber = request.form.get("cellnumber")
        email = request.form.get("email")
        country = int(request.form.get("country"))
        username = request.form.get("username")
        userrole = request.form.get("userrole")
        hash = request.form.get("password")
        notes = request.form.get("notes")
        encrypted_key = encrypt_key("NULL")

        # Query database to check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username does not exist already
        if len(rows) == 1 and rows[0]["username"] != "NULL":
            return apology("username already exists", 400)

        # Ensure title exists
        if not title:
            return apology("Missing title", 400)

        # Ensure Name and Surname exists
        if not firstname or not surname:
            return apology("Missing Name or Surname", 400)

        # Ensure gender exists in database
        if gender not in list(gender["gender_id"] for gender in genders):
            return apology("Age group not found", 400)

        # Ensure Activity is valid
        if activity not in list(state["activity_id"] for state in status):
            return apology("Activity Invalid", 400)

        # Ensure country exists in database
        if country not in list(eachcountry["country_id"] for eachcountry in countries):
            return apology("Country not found", 400)

        # Ensure userrole exists in database
        if userrole not in ["admin", "user"]:
            return apology("User role not found", 400)

        # Insert user details and hash into database
        db.execute("INSERT INTO users (title_id, first_name, surname, gender_id, activity_id, email, cell_number, country_id, username, userrole, hash, notes, encrypted_key) VALUES(?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", title, firstname, surname, gender, activity, email, cellnumber, country, username, userrole, generate_password_hash(hash), notes, encrypted_key)

        flash('Registration successful!')

        # Redirect user to memberadd page
        return redirect("/useradd")

    return render_template("useradd.html", titles=titles, genders=genders, status=status, countries=countries)