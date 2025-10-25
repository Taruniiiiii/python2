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

#2: Merge Two Dictionaries
di1 = {'a':1, 'b':2}
di2 = {'b':3, 'c':4}
for key,value in di2.items():#items=key,value pairs
        di1[key]=value
print(di1)
#or
#di1.update(di2)

#3: Find Student with Maximum Marks
res= {'John': 80, 'Tina': 92, 'Alex': 89}
max_marks = -1
top_student = ""
for student,mark in res.items():
    if mark>max_marks:
        max_marks=mark
        top_student=student
print(top_student,max_marks)