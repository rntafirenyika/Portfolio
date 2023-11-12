#Bank account class with private method __service_charge()
class BankAccount:
    # Constructor which takes the name of the owner, account number and balance as arguments.
    def __init__(self, owner: str, account_number: str, balance: float):
        self.__owner = owner
        self.__account_number = account_number
        self.__balance = balance

    # for depositing money to the account        
    def deposit(self, amount: float):
        if amount > 0:
            self.__balance += amount
            self.__service_charge()
        else:
            raise ValueError("Deposit amount cannot be less than zero")

    # for withdrawing money from the account.            
    def withdraw(self, amount: float):
        if amount > 0:
            self.__balance -= amount
            self.__service_charge()
        else:
            raise ValueError("Withdrawal amount cannot be less than zero")
    
    @property        
    def balance(self):
        return self.__balance

    # Decreases the balance on the account by one percent whenever either of the methods deposit or withdraw is called.        
    def __service_charge(self):
        self.__balance -= self.__balance * 0.01