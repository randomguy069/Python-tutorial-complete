class Account:

    def __init__(self,filepath):
        self.filepath = filepath
        with open(filepath,'r') as file:
            self.balance = int(file.read())

    def withdraw(self,amount):
        self.balance = self.balance - amount

    def deposit(self,amount):
        self.balance= self.balance + amount

    def commit(self):
        with open(self.filepath,"w") as file:
            file.write(str(self.balance))

account = Account("accountbalance.txt") #creating an object. Passing the txt filepath
print(account.balance) #if you type print(account), it prints the object id and also it's address
account.withdraw(100)
account.commit()
account.deposit(1100)
account.commit()
