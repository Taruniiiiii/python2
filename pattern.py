#1 square of Stars
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
    