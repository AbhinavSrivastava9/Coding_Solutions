n = int(input("Enter any year of your choice \n"))

if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
    print("The year is leap year")
else:
    print("Year is not a leap year")

    


