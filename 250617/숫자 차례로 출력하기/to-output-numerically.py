n = int(input())

# Please write your code here.
def printSeq(n):
    if n == 0 :
        return
    
    printSeq(n-1)
    print(n,end=" ")

def printSeq2(n):
    if n == 0 :
        return

    print(n,end=" ")
    printSeq2(n-1)
printSeq(n)
print()
printSeq2(n)