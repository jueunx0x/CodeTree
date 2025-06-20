n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Please write your code here.

sorted_str = sorted([word for word in str if word.startswith('ap')])

print(sorted_str[k-1])