#leap year Checker
print("Welcome to leap year checker wizard!")
year = int(input("Enter year that you want to check.\n"))


#leap check condition
if year % 4 != 0:
    print("Not leap year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Not leap year")
else:
    print("Leap year")