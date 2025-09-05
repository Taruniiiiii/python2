#two sum
nums=[1,2,3,4,5,6]
target=int(input())
n=len(nums)
for i in range(n):
       for j in range(i+1,n):
              if nums[i]+nums[j]==target:
                   print([i,j])
             