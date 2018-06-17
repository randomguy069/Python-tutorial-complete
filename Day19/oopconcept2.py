#contains inheritance
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

class Checking(Account):

    def __init__(self,filepath,fee):

        Account.__init__(self,filepath) #executes the super class (Account) method
        self.fee = fee
    def transfer(self,amount):
        self.balance = self.balance - amount - self.fee
checking = Checking("bal.txt",1)
checking.transfer(10)
checking.commit()

#learn on class, object instance, instance variable, doc strings,data members,instantion, inheritance
