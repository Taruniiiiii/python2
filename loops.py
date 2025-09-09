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
    print(name,age)

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

#Movie Ticket Booking
tickets = int(input("How many tickets: "))
tot=0

for i in range(1,tickets+1):
    age = int(input("Enter age of passenger : "))

    if age < 12:
        print("Child Price=50")
        tot+=50
    elif age <= 59:
        print("Adult Price=100")
        tot+=100
    else:
        print("Senior Citizen Price=70")
        tot+=70
print("total tickets: ",tickets)
print("tot amt: ",tot )
#Student Result Processing
tot=0
for i in range(1,6):
    marks=int(input(f"enter marks of sub {i}: "))#replace str with actual values
    tot=tot+marks#updates  tot value acc to given marks
average=tot/5
print("tot marks: ",tot)
print("average: ",average)
if average>=90:
    print("grade A")
elif average>=75:
    print("grade A")
if average>=50:
    print("grade A")
else:
    print("FAIL!!")

#Library Fine System
days_late=int(input("no.of days late: "))
if days_late<=5:
    fine=days_late*2
elif days_late<=10:
    fine=days_late*5
elif days_late<=30:
    fine=days_late*10
else:
    fine="cancelled"
print("fine= ",fine)

#Bank ATM Simulation
balance=5000
withdrawal_amt=int(input("enter withdrawal amt: "))
if withdrawal_amt % 100 != 0:
    print("withdrawal amount must be in multiples of 100")
elif withdrawal_amt > balance:
    print("Insufficient balance")
else:
    balance -= withdrawal_amt
    print(" collect your cash")
    print("remaining balance:", balance)

#using loops
balance=5000
while True:
    print("1.check balance")
    print("2.withdraw")
    print("3.deposit amt")
    print("0.exit")

    choice=int(input("enter your choice: "))

    if choice==1:
        print("current balance",balance)
    elif choice==2:
        withdraw=int(input("enter withdrawal amt: "))
        if withdraw%100!=0:
            print("withdrawal amt is not multiple of 100")
        elif withdraw>balance:
            print("insufficient balance")
        else:
            balance=balance-withdraw
            print("remainning balance",balance)
    
    elif choice==3:
        dep_amt=int(input("dep amt: "))
        balance=balance+dep_amt
        print("updated  balance: ",balance)
    elif choice==0:
        print("exit")
        break
    else:
        print("invalid choice")"""

#Shopping Discount System

total = 0

while True:
    price = float(input("Enter item price: "))
    if price == 0:
        break
    total += price

print("Total bill before discount = ", total)

# Apply discounts
if total>=5000:
    discount=total*0.20 # 20% discount
elif total>=3000:
    discount=total * 0.15   # 15% discount
elif total >= 1000:
    discount = total * 0.10   # 10% discount
else:
    discount = 0

final_amount = total - discount
print(f"Discount applied: {discount}")
print(f"Final payable amount: {final_amount}")