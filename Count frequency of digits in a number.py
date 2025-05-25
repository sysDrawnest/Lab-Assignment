num=11222555
frequency={}
for digits in str(num):
    frequency[digits]=frequency.get(digits,0)+1
print(frequency)