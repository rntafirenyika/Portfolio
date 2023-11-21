import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")

# Make sure API key is set
if not os.environ.get("API_KEY"):
    raise RuntimeError("API_KEY not set")


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
    """Show portfolio of stocks"""

    # Get user id of logged in user
    user_id = session.get("user_id")

    # Get cash balance
    cash = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]

    # Get stocks data
    stocks_data = db.execute(
        "SELECT stock_symbol, stock_name, SUM(num_shares) AS num_shares FROM transactions WHERE user_id = ? GROUP BY stock_symbol HAVING SUM(num_shares) > 0", user_id)

    # Get stocks current price and current value, and append to stocks data
    for stock in stocks_data:
        stock.update(current_price=lookup(stock["stock_symbol"])["price"])
        stock.update(total=stock["current_price"] * stock["num_shares"])

    # Calculate total portfolio value (Stocks and cash)
    stocks_value = sum(item["total"] for item in stocks_data)
    portfolio_value = stocks_value + cash

    return render_template("index.html", stocks_data=stocks_data, cash=cash, portfolio_value=portfolio_value)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":

        # Retrive form data
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Get stock data from IEX
        stock_data = lookup(symbol)

        # Ensure number of shares is a positive integer.
        if str(shares).isnumeric() == False or shares == "0":
            return apology("Invalid Shares", 400)

        # Ensure symbol input is not blank.
        elif not symbol:
            return apology("Missing Symbol", 400)

        # Ensure symbol exists.
        elif stock_data == None:
            return apology("Invalid Symbol", 400)

        else:
            shares = int(shares)
            user_id = session.get("user_id")
            balance = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
            stock_price = stock_data["price"]
            stock_name = stock_data["name"]
            stock_symbol = stock_data["symbol"]
            purchase_amount = shares * stock_price

            if purchase_amount > balance:
                return apology("insufficient Funds", 400)
            else:
                type = "buy"
                new_balance = balance - purchase_amount
                db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, user_id)
                db.execute("INSERT INTO transactions (user_id, type, stock_symbol, stock_name, stock_price, num_shares) VALUES(?, ?, ?, ?, ?, ?)",
                           user_id, type, stock_symbol, stock_name, stock_price, shares)

                flash('Transaction successful!')
                
                # Redirect user to home page
                return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session.get("user_id")
    history_data = db.execute(
        "SELECT transaction_date, stock_symbol, stock_name, type, num_shares, stock_price FROM transactions WHERE user_id = ? ORDER BY transaction_number ASC", user_id)
    cash_data = db.execute(
        "SELECT transaction_date, type, amount FROM cash WHERE user_id = ? ORDER BY transaction_number ASC", user_id)
    return render_template("history.html", history_data=history_data, cash_data=cash_data)


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
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
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        flash('You were successfully logged in')

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        symbol = request.form.get("symbol")
        stock_data = lookup(symbol)
        if stock_data != None:
            return render_template("quoted.html", stock_data=stock_data)
        else:
            return apology("Missing Symbol", 400)
    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":

        # Retrive form data
        username = request.form.get("username")
        password = request.form.get("password")
        confirmation = request.form.get("confirmation")

        # Query database to check if username already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Ensure username was submitted
        if not username or len(rows) == 1:
            return apology("must provide username or already exists", 400)

        # Ensure a password has been submitted
        elif not password:
            return apology("password may not be blank", 400)

        # Ensure passwords match
        elif password != confirmation:
            return apology("Passwords must match", 400)

        # Insert username and hash into database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)

        # Record initial cash in database
        db.execute("INSERT INTO cash (user_id, type, amount) VALUES(?, ?, ?)", rows[0]["id"], "Deposit", 10000)

        # Login user after registration

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        flash('Registration successful!')

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""

    user_id = session.get("user_id")
    symbols = db.execute(
        "SELECT stock_symbol FROM transactions WHERE user_id = ? GROUP BY stock_symbol HAVING SUM(num_shares) > 0", user_id)

    if request.method == "POST":
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")
        shares_owned = db.execute(
            "SELECT SUM(num_shares) FROM transactions WHERE stock_symbol = ? AND user_id = ?", symbol, user_id)[0]["SUM(num_shares)"]

        # Ensure user owns shares of that stock.
        if symbol not in list(stock["stock_symbol"] for stock in symbols):
            return apology("Symbol not owned", 400)

        # Ensure number of shares is a positive integer.
        elif str(shares).isnumeric() == False or shares == "0":
            return apology("Invalid Shares", 400)

        # Ensure user own that many shares of the stock.
        elif int(shares) > shares_owned:
            return apology("Not enough Shares", 400)

        stock_data = lookup(symbol)
        shares = int(shares)
        balance = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
        stock_price = stock_data["price"]
        stock_name = stock_data["name"]
        stock_symbol = stock_data["symbol"]
        sold_amount = shares * stock_price
        type = "sell"
        new_balance = balance + sold_amount
        shares_sold = -shares
        db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, user_id)
        db.execute("INSERT INTO transactions (user_id, type, stock_symbol, stock_name, stock_price, num_shares) VALUES(?, ?, ?, ?, ?, ?)",
                   user_id, type, stock_symbol, stock_name, stock_price, shares_sold)

        flash('Transaction successful!')

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("sell.html", symbols=symbols)


