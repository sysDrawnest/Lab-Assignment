s = "hello world"
count = sum(1 for ch in s if ch.lower() in 'aeiou')
print("Vowel count:", count)

#number of vowels in a string
def vowels_count(s):
    count=0
    for i in s:
        if i in "aeiouAEIOU":
            count=count+1
    return count

s=input("Enter string")
print(vowels_count(s))