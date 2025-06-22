N, B = map(int, input().split())

# Please write your code here.

digits = []
while True:
    if N < 4:
        digits.append(N)
        break
    
    digits.append(N%4)
    N//=4

for i in digits[::-1]:
    print(i,end="")
