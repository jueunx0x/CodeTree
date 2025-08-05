a = input()
length = len(a)
str_a = []
int_a = []
sum = 0
temp = ''
# Please write your code here.
for i in a:
    str_a.append(i)
for j in range(len(a)):
    temp = str_a[j]
    if(str_a[j] == '0'):
        str_a[j] = '1'
    else : str_a[j] = '0'
    for i in range(len(a)):
        sum += int(str_a[i]) * 2 ** (length-i-1)
    str_a[j] = temp
    int_a.append(sum)
    sum = 0

print(max(int_a))