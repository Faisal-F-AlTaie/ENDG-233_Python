year = int(input("Please input a year to check if it is a leap year:\n"))

if year % 4 == 0:
    if year % 100 != 0:
        print(year, "is a leap year")
    else:
        if year % 400 == 0:
            print(year, "is a leap year")
        else:
            print(year, "is not a leap year") 
else:
    print(year, "is not a leap year")