#Estimates a user's typical food expenditure.
times = int(input("How many times a week do you eat at the student cafeteria? "))
price = float(input("The price of a typical student lunch? "))
gspend = float(input("How much money do you spend on groceries in a week? "))
total_spend = times * price + gspend
daily_spend = total_spend / 7
print("")
print("Average food expenditure:")
print(f"Daily: {daily_spend} euros")
print(f"Weekly: {total_spend} euros")