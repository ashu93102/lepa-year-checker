#leap year Checker
print("Welcome to leap year checker wizard!")
year = int(input("Enter year that you want to check.\n"))
month = int(input("Which month days do you wanna know enter the month number\n")) % 12

#leap check condition
def is_leap(year):
    if year % 4 != 0:
        return False
        print("Not leap year")
    elif year % 100 != 0:
        return True
        print("Leap year")
    elif year % 400 != 0:
        return False
        print("Not leap year")
    else:
        return True
        print("Leap year")

leap_year = is_leap(year)


def days_in_month(actual_year, actual_month):
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year == False:
        return month_days[actual_month - 1]
    elif leap_year == True and actual_month == 2:
        leap_month = month_days[actual_month - 1]
        actual_month_days = leap_month + 1
        return actual_month_days
    else:
        return month_days[actual_month - 1]



days = days_in_month(year, month)
print(days)
