n = int(input("Enter to test weird or not weird: "))
if n % 2 == 1:
    print("Weird")
elif n % 2 == 0 and n in range(6, 21):
    print("Weird")
else:
    print("Not Weird")