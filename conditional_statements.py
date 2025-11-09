
"""
def friends_in_trouble(j_angry, s_angry):
    if(j_angry == True and s_angry == True):
        return True
    elif(j_angry == True and s_angry == False):
        return False

#2
def checkOddEven(x):
    if x%2==0:
        return "Even"
    else:
        return "Odd"
    
#3 return True if  the words "cat" and "hat" appear same 
# number of times in str, otherwise return False.
def cat_hat(str):
  if str.count("cat") == str.count("hat"):
      return True
  else:
      return False

#4
a=int(input())
if(a>100):
    print("Big")
else:
    print("Number")

##
if age<=12:
    print("Travel for free")
else:
    print("Pay for ticket")

##
age=25

if age<=12:
    print("child.")
elif age<=19:
    print("teen")
elif age<=35:
    print("Young adult")
else:
    print("adult")


#sep2
#login verification
u="tarunimedi"
p="jack13"
usn=str(input("enter username: "))
passw=str(input("enter your password: "))
if u==usn and p==passw:
    print("login successfulllll..")
else:
    print("wrong credentials")
#online shopping discount
n=int(input("bill amount: "))
if n>=5000:
    print("You get 20% discount")
elif n>=2000:
    print("you get 10% discount")
else:
    print("no discount")
#Vowel or Consonant Checke
v=str(input("enter a char: "))
if v=="a" or v=="e" or v=="i" or v=="o" or v=="u":
    print("given char is a vowel")
else:
    print("not a vowel")

#sep3
#Hospital Bed Allocation system

condition=str(input("Patient condition(critical/serious/normal): "))
if condition=="critical":
    print("icu bed")
elif condition=="serious":
    print("special ward")
elif condition=="normal":
    print("general ward")
else:
    print("no patient")

#Smart Toll Payment System
vehicle_type=str(input("car/bike/truck: "))
payment_type=str(input("cash/FASTag"))
if vehicle_type=="car" and payment_type=="FASTag":
    print("Car fare=100,after 10% discount=90")
elif vehicle_type=="bike" and payment_type=="FAStag":
    print("Bike fare=50,after 10% discount=45")
elif vehicle_type=="truck" and payment_type=="FAStag":
    print("Truck fare=300,after 10% discount:270")
else:
    if vehicle_type == "car":
        print("Car fare =100+10 service fee='110'")
    elif vehicle_type == "bike":
        print("Bike fare =50+10 service fee='60'")
    elif vehicle_type == "truck":
        print("Truck fare =300+10 service fee='310'")
    else:
        print("Invalid vehicle type")

#sep4

#Smart Parking System
vehicle_type=str(input("Vehicle type(car/bike): "))
time_of_day=str(input("peak time(8-10am)and(5-8pm)||off-peak time(late  night or mid day): "))
parking_time=int(input("How much time are you going to park your vehicle: "))
if vehicle_type=="car" and time_of_day=="peak" and parking_time<12:
    parking_time=parking_time*50+20
    print("to pay...",parking_time)
elif vehicle_type=="bike" and time_of_day=="peak" and parking_time<12:
    parking_time=parking_time*20+20
    print("to pay...",parking_time)
elif parking_time>12:
    print("not allowed!!!")
elif  vehicle_type=="car" and time_of_day=="off-peak":
    parking_time=parking_time*50
    print("to pay...",parking_time)
elif  vehicle_type=="bike" and time_of_day=="off-peak":
    parking_time=parking_time*20
    print("to pay...",parking_time)
else:
    print("invalid vehicle_type")

#Bank ATM Cash Dispenser
pin=int(1234)
withdrawal_amt=int(input("enter the amt you want to withdraw"))
balance_amt=int(input("Enter balance amt: "))
pin_crt=int(input("enter your pin: "))
if pin_crt==pin and balance_amt>=withdrawal_amt and withdrawal_amt%100==0:
    print("Here is your money!!!")
else:
    print("invalid")
"""
