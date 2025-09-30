#1
tuple = ("apple", "banana", "cherry")
if "apple" in tuple:
  print("Yes, 'apple' is in the fruits tuple")
  #2
tuple1=("a", "b" , "c")
tuple2=(1, 2, 3)
tuple3=tuple1 + tuple2
print(tuple3)
#3 allows duplicate values
tuple4= ("apple", "banana", "cherry", "apple", "cherry")
print(tuple4)
# to find length of tuple
print(len(tuple4))
# type of data
print(type(tuple4))

#set
set={"apple", "banana", True , 0 , False , 1 , "cherry", "apple"}
print(set)
# true and 1 considered same value 
# false and 0 considered same value
print(len(set))

#if particular item is present in set or not
sset = {"apple","banana","cherry"}
print("banana" in sset)#true
#add ele
sset.add("papaya")
print(sset)
sset.remove("papaya")
print(sset)
#can also use "discard" to remove ele
#can remove random ele using "pop"
#clear for full delete
#join multiple sets using union 1st ex.
set1={"a","b","c"}
set2={1,2,3}
set3={"John","Elena"}
set4={"apple","bananas","cherry"}

fullset = set1.union(set2,set3,set4)
print(fullset)
#or
fullset=set1|set2|set3|set4
print(fullset)
