#Given two numbers a and b. You need to perform
#  basic mathematical operations on them
a=int(input())
b=int(input())
if operator==1:
    print(a+b)
elif operator==2:
    print(b-a)
elif operator==3:
    print(a*b)
else:
    return "Invalid Input"

#User function Template for python3
# Take a, b and c input and print the greatest of three
q=int(input())
p=int(input())
c=int(input())
x=[a,b,c]
x.sort()
print(x[-1])

#calculator
class Solution:
    def calculate(self, a: int, b: int, operator: int) -> None:
        if operator==1:
            print(a+b,end="")
        elif operator==2:
            print(b-a,end="")
        elif operator==3:
            print(a*b,end="")
        else:
            print("Invalid Input",end="")
            
#dice
#User function Template for python3

class Solution:
    def oppositeFaceOfDice(self, n):
        if n==6:
            return 1
        elif n==2:
            return 5
        elif n==5:
            return 2
        elif n==1:
            return 6
        elif n==3:
            return 4
        elif n==4:
            return 3
        else:
            return "invalid input"
        
        