#sep5
#two sum
"""nums=[1,2,3,4,5,6]
target=int(input())
n=len(nums)
for i in range(n):
       for j in range(i+1,n):
              if nums[i]+nums[j]==target:
                   print([i,j])

#Multiplication Table
num=int(input("enter a num u want to multiply: "))
for i in range(1,11):
      print(num,"X",i,"=",num*i)
#ATM Cash Withdrawal Simulation
balance=int(5000)
while balance>0:
    withdraw=int(input("How much u want to withdraw: "))
    if withdraw<=balance:
        balance=balance-withdraw
        print(withdraw,"here is your money")
    else:
        print("insufficient balance")
    break

#Parking Lot Counter
max_slots=5
count=int(input())
if count>=max_slots:
    print("parking full")
else:
    while count<max_slots:
        count+=1
        if count>=max_slots:
            print("parking full")
        else:
            print("you can park your vehicle")

            
#Password Attempt System
act_password="taruni@123"
count=0
while count<3:
    password=input("enter your password: ")
    if password==act_password:
        print("login success")
        break#exits the loop if entered pass is crt
    else:
        print("wrong pass")
        count=count+1
if count==3:
    print("acc locked")
#bus ticket booking
tickets=int(input("no of tickets: "))
for i in range(1,tickets+1):
    name=str(input("enter your name: "))
    age=int(input("age:" ))
    print(name,age)"""

# Cafeteria Ordering System

total=0
print("1: Pizza = 120\n2: Burger = 80\n3: Coffee = 50\n0: Exit")
while True:
    choice=int(input("enter your choice"))
    if choice==1:
        total=total+120
        print("Pizza added ")
    elif choice == 2:
        total += 80
        print("Burger added ")
    elif choice == 3:
        total += 50
        print("Coffee added ")
    elif choice == 0:
        break
    else:
        print("invalid choice")
print("final bill= ",total)



