num = 1234
print(sum(int(d) for d in str(num)))

#OR OR  
def sumDigit(n):
    total=0
    while n>0:
        total+=n%10
        n//=10
    return total
num=123456
print("Sum of digits =",sumDigit(num))