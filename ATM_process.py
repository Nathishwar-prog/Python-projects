import time as t
class Bank:
    def __init__(self, Name: str, balance: int = 0):
        self.account_holder = Name
        self.balance = balance

    def deposit(self, amount: int = 0):
        self.balance += amount
        return self.balance

    def withdraw(self, amount: int = 0):
        if amount > self.balance:
            return "Insufficient funds"
        self.balance -= amount
        return f"Account Balance: {self.balance}"

    def check(self):
        return self.balance


class ATM(Bank):
    def run(self):
        while True:
            print("*" * 10, "----Main Menu-------", "*" * 10)
            print("1] Deposit Money \n2] Withdraw Money \n3] Check Balance \n4] Exit")
            user: int = int(input("Select the Process: "))
            if user == 1:
                amount: int = int(input("Enter the amount you want to deposit: "))
                print(f"New Balance: {self.deposit(amount)}")
            elif user == 2:
                amount: int = int(input("Enter the amount you want to withdraw: "))
                print(self.withdraw(amount))
            elif user == 3:
                print(f"Current Balance: {self.check()}")
            elif user == 4:
                print("Thank you for using our ATM. Please visit again!")
                break
            else:
                print("Please select a valid option!")

            t.sleep(3)


# Create an instance of ATM and run it
h1 = ATM("John Doe", 1000)  # Example: Account holder "John Doe" with an initial balance of 1000
h1.run()

