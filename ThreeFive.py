for number in range(1,101):
    if (number%3)==0 and (number%5)==0:
        print("ThreeFive")
    elif (number%3)==0:
        print("Three")
    elif (number%5)==0:
        print("Five")
    else:
        print(number)
