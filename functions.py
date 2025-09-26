#syntax:
#def=keyword
"""
def function_name(parameters):
    #function body
    
#ex.1
def function_name():
    print("I'm taruniii")
function_name()#calling function

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
        for i in range(n):"""
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
