# 1. Prime check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

# 2. Area of rectangle
def area_rectangle(length, width):
    return length * width

# 3. Maximum of three numbers
def max_of_three(a, b, c):
    return max(a, b, c)

# 4. Reverse a string
def reverse_string(s):
    return s[::-1]

# 5. Count vowels
def count_vowels(s):
    return sum(1 for ch in s.lower() if ch in 'aeiou')

# 6. Check palindrome
def is_palindrome(s):
    return s == s[::-1]

# 7. Sum of list
def sum_list(lst):
    return sum(lst)

# 8. Fibonacci sequence
def fibonacci(n):
    seq = []
    a, b = 0, 1
    for _ in range(n):
        seq.append(a)
        a, b = b, a + b
    return seq

# 9. Celsius to Fahrenheit
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

# 10. Minimum value in list
def min_in_list(lst):
    return min(lst)

# 11. Count character occurrences
def count_char(s, ch):
    return s.count(ch)

# 12. Check perfect number
def is_perfect(n):
    return sum(i for i in range(1, n) if n % i == 0) == n

# 13. Sum of digits
def sum_digits(n):
    return sum(int(d) for d in str(n))

# 14. Character frequency dictionary
def char_freq(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# 15. Average of list
def average(lst):
    return sum(lst) / len(lst)

# 16. Multiplication table
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n*i}")

# 17. Reverse list
def reverse_list(lst):
    return lst[::-1]

# 18. Second largest number
def second_largest(lst):
    unique = list(set(lst))
    unique.sort()
    return unique[-2] if len(unique) >= 2 else None

# 19. Filter even numbers
def even_numbers(lst):
    return [x for x in lst if x % 2 == 0]

# 20. Unique characters check
def are_chars_unique(s):
    return len(set(s)) == len(s)

# 21. GCD
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# 22. LCM
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 23. Remove duplicates
def remove_duplicates(lst):
    return list(set(lst))

# 24. Recursive factorial
def factorial(n):
    return 1 if n == 0 else n * factorial(n - 1)

# 25. Armstrong number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)

# 26. Prime numbers up to n
def primes_up_to_n(n):
    return [x for x in range(2, n+1) if is_prime(x)]

# 27. Longest word
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 28. Recursive power
def power(base, exp):
    if exp == 0:
        return 1
    return base * power(base, exp - 1)

# 29. Flatten nested list
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# 30. Check if list is sorted
def is_sorted(lst):
    return lst == sorted(lst)

# 31. Merge sorted lists
def merge_sorted(l1, l2):
    return sorted(l1 + l2)

# 32. Most frequent element
def most_frequent(lst):
    return max(set(lst), key=lst.count)

# 33. Median of list
def median(lst):
    lst = sorted(lst)
    n = len(lst)
    mid = n // 2
    return (lst[mid] if n % 2 != 0 else (lst[mid-1] + lst[mid]) / 2)

# 34. Intersection of two lists
def list_intersection(l1, l2):
    return list(set(l1) & set(l2))

# 35. Product of variable arguments
def product(*args):
    result = 1
    for num in args:
        result *= num
    return result

# 36. List of tuples (element, index)
def element_index(lst):
    return [(element, index) for index, element in enumerate(lst)]

# 37. Word count dictionary
def word_count(s):
    words = s.split()
    return {word: words.count(word) for word in set(words)}

# 38. Check pangram
def is_pangram(s):
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(s.lower()))

# 39. Index of value in list
def find_index(lst, value):
    return lst.index(value) if value in lst else -1

# 40. Count upper and lower case
def count_case(s):
    upper = sum(1 for c in s if c.isupper())
    lower = sum(1 for c in s if c.islower())
    return {'uppercase': upper, 'lowercase': lower}
