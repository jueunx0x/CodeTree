N = int(input())

# Please write your code here.
def pivo(N):
    if N == 1:
        return 1
    if N == 2:
        return 1
    return pivo(N-1)+pivo(N-2)

print(pivo(N))