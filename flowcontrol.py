#Given two numbers a and b. You need to perform
#  basic mathematical operations on them
a=int(input())
b=int(input())
if operator==1:
    print(a+b)
elif operator==2:
    print(b-a)"""
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
            return
        elif n==1:
            return 6
        elif n==3:
            return 4
        elif n==4:
            return 3
        else:
            return "invalid input"
        
#day=2
#1..You are given a string s, you need to print its characters at
#  even indices(index starts at 0).
def stringJumper(s):
    for i in range(0,len(s),2):
        # from 0 to length of str and skip 2
        print(s[i], end="")
        #printing character and separating characters by nothing

#2..
#print the numbers from x to 0 in decreasing order in a single line.
#User function Template for python3
x = int(input())
for i in range(x,-1,-1):
    print(i,end=" ")

#3...
#print the numbers from 1 to x in the order as
# 12, 22, 32, 42, 52, ... (in increasing order).
def printIncreasingPower(x):
    i=1# start from 1
    while(i*i<=x): until i matches or less that given number multiply
        print (i*i , end = " ")
        i=i+1 # i changes and goes to next num

#3...given a number n. The number n can be negative or positive.
# If n is negative, print numbers from n to 0 by adding 1 to n
#  the neg function. If positive, print numbers from n-1 to 0 by
# subtracting 1 from n in the pos function."""
def pos(n):
    for i in range(n-1,-1,-1):
        print(i,end=" ")
        
    
def neg(n):
    for i in range(n,1,1):
        print(i,end=" ")