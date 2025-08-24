"""#Write a program to check if a number is divisible by both 3 and 7.
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

#Write a program to find the maximum of four numbers using if-else.
m=int(input())
n=int(input())
o=int(input())
p=int(input())
if m>n:
    print("m is greater")
elif n>o:
    print("n is greater")
elif o>p:
    print("o is greater")
else:
    print("p is greater")"""

#Write a program to check whether a character is uppercase,
#  lowercase, digit, or special character.
q=input()
if q.isupper():
    print("Uppercase letter")
elif q.islower():
    print("lowercase letter")
elif q.isdigit():
    print("digit")
else:
    print("special char")

#d=3
n = int(input())
 if n%2==0 and n>=2 and n<=5:
        print("Not Weird")
    elif n%2==0 and n>=6 and n<=20:
        print("Weird")
    elif n%2==0 and n>20:
        print("Not Weird")
    else:
        print("Weird")
#2
# Print the square of each number on a separate line.
 n = int(input())
    for i in range(0,n):
        n=n+1
        n=i*i
        print(n)
