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