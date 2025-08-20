#area of circle using operator
radius=int(input())
area = 3.14 * radius * radius
print("Area of a circle is: " + str(area))

#comparison operators
print(5>7)#false
print(5!=7)#true
print(5==7)#false
print(7>=5)#true

#2 user inputs whether they are equal using == operator
a=str(input())
A=str(input())
print(a==A)

#combine comparisions
num1=int(input())
num2=int(input())
print(num1>0 and num2<50)# false if 1 condion is not true
print(num1>0 or num2<50)#true if 1 condition is true"""

#assignment operators
num=10
num+=5#adds 5 so 10
num-=3# sub 3 so 12
print(num)#output:12

#2
n=int(input())
n*=4 # given num * 4
print(n)

#distance in km and convert into meters
km=int(input())
m=km*1000
print(m)