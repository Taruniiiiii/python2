#1
"""list=["apple","banana","cherry"]
list.append("orange")
print(list)

#2
list2=["apple","banana","cherry"]
list2.insert(1, "orange")
print(list2)

#3
list3=["apple","banana","cherry"]
list4=["mango","pineapple","papaya"]
list3.extend(list4)
print(list3)#prints l3,l4 together

#4
lista=["apple","banana","cherry"]
lista.remove("banana")
print(lista)# removes banana from lista

#5 removes the ele which is in index 1 i.e banana
#if u give just pop() it will pop the last ele in list i.e cherry
#can also use del.. cclear is used to clear the list prints []
listb=["apple", "banana", "cherry"]
listb.pop(1)
print(listb)

#6 list using loop
li=["apple","ball","cat","dog"]
i=0
while i < len(li):
    print(li(i))
    i=i+1

#7 sort() arranges in alphabetical order
listc=["orange","mango","kiwi","pineapple","banana"]
listc.sort()
print(listc)

#8 if reverse(descending order)
listc.sort(reverse=True)
print(listc)

#9 squares in list
llist=[1,2,3,4,5,6,7,8,9,10]"""
for x in llist:
    i=0
    i=i*x

#10 find the second largest number in a list

llist2=[11,2,33,42,5,31,98,67,0]
llist2.sort()
print(llist2)
print("second largest  in llist2 is: ",llist2[-2])

#11 count how many times the number 9 appears in a list
llist3=[1,2,1,2,1,3,4,5,6,4,4,4,7,4,8,9,0,1]
print(llist3.count(1))#4 times
print(llist3.count(2))# 2 times
print(llist3.count(4))# 5 times