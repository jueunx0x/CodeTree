n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
a = max(nums)
b = min(nums)

nums.remove(b)
nums.remove(a)
c = min(nums)
d = max(nums)
if a+b < c+d :
    print(c+d)
else : print(a+b)