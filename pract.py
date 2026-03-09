"""#string palindrome
def is_palindrome(s):
  reverse=""
  for ch in s:
    reverse=ch+reverse
  if s==reverse:
    print("palindrome")
  else:
    print("not palindrome")
  
text="madam"
print(is_palindrome(text))

n=int(input())
fact=1
for i in range(1,n+1):#takes values from 1 to n+1
  fact=fact*i#  1*1,1*2,2*3,6*4,24*5
print(fact)

#prime or not
n=int(input())
for i in range(2, n):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")
    
data = input()
##
if data.isdigit():
    print("Numeric")
else:
    print("Not numeric")
##
logs = ["error", "info", "error", "warning", "error"]
count = 0

for log in logs:
    if log == "error":
        count += 1

print("Error count:", count)
##
amount = float(input("Enter amount: "))

if amount > 5000:
    discount = amount * 0.1
else:
    discount = 0

print("Final bill:", amount - discount)
##
print("\n2. Which keyword is used to define a function in Python?")
print("a) def\nb) function\nc) fun\nd) define")
ans = input("Your answer: ")
if ans.lower()=="a":
    score+=1

##
n = int(input())
temp = n
order = len(str(n))
sum = 0

while temp > 0:
    digit = temp % 10
    sum += digit ** order
    temp //= 10

print("Armstrong" if sum == n else "Not Armstrong")

##28 duplicates
sen=input("enter a sentence").split()
unique=[]
for w in sen:
  if w not in unique:
      unique.append(w)
print(" ".join(unique))

##
ex="aabbbc"
freq={}
for ch in ex:
    if ch in freq:
        freq[ch]+=1
    else:
        freq[ch]=1
print(freq)

##
y=[0,1,0,3,12]
res=[]
z_count=0
for n in y:
    if n==0:
        z_count+=1
    else:
        res.append(n)
res.extend([0]*z_count)#extend() means  add all ele of another list 1 by 1 to the list
print(res)

##
class Solution(object):
    def groupAnagrams(self, strs):
        group={}
        for word in strs:
            keys="".join(sorted(word))
            if keys not in group:
                group[keys]=[]
            group[keys].append(word)
        return list(group.values())

#29
class Solution(object):
    def majorityElement(self, nums):
        count=0
        cand=None
        for n in nums:
            if count == 0:
                cand = n
            if n==cand:
                count+=1
            else:
                count-=1
        return cand
    
##let
class Solution(object):
    def findTheDifference(self, s, t):
        res=0
        for ch in s:
            res^=ord(ch) #^ xor operator which gives all -ve asn
        for ch in t:
            res^=ord(ch)
        return chr(res) #num to letter conversion(chr)
    
##
class Solution(object):
    def toLowerCase(self, s):
        return s.lower()


        
##
class Solution(object):
    def isAnagram(self, s, t):
        return sorted(s)==sorted(t)
        
##
class Solution(object):
    def sortedSquares(self, nums):
        n=len(nums)
        res = [0] * n
        left,right=0,n-1
        pos=n-1
        while left<=right:
            if nums[left]*nums[left]>nums[right]*nums[right]:
                res[pos]=nums[left]*nums[left]
                left+=1
            else:
                res[pos]=nums[right]*nums[right]
                right-=1
            pos-=1
        return res
##31 jan
class Solution(object):
    def detectCapitalUse(self, word):
        if word.isupper() or word.islower() or word.istitle():
            return True
        else:
            return False
        
##
class Solution(object):
    def fizzBuzz(self, n):
        res=[]
        for i in range(1,n+1):
            
            if i%3==0 and i%5==0:
                res.append("FizzBuzz")
            elif i%3==0:
                res.append("Fizz")
            elif i%5==0:
                res.append("Buzz")
            else:
                res.append(str(i))
        return res
    
##1 feb
class Solution:
    def capitalizeTitle(self, title: str) -> str:
        word=title.split()
        res=[]
        for w in word:
            if len(w)<=2:
                res.append(w.lower())
            else:
                res.append(w[0].upper()+ w[1:].lower()) 
        return " ".join(res)

##
class Solution:
    def triangleType(self, nums: List[int]) -> str:
        a,b,c=nums[0],nums[1],nums[2]
        if a==b==c:
            return "equilateral"
        elif (a==b or b==c or c==a)and a+b>c and b+c>a and c+a>b :
            return "isosceles"
        elif a+b>c and b+c>a and c+a>b:
            return "scalene"
        else:
            return "none"

#5 feb
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        pos = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[pos], nums[i] = nums[i], nums[pos]
                pos += 1
##6 feb
class Solution:
    def canWinNim(self, n: int) -> bool:
        if n%4==0:
            return False
        else:
            return True
##7 feb
class Solution:
    def countSegments(self, s: str) -> int:
        count=0
        s=s.split()
        for word in s:
            count+=1
        return counts

#gfg
class Solution:
    def minTime (self, arr, k):
        low=max(arr)
        high=sum(arr)
        
        while low<high:
            mid=(low+high)//2
            
            painters=1
            work=0
            for board in arr:
                if work+board<=mid:
                    work+=board
                else:
                    painters+=1
                    work=board
            if painters<=k:
                high=mid
            else:
                low=mid+1
        return low
#gfg
class Solution:
    def canAttend(self, arr):
        arr.sort()#sorting arr
        for i in range(1,len(arr)):
            if arr[i][0]<arr[i-1][1]:#condition applied
                return False
        return True
            
        
##leet
class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        s=list(s)
        left,right=0,len(s)-1
        while left<right:
            if not s[left].isalpha():
                left+=1
            elif not s[right].isalpha():
                right-=1
            else:
                s[left],s[right]=s[right],s[left]
                left+=1
                right-=1
        return ''.join(s)
##
class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result=int(num1)*int(num2)
        return str(result)
    
    class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        num = set(nums)
        s = []
        for i in range(1,len(nums)+1):
            if i not in num:
                s.append(i)

        return s
#
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            age=int(i[11:13]) 
            if age>60:
                count+=1
        return count
        
#
class Solution:
    def removeStars(self, s: str) -> str:
        stack=[]
        for c in s:
            if c=="*":
                stack.pop()#If character is *, pop from stack.
            else:
                stack.append(c)#If character is not *, push it.
        return "".join(stack)

## debugging session
Python Debugging Hackathon Sheet
Identify the bug(s), fix the code, and explain the issue.
Instructions:
1. Each problem contains buggy Python code.
2. Your task: (a) Identify the bug, (b) Fix the code, (c) Explain the issue.
3. Time limit: 60–90 minutes.
4. You may use paper or an editor, but avoid running the code initially.

#1. Missing Colon"""

