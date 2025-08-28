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
     print(n)

#Write a program to find the factorial of a number.
n=int(input())
fact=1
for i in range(1,n):
    fact=fact*i
    print(fact)

#Write a program to reverse a number.
n=int(input())
rev=0
while n>0:
     digit=n%10
     rev=rev*10+digit
     n=n//10
print(rev)

#Write a program to check if a number is Prime or not.
n = int(input())
if n > 1:
    for i in range(2, n):
        if n % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime")
else:
    print("Not Prime")

#Take the sides of a triangle and check if it is valid or not.
a=int(input())
b=int(input())
c=int(input())
if (a+b>c) and (a+c>b) and (b+c>a):
    print("triangle ")
else:
    print("not a triangle")"""

for i in range(5):
    print("taruni medishetty")