@app.route("/deposit", methods=["GET", "POST"])
@login_required
def deposit():
    """Add additional cash to account"""

    user_id = session.get("user_id")

    if request.method == "POST":
        deposit = request.form.get("deposit")

       # Ensure amount input is not blank.
        if not deposit:
            return apology("Enter an amount", 400)

        # Ensure deposit amount is a positive integer.
        elif str(deposit).isnumeric() == False or deposit == "0":
            return apology("Invalid Amount", 400)

        else:
            deposit = int(deposit)
            balance = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
            new_balance = balance + deposit
            db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, user_id)

            # Record transaction in database
            db.execute("INSERT INTO cash (user_id, type, amount) VALUES(?, ?, ?)", user_id, "Deposit", deposit)

            flash('Transaction successful!')

            # Redirect user to home page
            return redirect("/")

    else:
        return render_template("deposit.html")


@app.route("/withdraw", methods=["GET", "POST"])
@login_required
def withdraw():
    """Remove/reduce cash in account"""

    user_id = session.get("user_id")

    if request.method == "POST":
        withdrawal = request.form.get("withdraw")

       # Ensure amount input is not blank.
        if not withdrawal:
            return apology("Enter an amount", 400)

        # Ensure deposit amount is a positive integer.
        elif str(withdrawal).isnumeric() == False or withdrawal == "0":
            return apology("Invalid Amount", 400)

        else:
            withdrawal = int(withdrawal)
            balance = db.execute("SELECT cash FROM users WHERE id = ?", user_id)[0]["cash"]
            new_balance = balance - withdrawal

            if new_balance < 0:
                return apology("Insufficient Cash", 400)

            else:
                db.execute("UPDATE users SET cash = ? WHERE id = ?", new_balance, user_id)

                # Record transaction in database
                db.execute("INSERT INTO cash (user_id, type, amount) VALUES(?, ?, ?)", user_id, "Withdrawal", withdrawal)

                flash('Transaction successful!')

                # Redirect user to home page
                return redirect("/")

    else:
        return render_template("withdraw.html")


@app.route("/changepassword", methods=["GET", "POST"])
@login_required
def changepassword():
    """Change user password"""

    user_id = session.get("user_id")

    if request.method == "POST":
        oldpassword = request.form.get("oldpassword")
        newpassword = request.form.get("newpassword")
        confirmation = request.form.get("confirmation")
        rows = db.execute("SELECT * FROM users WHERE id = ?", user_id)

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
        db.execute("UPDATE users SET hash = ? WHERE id = ?", generate_password_hash(newpassword), user_id)

        flash('Password change successful!')

        # Redirect user to home page
        return redirect("/")

    else:
        return render_template("changepassword.html")