def leap(year):
    if year % 4 == 0 and year % 100 != 0:
        #print(f"{year} przestępny.")
        return True
    elif year % 400 == 0 and year % 100 == 0:
        #print(f"{year} przestepny.")
        return True
    else:
        #print(f"{year} Crok nieprzestepny.")
        return False


def days_in_month(year, month):
    if month > 12 or month < 1:
        return "Invalid month!"
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap(year) and month == 2:
        return 29
    return month_days[month - 1]


year = int(input("Enter a year: "))
month = int(input("Enter a month: "))
days = days_in_month(year, month)
print(days)