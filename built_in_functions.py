#Use len() to find how many characters are in "Python".
word="python"
print(len(word))#6

#find max
num=(5, 10, 15, 20)
print(max(num),"is max")
print(sum(num),"is sum of num")

#convert list to tuple
li=[1, 2, 3, 4]
tup=tuple(li)
print(tup)

#sorting
ex=[9, 3, 5, 2]
tup1=sorted(ex)
print(tup1)


#zip()
#pairs up elements from two or more sequences
names=["Taruni","Mahesh","ashritha"]
marks=[95,88,92]

combined=zip(names, marks)
print(list(combined))


#all
num=[1, 2, 3, 4]
result=all(n<10 for n in num)#all ele are greater than 10 so true
print(result)


#any()
num2=[1, 2, 3, 0]
print(any(num2))#there are numbers other than 0
#if there is all 0's hen it gives false

#map()
def double(x):
    return x*2

numbers=[1, 2, 3, 4]
result=map(double,numbers)#maps double and number
print(list(result))


#ex2
words = ["taruni", "ishu", "sahasra"]
upper_case=list(map(str.upper,words))
print(upper_case)#gives upper case letters


#filter()
numbers=[1,2,3,4,5,6]
even_nums=filter(lambda x: x%2==0,numbers)#code to print only even numbers using lambda
print(list(even_nums))
odd_nums=filter(lambda x: x%2!=0,numbers)
print(list(odd_nums))


#enumerate()
fruits=["apple","banana","kiwi"]

for index,fruit in enumerate(fruits):
    print(index,fruit)#prints indexes with fruits

#map()Find Length of Each Word
word=["hello", "world","python"]
res=map(len,word)
print(list(res))

#filter() — Numbers Divisible by 3 and 5
exa1=[12, 15, 21, 24, 30, 37, 40]
res1=list(filter(lambda x:x%3==0 and x%5==0,exa1))
print(res1)

#reduce() — Product of All Numbers
from functools import reduce
prob=[2, 3, 4, 5]
n=reduce(lambda x,y:x*y,prob)
print(n)#prints product of all numbers

#zip() — Combine Two Lists into a Dictionary
names = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
new1=dict(zip(names,scores))
print(new1)#output:{'Alice': 85, 'Bob': 92, 'Charlie': 78}

#enumerate() — Print Index + Item
sub=["Math", "Science", "History", "English"]
for index,subjects in enumerate(sub):
    print(index,subjects)

#sorted() — Sort Tuples by Second Value
marks = [("Alice", 50), ("Bob", 75), ("Charlie", 65)]
s=list(sorted(marks,key=lambda x:x[1]))
print(s)

#all() and any() — Check Conditions
prob1=[10, 20, 30, 40, 50]
r1=all(p>5 for p in prob1)
print(r1)
r2=any(p%3==0 for p in prob1)
print(r2)

#Combination (map + filter + lambda)
pro2=[2, 5, 8, 11, 14, 17]
odd=list(filter(lambda x:x%2!=0,pro2))
print(odd,":are the odd nums in list")
sq=map(lambda x:x**2,odd)
print(list(sq),":are the squares od odd  nums")