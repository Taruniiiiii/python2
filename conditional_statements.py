
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
    print("adult")"""
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
