class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
        


    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            return self
        else: 
            amount > self.balance
            self.balance = self.balance - 5
        return print("Insuficient funds: Charging a $5 fee")

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self, amount):
        self.balance = amount*0.10 + amount
        return self


class User:
    def __init__(self, first_name, savings_start_balance, checking_start_balance):
        self.first_name = first_name
        self.account = {
            "Savings": BankAccount(int_rate=0.10, balance=savings_start_balance),
            "Checking": BankAccount(int_rate=0.20, balance=checking_start_balance),
        }
    def account_display(self):
        temp= ""
        print(self.first_name+"'s Account Balance\n")
        for key,val in self.account.items():
            temp +=(f"{key}:${val.balance} \n")
        
        print(temp)
        


Stef = User("Stef", 1000, 100)   
Chris = User("Chris", 100, 1000)

Stef.account["Savings"].deposit(100).deposit(100).withdraw(40)
Stef.account["Checking"].deposit(4000)
Stef.account_display()


Chris.account["Savings"].deposit(0).deposit(100).withdraw(40)
Chris.account["Checking"].deposit(300)
Chris.account_display()

