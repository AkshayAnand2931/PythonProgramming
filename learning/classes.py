class account():

    def __init__(self,owner:str,balance:float) -> None:
        self.owner = owner
        self.balance = balance

    def __str__(self) -> str:
        return f"Account owner : {self.owner}\nAccount balance: {self.balance}"
    
    def withdraw(self,amount:float) -> None:
        if amount > self.balance:
            print("Unsufficient Funds!!")
        
        elif amount <= self.balance:
            self.balance -= amount
            print("Withdrawal Successful")
    
    def deposit(self,amount:float)->None:
        self.balance += amount
        print("Deposit successful")

acc1 = account("AK",100)
print(acc1)
acc1.deposit(50)
acc1.withdraw(100)
acc1.withdraw(1000)