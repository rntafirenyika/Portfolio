# LunchCard and PaymentTerminal
class LunchCard:
    def __init__(self, balance: float):
        self.balance = balance

    def deposit_money(self, amount: float):
        self.balance += amount

    def subtract_from_balance(self, amount: float):
        if amount <= self.balance:
            self.balance -= amount
            return True
        return False

# A payment terminal can handle both cash and card transactions.
class PaymentTerminal:
    def __init__(self):
        # Initially there is 1000 euros in cash available at the terminal
        self.funds = 1000
        self.lunches = 0
        self.specials = 0

    # Paying for normal lunch using cash and returning the appropriate change.
    def eat_lunch(self, payment: float):
        lunch_cost = 2.50
        if payment >= lunch_cost:
            self.funds += lunch_cost
            self.lunches += 1
            change = payment - lunch_cost
            return change
        return payment

    # Paying for special lunch using cash and returning the appropriate change.
    def eat_special(self, payment: float):
        lunch_cost = 4.30
        if payment >= lunch_cost:
            self.funds += lunch_cost
            self.specials += 1
            change = payment - lunch_cost
            return change
        return payment

    # Paying for normal lunch using card
    def eat_lunch_lunchcard(self, card: LunchCard):
        lunch_cost = 2.50
        if subtract_from_balance(lunch_cost):
            card.balance -= lunch_cost
            self.lunches += 1
            return True
        return False

    # Paying for special lunch using card
    def eat_special_lunchcard(self, card: LunchCard):
        lunch_cost = 4.30
        if subtract_from_balance(lunch_cost):
            card.balance -= lunch_cost
            self.specials += 1
            return True
        return False

    # Lets you deposit money on the card.
    # The card owner pays this by cash, so the deposited sum is added to the funds available at the terminal.
    def deposit_money_on_card(self, card: LunchCard, amount: float):
        self.funds += amount
        card.balance += amount
    
if __name__ == "__main__":
    exactum = PaymentTerminal()
    
    card = LunchCard(2)
    print(f"Card balance is {card.balance} euros")
    
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    
    exactum.deposit_money_on_card(card, 100)
    print(f"Card balance is {card.balance} euros")
    
    result = exactum.eat_special_lunchcard(card)
    print("Payment successful:", result)
    print(f"Card balance is {card.balance} euros")
    
    print("Funds available at the terminal:", exactum.funds)
    print("Regular lunches sold:", exactum.lunches)
    print("Special lunches sold:", exactum.specials)