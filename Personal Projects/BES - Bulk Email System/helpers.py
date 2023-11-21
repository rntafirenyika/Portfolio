import os
from datetime import datetime, timezone, timedelta
from dateutil import parser
from dateutil import tz
import requests
import urllib.parse
import glob
import csv
import pandas as pd
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
import smtplib
from flask import redirect, render_template, request, session
from functools import wraps
import re
from cryptography.fernet import Fernet

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

def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function


def requires_access_level(access_level):
    """
    Decorate routes to give access to certain users.
    """
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if session.get("user_id") is None:
                return redirect("/login")

            userrole = session.get("userrole")
            if userrole not in access_level:
                return apology("You are not authorised!", 403)
            return f(*args, **kwargs)
        return decorated_function
    return decorator


def zar(value):
    """Format value as ZAR."""
    return f"R{value:,.2f}"


def extract_emails():
    # Supported file extensions
    supported_extensions = (".csv", ".xls", ".xlsx")

    # Search for files with supported extensions in the current folder
    matching_files = []
    for extension in supported_extensions:
        matching_files.extend(glob.glob(f"*{extension}"))

    # Read emails from the first matching file
    if len(matching_files) > 0:
        file_path = matching_files[0]

        # Determine the file extension
        file_extension = os.path.splitext(file_path)[1].lower()

        # Read emails from different file formats
        if file_extension in [".xls", ".xlsx"]:
            df = pd.read_excel(file_path, header=None)
            column_index = 0  # Specify the column index (0-based) where the emails are located
            emails = df.iloc[:, column_index].tolist()
        elif file_extension == ".csv":
            with open(file_path, "r") as file:
                reader = csv.reader(file)
                emails = [row[0] for row in reader]
        else:
            return []
    return emails


def is_valid_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    match = re.match(pattern, email)
    return match is not None


def message(subject="", text="", img=None, attachment=None):
    # build message contents
    msg = MIMEMultipart()

    # Add Subject
    msg['Subject'] = subject

    # Add text contents
    msg.attach(MIMEText(text))

    # Check if we have anything given in the img parameter
    if img is not None:
        # Check whether we have the lists of images or not!
        if type(img) is not list:
            # if it isn't a list, make it one
            img = [img]

        # Now iterate through our list
        for one_img in img:
            # read the image binary data
            img_data = open(one_img, 'rb').read()
            # Attach the image data to MIMEMultipart using MIMEImage,
            # we add the given filename using os.basename
            msg.attach(MIMEImage(img_data, name=os.path.basename(one_img)))

    # We do the same for attachments as we did for images
    if attachment is not None:
        if not isinstance(attachment, list):
            attachment = [attachment]

        for file in attachment:
            if isinstance(file, str):
                # If the attachment is a file path (string)
                filename = os.path.basename(file)
                with open(file, 'rb') as f:
                    file_data = f.read()

                mime_type = 'application/octet-stream'
            else:
                # If the attachment is a FileStorage object
                filename = file.filename
                file_data = file.read()

                mime_type = file.mimetype
                if not mime_type:
                    mime_type = 'application/octet-stream'

            attachment = MIMEApplication(file_data, name=filename)
            attachment['Content-Disposition'] = f'attachment; filename="{filename}"'

            # At last, Add the attachment to our message object
            msg.attach(attachment)

    return msg


def extract_emails(text):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    emails = re.findall(email_pattern, text)
    return emails


def extract_emails_from_docx(docx_file):

    file_path = docx_file

    doc = docx.Document(docx_file)

    # Extract email addresses from the document
    emails = []
    for paragraph in doc.paragraphs:
        # Extract email addresses from plain text
        emails.extend(extract_emails(paragraph.text))

        # Extract email addresses from hyperlinks
        for run in paragraph.runs:
            for field in run.element.iter():
                if field.tag.endswith('hyperlink'):
                    address = field.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id')
                    if address:
                        hyperlink = doc.part.related_parts[address]
                        emails.extend(extract_emails(hyperlink._element.attrib.get('Target', '')))


    return emails


def extract_emails_from_pdf(pdf_file):
    emails = []
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            text = reader.pages[page_number].extract_text()
            emails.extend(extract_emails(text))
    return emails


def extract_emails_from_spreadsheet(spreadsheet_file):

    file_path = spreadsheet_file

    # Read emails from different file formats
    if file_path.endswith('.xls') or file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path, header=None)
        column_index = 0  # Specify the column index (0-based) where the emails are located
        emails = df.iloc[:, column_index].tolist()
    elif file_path.endswith('.csv'):
        with open(file_path, "r") as file:
            reader = csv.reader(file)
            emails = [row[0] for row in reader]
    else:
        return []
    return emails


def extract_emails_from_images(image_path):
    # Read the image file
    image = cv2.imread(image_path)

    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Apply thresholding to preprocess the image
    _, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

    # Perform OCR using pytesseract
    text = pytesseract.image_to_string(threshold)

    # Extract email addresses using regular expressions
    email_addresses = extract_emails(text)

    return email_addresses


def extract_emails_from_pdf_to_csv(pdf_file, output_file):
    emails = []
    with open(pdf_file, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        num_pages = len(reader.pages)
        for page_number in range(num_pages):
            text = reader.pages[page_number].extract_text()
            emails.extend(extract_emails(text))

    # Save emails to CSV file in the current folder
    current_folder = os.getcwd()
    output_path = os.path.join(current_folder, output_file)

    with open(output_path, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Emails"])
        writer.writerows([[email] for email in emails])

    return emails


def encrypt_key(key):
    encryption_key = os.getenv('ENCRYPTION_KEY').encode()
    f = Fernet(encryption_key)
    encrypted_key = f.encrypt(key.encode())
    return encrypted_key


def decrypt_key(encrypted_key):
    encryption_key = os.getenv('ENCRYPTION_KEY').encode()
    f = Fernet(encryption_key)
    decrypted_key = f.decrypt(encrypted_key).decode()
    return decrypted_key


def is_past_24_hours(specified_date):
    # Convert the datetime string to a datetime object
    specified_datetime = datetime.strptime(specified_date, '%Y-%m-%d %H:%M:%S.%f')

    # Get the current datetime
    current_datetime = datetime.now()

    # Calculate the time difference
    time_difference = current_datetime - specified_datetime

    # Check if the time difference is greater than 24 hours
    return time_difference > timedelta(hours=24)


def is_past_24_hours2(specified_date):
    # Get the current date and time in UTC
    current_datetime = datetime.now(tz.tzutc())

    # Parse the specified datetime string
    specified_datetime = datetime.fromisoformat(specified_date)

    # Apply the specified time zone offset
    specified_datetime = specified_datetime.replace(tzinfo=tz.gettz(specified_date[-6:]))

    # Convert the specified datetime to UTC
    specified_datetime_utc = specified_datetime.astimezone(tz.tzutc())
    print(specified_datetime_utc)

    # Calculate the time difference in hours
    time_difference = current_datetime - specified_datetime_utc
    hours_difference = time_difference.total_seconds() / 3600

    # Check if the time difference is greater than 24 hours
    if hours_difference > 24:
        return True
    else:
        return False


def allowed_file(filename):
    ALLOWED_EXTENSIONS = ['pdf', 'png', 'jpg', 'jpeg', 'gif', 'csv', 'xls', 'xlsx', 'docx']
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS
