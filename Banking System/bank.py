from users import User


# Bank class inheriting from User Class
class Bank(User):
    def __init__(self, name: str, age: int, gender: str) -> None:
        super().__init__(name, age, gender)
        self.balance: float = 0.00

    #Method to deposit to account
    def deposit(self, amount: float):
        self.balance += amount
        print(f"You Have Successfully Deposited ${amount} To Your Account.")
    
    # Method to withdraw from account
    def withdraw(self, amount: float):
        if amount > self.balance:
            print("Insufficient Balance")
            self.account_balance()
        else:
            self.balance -= amount
            print(f"You Have Successfully Withdrawn {amount} From Your Account.")

    # Method to check account balance
    def account_balance(self):
        print(f'Balance: ${self.balance}')

if __name__=='__main__':
    user1 = Bank("Solomon Bestz", 39, "Male")
    user1.user_detail()
    user1.account_balance()
    user1.deposit(10)
    user1.withdraw(20)

    

    