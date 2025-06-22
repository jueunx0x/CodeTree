a, b = map(int, input().split())
N = list(map(int, list(input())))

num = 0
digits = []
for i in range(len(N)):
    num = num * a + N[i]


while True:
    if num < b:
        digits.append(num)
        break
    digits.append(num%b)
    num //= b

for i in digits[::-1]:
    print(i,end = "")

