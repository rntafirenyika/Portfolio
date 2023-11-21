import os
from datetime import datetime, timezone, timedelta
from dateutil import parser
from dateutil import tz
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, zar, requires_access_level, is_valid_email, message, is_past_24_hours, decrypt_key

from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib

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

def main():
    daily_limit = 900
    batch_size = 100

    tasks_wip = list(wipid["wip_id"] for wipid in (db.execute("SELECT wip_id FROM wip WHERE wip_status = ?", 'Incomplete')))

    # Get the current datetime
    current_datetime = datetime.now()

    # Format the datetime
    utcTime = current_datetime.strftime('%Y-%m-%d %H:%M:%S.%f')

    for task in tasks_wip:
        # Query database for task details
        rows = db.execute("SELECT * FROM wip WHERE wip_id = ?", task)
        pwip_id = rows[0]["wip_id"]

        if rows[0]["wip_type"] == 'd':

            # get the last run date
            last_run = rows[0]["utcDTStamp"]

            # Send emails if it has been more than 24 hours since the last run date.
            if is_past_24_hours(last_run):
                pemail_id = rows[0]["email_id"]
                pcategory_id = rows[0]["category_id"]
                pcountry_id = rows[0]["country_id"]
                puserid = rows[0]["user_id"]
                psubject = rows[0]["wip_subject"]
                pmessagebody = rows[0]["wip_message"]
                if rows[0]["cv_name"] is not None:
                    # Extract the filename, file type, and file data from the database row
                    filename = rows[0]["cv_name"]
                    file_type = rows[0]["cv_type"]
                    file_data = rows[0]["cv_data"]

                    output_folder = 'C:\Users\Tafirenyikas\OneDrive\Developer\BES\temp'
                    file_path = os.path.join(output_folder, f"{filename}.{file_type}")
                    with open(file_path, 'wb') as f:
                        f.write(file_data)
                else:
                    file_path = None

                previous_day_count = db.execute("SELECT COUNT('email') AS emailcount FROM emaillist WHERE email_id <= ? AND country_id = ? and category_id = ? AND activity_id = ?", pemail_id, pcountry_id, pcategory_id, 1)[0]["emailcount"]

                current_day_limit = daily_limit + previous_day_count

                total_emails_sent = 0

                today_batch_total = previous_day_count

                full_count = db.execute("SELECT COUNT(email) AS emailcount FROM emaillist WHERE category_id = ? AND country_id = ? AND activity_id = ?", pcategory_id, pcountry_id, 1)[0]["emailcount"]

                # Prepare the email message
                msg = message(psubject, pmessagebody, attachment=file_path)

                # initialize connection to our email server, we will use gmail here
                with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
                    smtp.ehlo()
                    smtp.starttls()

                    SMTP_USERNAME = (db.execute("SELECT email FROM users WHERE user_id = ?", puserid))[0]['email']
                    SMTP_PASSWORD = decrypt_key((db.execute("SELECT encrypted_key FROM users WHERE user_id = ?", puserid))[0]['encrypted_key'])

                    if not SMTP_PASSWORD or SMTP_PASSWORD == 'NULL':
                        continue

                    # Login with your email and password
                    smtp.login(SMTP_USERNAME, SMTP_PASSWORD)

                    while today_batch_total < current_day_limit or today_batch_total != full_count:
                        batch_emails = [entry['email'] for entry in (db.execute(f"SELECT email FROM emaillist WHERE country_id = ? AND category_id = ? AND activity_id = ? LIMIT {batch_size} OFFSET {today_batch_total}", pcountry_id, pcategory_id, 1))]

                        # Provide some data to the sendmail function!
                        smtp.sendmail(from_addr=SMTP_USERNAME, to_addrs=batch_emails, msg=msg.as_string())

                        for email in batch_emails:
                            db.execute("INSERT INTO history (hist_subject, email, category_id, country_id, user_id) VALUES(?, ? ,?, ?, ?)", psubject, email, pcategory_id, pcountry_id, puserid)
                            total_emails_sent += 1
                            today_batch_total += 1

                            if total_emails_sent == daily_limit:
                                # Make a new wip to be done the next day
                                lastSent_email_id = (db.execute("SELECT email_id FROM emaillist WHERE email = ?", email))[0]['email_id']
                                db.execute("INSERT INTO wip (user_id, email_id, category_id, country_id, wip_status, wip_type, wip_message, wip_subject, cv_name, cv_type, cv_data, DTStamp, utcDTStamp) VALUES(?, ? ,?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", puserid, lastSent_email_id, pcategory_id, pcountry_id, 'Incomplete', 'd', pmessagebody, psubject, filename, file_type, file_data, utcTime, utcTime)
                                print(f"{pwip_id} completed. Next batch will run after 24hrs")

                                # Close the previous job
                                db.execute("UPDATE wip SET wip_status = ? WHERE wip_id = ?", "Complete", task)

                        if len(batch_emails) < batch_size:
                            db.execute("UPDATE wip SET wip_status = ? WHERE wip_id = ?", "Complete", task)
                            break
                #Remove temporary file
                print(f"{pwip_id} completed.")
                os.remove(file_path)
            else:
                print(f"{pwip_id} is not yet due.")

if __name__ == "__main__":
    main()