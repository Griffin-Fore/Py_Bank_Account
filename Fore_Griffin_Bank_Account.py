class BankAccount :
    def __init__(self, name, interest_rate, balance):
        self.name = name
        if interest_rate == None:
            self.interest_rate = 0.05
        else:
            self.interest_rate = interest_rate
        if balance == None:
            self.balance = 0
        else:
            self.balance = balance
    
    def deposit(self,amount):
        self.balance += amount
        print(f"Made a Deposit. Balance: {self.balance}")
        return self
    
    def withdraw(self,amount):
        if(self.balance >= amount):
            self.balance -= amount
            print(f"Made a withdrawal. Balance: {self.balance}")
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5.00
        return self
    
    def display_account_info(self):
        print(f"Name: {self.name}, Balance: {self.balance}")
        return self
    
    def yield_interest(self):
        self.balance *= self.interest_rate
        print(f"Interest rate: {self.interest_rate}")
        print(f"Balance: {self.balance}")
        return self
    
account_1 = BankAccount("George", 0.05, 500)
account_2 = BankAccount("Riley", 0.06, 2700)

account_1.deposit(50).deposit(300).deposit(400).withdraw(1000).yield_interest().display_account_info()
account_2.deposit(100).deposit(100).withdraw(400).withdraw(400).withdraw(400).withdraw(400).yield_interest().display_account_info()