#1 mutable
#list creation and access elements
colours=["red", "blue", "green", "yellow"]
print(colours)
#access element at index 2
print(colours[2])
colours[2]="purple"
#replacing element at index 2 with purple
print(colours)

#2 tuple immutable
num = (10, 20, 30)
print(num)
print(num[0])
#immutable (shows error)'tuple' object does not support item assignment
#num[1]=70
#3
var1 = 42 """
var2 = 3.14 
var3 = "hello" 
var4 = True 
var5 = [1, 2] """
var6 = (1, 2) 
var7 = {"a": 1} 
var8 = {1, 2} 
variables = [var1,var2,var3,var4,var5,var6,var7,var8]
print(variables)
print(type(var1))#int
print(type(var2))#float
print(type(variables))#list