n = int(input())

# Please write your code here.

def printStar(n):
    if n == 0:
        return 
    print("* " * n)
    printStar(n-1)
    print("* " * n)

printStar(n)