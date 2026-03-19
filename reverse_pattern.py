

rows = int(input("Enter The number how many line you want to see as a reverse pattern"))

for i in range (rows,0,-1):
    for j in range(i):
        print("*",end=" ")
    print()