line = input("Enter the string: ")

reverse = ""   

for ch in line:
    reverse = ch + reverse   

print("Reversed string:", reverse)