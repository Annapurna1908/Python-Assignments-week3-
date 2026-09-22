class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print("Amount deposited successfully!")
        else:
            print("Invalid amount!")

    def withdraw(self, amount):
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print("Amount withdrawn successfully!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            print("Invalid amount!")

    def display_balance(self):
        print("Account Holder:", self.name)
        print("Current Balance: ₹", self.balance)



# Create account
account = BankAccount("Anu", 5000)

account.display_balance()

account.deposit(2000)
account.display_balance()

account.withdraw(1000)
account.display_balance()