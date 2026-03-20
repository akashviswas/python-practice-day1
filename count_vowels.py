# Count Vowels ...

words = input("Enter the words, do you want to know the present vowels in it ")

vowels = "aeiouAEIOU"

count = 0
for char in words:
    if char in vowels:
        count = count +1

print("Total vowels:",count)