from binascii import Error
from tokenize import String

from pandas import Index


def greet(name):
 print("Hello " + name)
greet("Santosh")
#2. Indentation Error
for i in range(5):
    print(i)
#3. Undefined Variable
x = 10
y = 11
z=x+y
print(z)
#
# 4. Type Error
age = 21
print("Age is " +  str(age))

#5. Infinite Loop
i = 1
while i < 5:
    print(i)
    
#6. Index Error
numbers = [10,20,30]
print(numbers[1])

#7. Function Not Returning
def add(a,b):
    result = a + b
print(add(3,4))

#8. Dictionary Key Error
student = {"name":"Santosh","age":22}
print(student["name"])

#9. Tuple Modification
t = (1,2,3)
lst = list(t)
lst[0] = 10
t = tuple(lst)

print(t)

#10. Division by Zero
a = 10
b = 0
print(a/b)
#11. Wrong Condition
num = 10
if num == 10:
 print("Ten")
 
#12. Wrong List Append
numbers = [1,2,3]
numbers.append(4)
print(numbers)

#13. Wrong Function Call
def square(x):
 return x*x
print(square(5))

#14. Wrong Boolean
flag = True
print(flag)

#5. Wrong Input Handling
num = int(input("Enter number: "))
print(num + 5)

#16. Wrong Loop Syntax
numbers = [1,2,3]
for i in numbers:
    print(i)
    
#17. String Index Error
name = "Python"
print(name[10])

#18. List Removal Bug
nums = [1,2,3,4,5]
for n in nums:
    if n % 2 == 0:
        nums.remove(n)
print(nums)
19. Wrong Class Definition
class Person
 def __init__(self,name):
 self.name = name
20. Recursion Bug
def fact(n):
 if n == 0:
 return 0
 return n * fact(n-1)
print(fact(5))