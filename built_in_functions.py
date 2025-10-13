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
result=all(n<10 for n in num)
print(result)#false coz of 0
