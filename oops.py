#2 feb
class Cat:
    species="street"

    def __init__(self,name,age):
        self.name=name
        self.age=age
cat1=Cat("jam",5)
print(cat1.name)
print(cat1.age)
print(cat1.species)

##
class students:
    def display(self,name,age):
        self.name=name
        self.age=age
st=students()#creating empty object
st.display("taruni",19)
print(st.name)

#
class Bank_acc:
    def __init__(self):
        self.balance=0
    def deposit(self,amount):
        self.balance+=amount
    def withdraw(self,amount):
        if amount<=self.balance:
            self.balance-=amount
        else:
            print("insufficient balance")
    def show_balance(self,balance):
        print("rem balannce",self.balance)
acc=Bank_acc
acc.deposit(100)