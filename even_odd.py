# Writing a code for even and odd number finding...

num = int(input("Enter your number:>"))

if num == 0:
    print ("The Number is zero,(0) :>")
elif num < 0:
    print("Negative number")
    
else:
     if num % 2 == 0:
        print ("Even Number :>")
     else:
         print ("Number is odd :>")

