n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
nums.sort()
answer = 0

for i in range(n):
    pair_sum = nums[i]+nums[-(i+1)]
    answer = max(answer,pair_sum)
print(answer)