#Write a program to check if a number is divisible by both 3 and 7.
n=int(input())
if n%3==0 and n%7==0:
    print("YES,given number is divisible by 3 and 7")
else:
    print("given num is not divisible by 3 and 7")

#similarly by or
n=int(input())
if n%3==0 or n%7==0:
    print("YES,given number is divisible by 3 and 7")
else:
    print("given num is not divisible by 3 and 7")

#marks
x=int(input())
if x>=90:
    print("A grade")
elif x>=75:
    print("B grade")
elif x>=50:
    print("C grade")
else:
    print("FAIL")
    