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
