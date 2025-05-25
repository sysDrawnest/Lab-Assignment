# 1. Print numbers from 1 to 10.
for i in range(1, 11):
    print(i)

# 2. Print even numbers from 1 to 20.
for i in range(2, 21, 2):
    print(i)

# 3. Check if a number is positive, negative or zero.
num = int(input("Enter a number: "))
if num > 0:
    print("Positive")
elif num < 0:
    print("Negative")
else:
    print("Zero")

# 4. Add two numbers using operators.
a, b = 5, 7
print("Sum:", a + b)

# 5. Print multiplication table of a number.
num = int(input("Enter a number: "))
for i in range(1, 11):
    print(f"{num} x {i} = {num*i}")

# 6. Find the largest among two numbers.
a, b = 10, 20
print("Largest:", max(a, b))

# 7. Use a while loop to print numbers 5 to 1.
i = 5
while i > 0:
    print(i)
    i -= 1

# 8. Print all characters in a string.
s = "Hello"
for char in s:
    print(char)

# 9. Use logical operator to check if a number is between 10 and 50.
num = 25
print(10 < num < 50)

# 10. Sum of first 10 natural numbers.
print(sum(range(1, 11)))

# 11. Print "Odd" or "Even" for numbers 1 to 10.
for i in range(1, 11):
    print(i, "Even" if i % 2 == 0 else "Odd")

# 12. Use “break” to stop loop when number is 5.
for i in range(1, 11):
    if i == 5:
        break
    print(i)

# 13. Print 1 to 10 and use continue to skip printing 5.
for i in range(1, 11):
    if i == 5:
        continue
    print(i)

# 14. Print all elements in a list using a loop.
lst = [1, 2, 3, 4, 5]
for item in lst:
    print(item)

# 15. Check if a number is divisible by both 3 and 5.
num = 15
print(num % 3 == 0 and num % 5 == 0)

# 16. Square of all numbers from 1 to 5.
for i in range(1, 6):
    print(i**2)

# 17. Print ASCII values of characters in a string.
for ch in "ABC":
    print(f"{ch} = {ord(ch)}")

# 18. Count down from 10 to 1 using while.
i = 10
while i >= 1:
    print(i)
    i -= 1

# 19. Check if a number is divisible by 2 or 3.
num = 6
print(num % 2 == 0 or num % 3 == 0)

# 20. Print sum of digits of a number.
num = 1234
print(sum(int(d) for d in str(num)))

# 21. Swap two numbers using a temporary variable.
a, b = 1, 2
temp = a
a = b
b = temp
print(a, b)

# 22. Print numbers from 1 to 100 that are divisible by 7.
for i in range(1, 101):
    if i % 7 == 0:
        print(i)

# 23. Find the factorial of a number.
num = 5
fact = 1
for i in range(1, num + 1):
    fact *= i
print("Factorial:", fact)

# 24. Count vowels in a string.
s = "hello world"
count = sum(1 for ch in s if ch.lower() in 'aeiou')
print("Vowel count:", count)

# 25. Reverse a number using loop.
num = 1234
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print("Reversed number:", rev)

# 26. Find the maximum in a list using loop.
lst = [10, 45, 2, 99]
max_val = lst[0]
for num in lst:
    if num > max_val:
        max_val = num
print("Max:", max_val)

# 27. Prime number check using loop.
num = 7
is_prime = True
for i in range(2, int(num**0.5)+1):
    if num % i == 0:
        is_prime = False
        break
print("Prime" if is_prime and num > 1 else "Not Prime")

# 28. Sum of even numbers in a list.
lst = [1, 2, 3, 4, 5, 6]
print("Sum of even numbers:", sum(num for num in lst if num % 2 == 0))

# 29. Print number pattern using nested loops.
for i in range(1, 6):
    for j in range(1, i+1):
        print(j, end=" ")
    print()

# 30. Count frequency of digits in a number.
num = 112233
freq = {}
for d in str(num):
    freq[d] = freq.get(d, 0) + 1
print(freq)

# 31. GCD of two numbers using loop.
a, b = 60, 48
while b:
    a, b = b, a % b
print("GCD:", a)

# 32. Check if a number is a palindrome.
num = 121
print("Palindrome" if str(num) == str(num)[::-1] else "Not Palindrome")

# 33. Count words in a sentence.
s = "Hello world, this is Python"
print("Word count:", len(s.split()))

# 34. Find common elements in two lists.
lst1 = [1, 2, 3, 4]
lst2 = [3, 4, 5, 6]
print("Common:", list(set(lst1) & set(lst2)))

# 35. Use elif to grade students based on score.
score = 85
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Fail")

# 36. Print a right-angled triangle using *.
for i in range(1, 6):
    print("*" * i)

# 37. Check if a year is a leap year.
year = 2024
is_leap = (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
print("Leap Year" if is_leap else "Not Leap Year")

# 38. Print Fibonacci series using loop.
n = 10
a, b = 0, 1
for _ in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# 39. Count uppercase and lowercase letters in a string.
s = "Hello World"
upper = sum(1 for c in s if c.isupper())
lower = sum(1 for c in s if c.islower())
print("Uppercase:", upper, "Lowercase:", lower)

# 40. Print numbers from 100 to 1 using loop.
for i in range(100, 0, -1):
    print(i)
