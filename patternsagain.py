#29
"""
for i in range(5):
    for j in range(5):
        if j<=5:
            print("*",end=" ")
    print()

* * * * * 
* * * * * 
* * * * *
* * * * *
* * * * *"""

#hollo square
n=4
for i in range(n):
    for j in range(n):
        if i==0 or i==n-1 or j==0 or j==n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
"""
* * * * 
*     * 
*     *
* * * *
"""
n=4
for i in range(n):
    for j in range(n-i-1):
        print(" ",end="")
    for j in range(n):
        print("*",end="")
    print()
