""""#Create a tuple containing your 5 favorite fruits and
#  print them one by one using a loop
fav_fruits=("apple","pineapple","kiwi")
for fruits in fav_fruits:
    print(fruits)

#Find the length of a tuple (4, 5, 6, 7, 8, 9).
num=(4,5,6,7,8,9)
print(len(num))

#Check whether an element (like 7) exists in a tuple.
if 17 in num:
    print("exists in tuple")
else:
    print("does not exist in tuple")

#Convert a tuple (10, 20, 30, 40) to a list, change the 
# second element to 99, and convert it back to a tuple.
tup=(10,20,30,40)
li=list(tup)
li[1]=99
li[2]=30
tup=tuple(li)
print(tup)

#Add and remove elements in a set:
set1={2,3,4,5,6,7}
set1.add(8)
set1.discard(7)
set1.remove(3)
print(set1)


#Find the maximum and minimum values from a tuple (5, 8, 1, 3, 7).
tup=(5,8,1,3,7)
print(max(tup),"is the max in tup")

#slicing
nums=(10,20,30,40,50)
print(nums[:3])#first 3 elements
print(nums[3:])#last 2 elements
print(nums[-1:0:-1])#reverse except first element
print(nums[::-1])#reverse

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
C = {3, 2, 6, 4}
#union
print(A | B)
#intersection
print(A & B)#common elements in both sets
#difference
print(A - B)
print(B - A)
#symmetric difference
print(A ^ B)#not common in both sets

#Write a program to find common elements in 3 sets.
print(A&B&C,"common in 3")

#Given a list of tuples (name, age), find the average age using tuple unpacking.
people=[("taruni",18),("manu",20),("vinya",21),("ashritha",19)]
print(people)
tot_age=0
for name,age in people:
    tot_age=tot_age+age
avg_age=tot_age/len(people)
print(avg_age,"avg_age")

#Find the highest-priced product Find the average price
products = (("Laptop", 60000), ("Phone", 30000), ("Tablet", 25000))
tot_price=0
max_price =0
max_product = ""
for name,price in products:
    tot_price+=price
    if price>max_price:
        max_price=price
        max_product=name
average_price=tot_price/len(products)
print(max_product,"max_products")
print(max_price,"max_price")
print(average_price,"average_pricee")

#You have a list of tuples representing coordinates:
coords = [(1, 2), (3, 4), (5, 6)]
for a,b in coords:
    print(a,end=" ")
    print(b)

#create a set that only includes the words whose length is more than 3 letters.
words = ["apple", "is", "red", "and", "sweet"]
result=set()
for word in words:
    if len(word)>3:
        result.add(word)
print(result)
#same problem in 1 line
result={word for word in words if len(word)>3}
print(result)

#reverse a tuple without using the reversed()
ex=(1, 2, 3, 4)
print(ex[::-1])

#Find Second Largest Number
ex2=(5, 7, 2, 9, 1)
lis=list(ex2)
lis.sort()
print(lis)
print(lis[-2],"is the second highest num in ex2")
"""
#Multiply All Numbers in a Tuple
ex3=(1, 2, 3, 4)
num=0
for i in ex3:
    num=num+i
    print(num)

#Duplicate Email Detector
mails = ["taruni@gmail.com", "ash@mail.com", "taruni@gmail.com", "soh@mail.com"]
unique_emails=set()
duplicate_emails=set()
for i in mails:
    if i in unique_emails:
        duplicate_emails.add(i)
    else:
        unique_emails.add(i)
print("duplicate emails",duplicate_emails)

#unique city finders
customers = [("Mahesh", "Hyderabad"), ("Taruni", "Chennai"), ("Kiran", "Hyderabad")]
unique_cities=set()
notunique_cities=set()
for i,j in customers:
    if j in unique_cities:
        notunique_cities.add(j)
    else:
        unique_cities.add(j)
unique_cities = unique_cities - notunique_cities
print("unique_cities:",unique_cities)

#Employee Skill Matcher
emp1 = {"Python", "SQL", "Excel"}
emp2 = {"Python", "Java", "Excel"}
print(emp1 & emp2,"common skills in both emps")
print(emp1-emp2,"is unique from emp2")
print(emp1 ^ emp2,"are not common")

#Attendance Comparison
day1 = {"Taruni", "Mahesh", "Ravi"}
day2 = {"Mahesh", "Ravi", "Asha"}
print(day1&day2,"attended both days")
print(day1-day2,"attended only day 1")
print(day2-day1,"attended only day 2")

#Tuple Sorting by Price
items = [("Apple", 120), ("Banana", 40), ("Cherry", 200)]
items.sort(key=lambda x: x[1])#lambda=temporaruy function..here used once for sorting
for fruit,price in items:  #x each ele in the tuple here in the list
    print(fruit,":",price)#key= specific rule or logic


#Word Uniqueness Checker
text = "Python is fun and learning Python is interesting"
word_count={}
print(text.split())
for word in text.split():
    if word in word_count:
        word_count[word]+=1
    else:
        word_count[word]=1

unique_words = {word for word, count in word_count.items() if count == 1}
print("unique_words:",unique_words)


ex=(10,20,30)
set_list= list(ex)
print(set_list)
set_list[1]=99
print(set_list)
li_tup=tuple(set_list)
print(li_tup)

names=['a', 'b', 'c']
values=[10, 20, 30]
m_dict=dict(zip(names,values))
print(m_dict)

n=7
for i in range(1,n+1):
    print(" " * (n-i),end="")# prints spaces acc to i=rows as rows increases spaces decreases
    print("*"*(2*i-1))#prints * odd no of times

#Write a function that finds the maximum element in a list.
li=[1,2,4,888,5,44,7]
def maxEleInList(li):
    return max(li)
print(maxEleInList(li),"is max in list")