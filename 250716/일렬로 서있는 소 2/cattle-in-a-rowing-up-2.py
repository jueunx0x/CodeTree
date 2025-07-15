N = int(input())
A = list(map(int, input().split()))
curnum = 0 
curheight = 0 

count = 0 
N_A_Match = []
# Please write your code here.
for i in range(N):
    N_A_Match.append((i,A[i]))

for x,y in N_A_Match:
    if x > curnum and y > curheight:
        curnum = x
        curheight = y
        count+=1
print(count-1)