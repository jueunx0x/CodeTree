n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.
def print_sort(nums):
    for i in nums:
        print(i , end =" ")

nums.sort()
print_sort(nums)
nums.sort(reverse = True)
print()
print_sort(nums)

