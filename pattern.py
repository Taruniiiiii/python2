"""#1 square of Stars
n=int(input())
for i in range(n):
    for j in range(n):
         print("*",end="")
    print()
    
#2 right-angled triangle of stars
n=int(input())
for i in range(0,n+1):
    for j in range(i):
         print("*",end="")
    print()

#Write a program to print all odd numbers from 1 to n.
n=int(input())
for i in range(0,n,2):
     n=i+1
     print(n)"""

#Write a program to find the factorial of a number.
n=int(input())
fact=1
for i in range(1,n):
    fact=fact*i
    print(fact)