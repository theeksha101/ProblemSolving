x = int(input("Please enter a number: "))
if x < 0:
    x = 0
    print("Value has been changed to zero. Please enter again: ")
    x = int(input("Please enter a number: "))
if x == 0:
    print("You entered Zero")

elif x <= 20:
    print("Your value is too small")

elif x >= 21 & x <= 50:
    print("Your value is too big")

else:
    print("Out of range")
