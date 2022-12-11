
# Importing date and time module to our program

from datetime import date as date_n

# Creating function to return difference

def number_of_days(date_1, date_2):
    return (date_2 - date_1).days

# Driver program

birth_date = int(input("Enter birth date: "))
birth_month = int(input("Enter birth month: "))
birth_year = int(input("Enter birth year: "))
date_1 = date_n(birth_year, birth_month, birth_date)
current_date = int(input("Current date: "))
current_month = int(input("Enter current month: "))
current_year = int(input("Enter current year: "))
date_2 = date_n(current_year, current_month, current_date)

# Printing the no. of days

print("\n\n\n\n\n\t\t\t\tNumber of Days between the given Dates are: ", number_of_days(date_1, date_2),
      "days\n\n\n\n\n\n")