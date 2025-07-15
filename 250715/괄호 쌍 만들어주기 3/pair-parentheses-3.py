A = input()
arr = list(A)
sum = 0
# Please write your code here.
for i in range(len(arr)):
    if(arr[i] == '(') :
        for j in range(i + 1, len(arr)):
            if(arr[j] == ')'):
                sum+=1
print(sum)