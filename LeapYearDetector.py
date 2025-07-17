def is_leap_year(year):
# Write your code here.
    year = int(input("Enter the Year?: \n"))
    if year % 4 == 0: # divisible by 4
        if year % 100 == 0: # divisible by 100
            if year % 400 == 0: # divisible by 400
                print(f" {year} is leap year")
                # return True
            else:
                print(f"{year} not a leap year")
                # return False
        print(f" {year} is leap year")
        # return True
    else:
        # return False
        print(f"{year} not a leap year")

is_leap_year(2001)