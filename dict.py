#Python dictionary is a data structure that stores the value in key: value pairs.
#ex
d1={1:'ish',2:'soh',3:'tar'}
print(d1)

# create dictionary using dict() constructor
d2=dict(a="tan",b="adh",c="sah")
print(d2)

#We can access a value from a dictionary by using the key within square brackets or get() method.
d = {"name":"Taruni",1:"Python",(1,2):[1,2,4]}

# Access using key
print(d[(1,2)])

# Access using get()
print(d.get("name"))

# Adding a new key-value pair in the end
d1["age"] = 22
print(d1)
# Updating an existing value
d1[1] = "man"
print(d1)

"""del: Removes an item by key.
pop(): Removes an item by key and returns its value.
clear(): Empties the dictionary.
popitem(): Removes and returns the last key-value pair.
"""
# Using del to remove an item
del d1["age"]
print(d1)

# Using pop() to remove an item and return the value
value=d1.pop(1)
print(value)

# Using popitem to removes and returns
# the last key-value pair
key,val=d.popitem()
print(f"Key:{key},Value:{val}")

# Clear all items from the dictionary
d2.clear()
print(d2)
d = {1:'MRU',2:'MRCET','CMR':2025}

# Iterate over keys
for key in d:
    print(key)#print just keys like here..1,2,cmr

# Iterate over values
for value in d.values():
    print(value)#prints values liike  mru,mrcet,2025

# Iterate over key-value pairs
for key, value in d.items():#prints keys and values both
    print(f"{key}: {value}")

#nested dictionary
di= {1:'iam',2:'taruni',3:{'A':'datascience','B':'delta','C':'336'}}
print(di)

names = ["john","ala","ilia","sudan","mercy"]
marks = ["100","200","150","80","300"]
def create_dict(arr):
    dict = {}
    for key,values in arr:
        dict[key]=values
    return dict

result=create_dict(zip(names,marks))#combines names and values in arr
print(result)

#1: Count Word Frequency
word="I love python because python is easy"
freq={}
sentence=word.split()#spliting the sentence
for word in sentence:
    if word in freq:
        freq[word]+=1 #if the aprticular word exists in freq word freq is increased by +1
    else:
        freq[word]=1 #else freq=1
print(word,freq)#prints word and he no of times it is repeated
#otp: {'I': 1, 'love': 1, 'python': 2, 'because': 1, 'is': 1, 'easy': 1}

#2: Merge Two Dictionaries
di1 = {'a':1, 'b':2}
di2 = {'b':3, 'c':4}
for key,value in di2.items():#items=key,value pairs
        di1[key]=value
print(di1)
#output:{'a': 1, 'b': 3, 'c': 4}
#or
#di1.update(di2)

#3: Find Student with Maximum Marks
res= {'John': 80, 'Tina': 92, 'Alex': 89}
max_marks = -1
top_student = ""
for student,mark in res.items():
    if mark>max_marks:
        max_marks=mark #updates marks
        top_student=student #updates student name accordingly
print(top_student,max_marks)
#otp:Tina 92

#Count Occurrences
nums=[1, 2, 2, 3, 1, 4, 2]
dicti={}
for n in nums:
    if n in dicti:
        dicti[n]+=1
    else:
        dicti[n]=1
print(dicti)
#otp:{1: 2, 2: 3, 3: 1, 4: 1}

#Filter Dictionary by Value
ex1={'a': 5, 'b': 10, 'c': 2, 'd': 8}
dictii={}
for key,value in ex1.items():
    if value>5:
        dictii[key]=value
print(dictii)
#otp:{'b': 10, 'd': 8}

#Swap Keys and Values
ex3={'a': 1, 'b': 2, 'c': 3}
dictiii={}
for key,value in ex3.items():
    dictiii[value]=key
print(dictiii)
#otp: {1: 'a', 2: 'b', 3: 'c'}

#Find the Key with Maximum Value
ex4={'apple': 10, 'banana': 25, 'grapes': 15}
maxx=-1
max_v=""
for k,v in ex4.items():
    if v>maxx:
        max_v=k
        maxx=v
print(max_v)
#otp:banana

dict1 = {'a': 10, 'b': 20, 'c': 30}
dict2 = {'a': 40, 'b': 50, 'd': 60}
o={}
for k,v in dict1.items():
    if k in dict1 and dict2:
        o[k]=v
for k,v in dict2.items():
    if k in o:
        o[k] += v   # if key already exists add values
    else:
        o[k] = v
print(o)

#Create Dictionary from Two Lists
names=['a', 'b', 'c']
values=[10, 20, 30]
m_dict=dict(zip(names,values))
print(m_dict)

#count word frequency
paragraph = "Apple banana apple orange banana apple"
new_p=paragraph.lower().split()
p={}
for word in new_p:
    if word in p:
        p[word]+=1
    else:
        p[word]=1
print(p)
#otp: {'apple': 3, 'banana': 2, 'orange': 1}

#Find All Pairs of Keys Whose Values Sum to a Target
prices = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
prices = {'a': 10, 'b': 20, 'c': 30, 'd': 40}
target = 50

keys = list(prices.keys())
values = list(prices.values())

for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] + values[j] == target:
            print(f"{keys[i]} and {keys[j]} add up to {target}")

#word length mapping
wordss = ["python", "is", "cool"]
w_l={}
for w in wordss:
    w_l[w]=len(w)
print(w_l)