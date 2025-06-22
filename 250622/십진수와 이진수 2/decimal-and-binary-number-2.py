N = list(map(int, list(input())))
# Please write your code here.

num = 0
for i in range(len(N)):
    num = num * 2 + N[i]

num = num*17

digits = []
while True:
    if num < 2:
        digits.append(num)
        break
    digits.append(num%2)
    num//=2

for i in digits[::-1]:
    print(i,end="")