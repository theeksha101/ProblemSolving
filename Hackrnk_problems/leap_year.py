def Leap(myyear):
    leap = False
    if myyear % 4 != 0 and myyear % 100 == 0 or myyear % 400 != 0:
        return False
    else:
        return True


year = int(input("Enter: "))
print(Leap(year))
