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
"""
# Adding a new key-value pair in the end
d1["age"] = 22
print(d1)
# Updating an existing value
d1[1] = "man"
print(d1)
"""
del: Removes an item by key.
pop(): Removes an item by key and returns its value.
clear(): Empties the dictionary.
popitem(): Removes and returns the last key-value pair."""

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