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
<<<<<<< HEAD
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
"""
##28 duplicates
sen=input("enter a sentence").split()
unique=[]
for w in sen:
  if w not in unique:
      unique.append(w)
print(" ".join(unique))
=======
    print("prime")"""
>>>>>>> e630764212dc4b10163c4462d8378c9fc27aea8c
