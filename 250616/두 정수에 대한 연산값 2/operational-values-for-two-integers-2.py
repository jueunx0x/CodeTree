a, b = map(int, input().split())

# Please write your code here.
def cal(a,b):
    if max(a,b) == a :
        a = a * 2
        b = a + 10
    else:
        a = a + 10
        b = b * 2

    print(a,b,sep = " ")

cal(a,b)