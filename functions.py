#syntax:
"""
def function_name(parameters):
    #function body
    """
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

#first name last name
def emp(first_name,last_name):
    print(first_name,last_name)
emp(first_name="taruni",last_name="medishetty")
emp(first_name="ashritha",last_name="sadhu")
emp(last_name="medishetty",first_name="sohan")