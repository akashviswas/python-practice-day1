rows = int(input("Enter The number how many line you want to see as a pattern"))

for i in range (1,rows+1):
    for j in range(i):
        print("*",end=" ")
    print()