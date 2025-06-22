n = int(input())

# Please write your code here.

def digits(n):
    digits_arr = []

    while True:
        if n < 2 :
            digits_arr.append(n)
            break
        
        digits_arr.append(n%2)
        n //= 2

    return digits_arr


digit = digits(n)
for i in digit[::-1]: #거꾸로 출력
    print(i,end="")