binary = input()

# Please write your code here.

bin_arr = []
num = 0
which = 0

for i in binary:
    bin_arr.append(i)

total_len = len(bin_arr)-1
for i in range (len(bin_arr)-1,-1,-1):
    
    num+= int(bin_arr[i]) * (2 ** (total_len-i))

print(num)
