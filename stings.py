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

#vowels and constraints
vowels=["a","e","i","o","u","A","E","I","O","U"]
word=str(input())
vowels_count=0
consonant_count=0
for i in word:
    if i in vowels:
        vowels_count+=1
    elif i.isalpha():#is alhabet if i use i is not in vowels it includes everything
        consonant_count+=1
    else:
        print("invalid char")
print(vowels_count,"vowels count")
print(consonant_count,"consonant count")

#reverse sentence 
sentence="hi im taruni"
word=sentence.split()#breaks the sentence into words
reversed_word=[w[::-1] for w in word]
print(" ".join(reversed_word))

#Find the longest word in a sentence.
sen="hi im taruni and"
wor=sen.split()
long=""
for w in wor:
    if len(w)>len(long):#compares word with another
        long=w #if true long is changed
print(long,len(long))

#Remove all punctuation marks from a sentence.
sent="He said, 'I can't believe it!'; and then he ran away—but where did he go?!"
li= [",", "@", "$", "%", "^", "&", "*", "(", ")", ".", ";", ":", "'", '"', "[", "]", "{", "}", "?", "-", "_", "!"]
clear=""
for ch in sent:
    if ch not in li:
        clear+=ch
print(clear)

#Count Uppercase, Lowercase, Digits, and Special Characters
s=str(input())
upper=0
lower=0
digit=0
special=0
for ch in s:
    if ch.isupper():
        upper+=1
    elif ch.islower():
        lower+=1
    elif ch.isdigit():
        digit+=1
    else:
        special+=1
print(upper,"upper")
print(lower,"lower")
print(digit,"digit")
print(special,"special")

#Reverse the Order of Words (Keep Letters in Order)
sentence="hi im taruni"
word=sentence.split()#breaks the sentence into words
rev_word=word[::-1]
print(rev_word)
"""
#Word Frequency Counter
p="hi im taruni im learning python python is fun"
words=p.split()
dicti={}
for word in words:
    if word in dicti:
        dicti[word]+=1
    else:
        dicti[word]=1
print(dicti)
#otp:{'hi': 1, 'im': 2, 'taruni': 1, 'learning': 1, 'python': 2, 'is': 1, 'fun': 1}




