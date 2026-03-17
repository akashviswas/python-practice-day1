# Guess number game

store_num = 7

choose_num = int(input("Enter your number from 1 to 10 "))
if choose_num < 1 or choose_num > 10:
    print("Out of range")
elif choose_num == store_num:
    print("Correct")
elif choose_num > store_num:
    print("Too High")
else:
    print("Too Low")

