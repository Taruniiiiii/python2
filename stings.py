"""| Function                        | Description             | Example                        |
| ------------------------------- | ----------------------- | ------------------------------ |
| `len()`                         | Returns length          | `len("hello") → 5`             |
| `.upper()`                      | Convert to uppercase    | `"hi".upper() → 'HI'`          |
| `.lower()`                      | Convert to lowercase    | `"Hi".lower() → 'hi'`          |
| `.title()`                      | First letter capital    | `"hello world".title()`        |
| `.strip()`                      | Removes spaces          | `"  hi  ".strip()`             |
| `.replace(a, b)`                | Replace characters      | `"apple".replace("a", "A")`    |
| `.split()`                      | Split into list         | `"a,b,c".split(",")`           |
| `.join()`                       | Join elements           | `" ".join(["Hello", "World"])` |
| `.count()`                      | Count occurrences       | `"banana".count("a")`          |
| `.find()`                       | Find index of substring | `"python".find("t")`           |
| `.startswith()` / `.endswith()` | Check beginning/end     | `"hello".startswith("he")`     |
"""
#f string
name="Taruni"
age=19
education="MRU"
department="ds"
year=3
print(f"My name is {name} and I am {age} years old. Iam a {year}rd year student at{education}")
#way2
print("My name is {} and I am {} years old.".format(name,age))

#palindrome
pal=str(input())
lap=pal[::-1]
if pal==lap:
    print("True")
else:
    print("False")

#removing dups from string
dup=str(input())
no_dup=""
for i in dup:
    if i not in no_dup:
        no_dup+=i
print(no_dup)