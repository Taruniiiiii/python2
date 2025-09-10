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
        print("invalid choice"

#Shopping Discount System

total = 0

while True:
    price = float(input("Enter item price: "))
    if price == 0:
        break#if give value is 0 it does not take any prices further
    total += price #every item price is added to total

print("total bill before discount: ",total)

#discount is applied acc to user spending
if total>=5000:
    discount=total*0.20 #20% discount applied
elif total>=3000:
    discount=total*0.15 #15% discount
elif total>=1000:
    discount=total*0.10 #10% discount
else:
    discount=0

final_amt=total-discount
print(f"Discount applied: {discount}")#f function is used  to replace variable with actual number
print(f"Final amount: {final_amt}")

# Online Quiz System

score = 0
print("Welcome to Python Quiz")

#1
print("\n1. Who developed Python?")
print("a) Dennis Ritchie\nb) Guido van Rossum\nc) James Gosling\nd) Bjarne Stroustrup")
ans = input("Your answer: ")
if ans.lower()=="b":#lower is small alpabets
    score += 1#score is incremented  if ans is crt

#2
print("\n2. Which keyword is used to define a function in Python?")
print("a) def\nb) function\nc) fun\nd) define")
ans = input("Your answer: ")
if ans.lower()=="a":
    score+=1

#3
print("\n3. Which data structure uses key-value pairs?")
print("a) List\nb) Dictionary\nc) Tuple\nd) Set")
ans = input("Your answer: ")
if ans.lower()=="b":
    score+=1

#4
print("\n4. What is the output of 2 ** 3 in Python?")
print("a) 6\nb) 8\nc) 9\nd) 5")
ans = input("Your answer: ")
if ans.lower()=="b":
    score+=1

#5
print("\n5. Which of the following is immutable?")
print("a) List\nb) Dictionary\nc) Tuple\nd) Set")
ans = input("Your answer: ")
if ans.lower()=="c":
    score+=1

#Final marks
print(f"Your final score: {score}/5")#score out of 5

if score == 5:
    print("excellent good score!!!")
elif score >= 3:
    print("Good Job!")
else:
    print("Better luck next time")

# Hotel Room Booking System

print("Hotel Booking")
print("Room Types:")
print("1.deluxe= 2000 per night")
print("2.suite= 3000 per night")
print("3.standard= 1500 per night")

choice = int(input("enter room choice 1,2,3: "))
nights = int(input("enter number of nights: "))

if choice==1:
    price=2000
    room="deluxe"
elif choice== 2:
    price=3000
    room="suite"
elif choice==3:
    price=1500
    room="standard"
else:
    print("invalid choice")
    price=0#we can also use exit() function  if user gives invalidd choice  it stps the program
    room="none"

bill=price*nights
gst=bill*0.18
total=bill+gst

print(f"room Type: {room}")
print(f"nights: {nights}")
print(f"base Amount: {bill}")
print(f"GST(18%): {gst}")
print(f"total Payable: {total}")"""

#loops + conditionals + arrays/strings
#1.max num in list
li=[1,2,3,4,5,6,78,4,43,555,123]
li.sort()
print(li)
print(li[-1],"is the max in given list")
#second largest element
print(li[-2],"is the second largest element")

n=int(input())
for i in range(1, n+1):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

