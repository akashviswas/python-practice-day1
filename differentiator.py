text = input("Enter a string: ")

letters = 0
digits = 0
others = 0

for ch in text:
    if ch.isalpha():
        letters += 1
    elif ch.isdigit():
        digits += 1
    else:
        others += 1

print("Alphabets:", letters)
print("Digits:", digits)
print("Other characters:", others)