for i in range(1,101):
    if (i % 3 == 0 and i % 5 == 0): #any clustered conditions should be the first one
        print("ENDG233")
    elif (i % 3 == 0):
        print("ENDG")
    elif (i % 5 == 0):
        print("233")
    else:
        print(i)