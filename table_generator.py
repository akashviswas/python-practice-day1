# Generating a table with the input validation method

number = input("Enter the number for creating a table :> ")

# Empty check
if number.strip() == "":
    print("Empty input")

# Number check
elif not number.isdigit():
    print("Invalid input")

else:
    number = int(number)
 
    if number == 0:
        print("Special message")
    else:
        for i in range(1, 11):
            print(f"{number} * {i} = {number * i}")
   
    


    
        
    
 