a, b = 60, 48
while b:
    a, b = b, a % b
print("GCD:", a)

#OR OR OR 

import math
num1=60
num2=48
print("GCD=",math.gcd(num1,num2))