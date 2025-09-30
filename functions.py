"""#syntax:
#def=keyword

def function_name(parameters):
    #function body
    """
#ex.1
def function_name():
    print("I'm taruniii")
function_name()#calling function
"""
#ex.2
def evenOdd(x):
    if (x%2==0):
        return "Even"
    else:
        return "Odd"

print(evenOdd(999))
print(evenOdd(8))

#ex.3
def myFun(x=90, y=50):
    print("x: ", x)
    print("y: ", y)

myFun()
#similar
def myFun(x, y=90):
    print("x: ", x)
    print("y: ", y)

myFun(109)

#ex.4
#first name last name
def emp(first_name,last_name):
    print(first_name,last_name)
emp(first_name="taruni",last_name="medishetty")
emp(first_name="ashritha",last_name="sadhu")
emp(last_name="medishetty",first_name="sohan")

#ex.5
def namePlace(name,place,dob):
    print("hi i'm",name)
    print("i'm from",place)
    print("i'm from",dob)

print("emp1")
namePlace("sohan","medak",2011)

print("emp2")
namePlace("thanish",2009,"hyderabad")

#ex
def f1():
    s = "helloooo"
    def f2():
        print(s)
        
    f2()
f1()

#ex
def cube(x):
    return x*x*x
print(cube(2))
#ex.geeksforgeeks
def argumentFunction(a=2,b=3):
    print(a+b)

def firstDigit(n):
    while n>9:
        n=n//10
    return n

#exleetcode
nums=[1,2,3,3,44,1,12,5]
for i in nums:
    if nums.count(i) == 1:
        print(i)

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        n = len(s)
        result = [""] * n   # empty array of length n
        for i in range(n):
            result[indices[i]] = s[i]
        return "".join(result)

#Write a function that takes a string and returns it in reverse.
def reverseString(str):
    return str[::-1]
print(reverseString("taruni"))

#Write a function that finds the maximum element in a list.
li=[1,2,4,888,5,44,7]
def maxEleInList(li):
    return max(li)
print(maxEleInList(li),"is max in list")

#sep28
#Temperature Converter
#Convert Celsius to Fahrenheit."""
def celcius_to_fh(c):
    f=(c*9/5)+32
    return f
print(celcius_to_fh(22),"fahrenheit")
print(celcius_to_fh(37),"fahrenheit")

#Bill Calculator
def bill_calculator(quantity,amounnt):
    total= quantity*amounnt
    return total
print(bill_calculator(4,250),"Is your total bill ")
print(bill_calculator(2,500),"Is your total bill ")

#Voting Eligibility
def voting_eligibility(age):
    if age>=18:
        return "Eligible to vote"
    else:
        return "Not eligible to vote"
print(voting_eligibility(17))
print(voting_eligibility(20))

#Taxi Fare Calculator
def taxi_Calculator(distance_in_km):
    fare=distance_in_km*10
    return fare
print(taxi_Calculator(15),"is your taxi fare")
print(taxi_Calculator(5),"is your taxi fare")

#Student Grading System
def student_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "FAIL"
print(student_grade(33))
print(student_grade(90))

#Discount Finder
def discount_finder(price):
    if price>1000:
        discount=price*0.01
        final_bill=price-discount
        return final_bill
print(discount_finder(2000))

#Restaurant Tip Calculator
def tip_Calculator(bill,tip):
    tip = (bill * tip) / 100#tip is taken in percentage
    final = bill + tip
    return final
print(tip_Calculator(1500,70),"is ur final bill")

#Movie Ticket Price
def ticket_price(cust_age):
    if cust_age<12:
        return 100
    elif cust_age<=60:
        return 200
    else:
        return 150
print(ticket_price(10))
print(ticket_price(50))
print(ticket_price(70))

#Maximum of Two Numbers
def max(a,b):
    if a>b:
        return a
    else:
        return b
print(max(11,21))