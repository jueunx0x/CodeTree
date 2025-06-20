word1 = input()
word2 = input()

# Please write your code here.
arr1 = list(word1)
arr2 = list(word2)
arr1.sort()
arr2.sort()

sorted_arr1 = ''.join(arr1)
sorted_arr2 = ''.join(arr2)

if(sorted_arr1 == sorted_arr2):
    print("Yes")
else : print("No")