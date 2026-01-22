#string palindrome
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
n=int(input())"""
for i in range(2, n):
    if n % i == 0:
        print("not prime")
        break
else:
    print("prime")