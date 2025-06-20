n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

sorted_str = sorted(str)
print(sorted_str[k])