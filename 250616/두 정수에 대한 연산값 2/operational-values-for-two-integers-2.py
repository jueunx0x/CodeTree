a, b = map(int, input().split())

# Please write your code here.
def cal(a,b):
    max_ = max(a,b)*2
    min_ = min(a,b)+10

    print(min(max_,min_),max(max_,min_),sep = " ")

cal(a,b)