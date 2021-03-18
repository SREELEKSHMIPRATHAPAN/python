class Bankaccount:
    def __init__(self):
        accno=float(input("Enter Account Number: "))
        name=str(input("Enter name of Account Holder:"))
        typeofacc=str(input("Enter Type of Account:"))
        self.balance=0
        

    def deposit(self):
        amount = float(input("\nEnter amount to be deposited: "))
        self.balance += amount 
        print("\n Amount Deposited:", amount)
 
    def withdraw(self):
        amount = float(input("\nEnter amount to be withdrawn: "))
        if self.balance >= amount:
            self.balance -= amount
            print("\n You Withdrew:", amount) 
        else:
            print("\n Insufficient balance ") 

    def display(self):
        print("\nAvailable balance is:",self.balance)

s = Bankaccount()     
s.deposit() 
s.withdraw() 
s.display() 


        
