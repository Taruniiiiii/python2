#Create a tuple containing your 5 favorite fruits and
#  print them one by one using a loop
"""fav_fruits=("apple","pineapple","kiwi")
for fruits in fav_fruits:
    print(fruits)"""

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