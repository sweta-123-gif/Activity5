# Name: Sweta kc
# ISQ(3900) Web Application Development
# The purpose of this program is to create a csv file and work with reading and writing it. 
import csv
import os

# display a title
print("The Miles Per Gallon program")
print()
with open('trips.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["miles", "gallon", "mpg"])

# get the read trips data
scores = input("Would you like to read from a file?(y/n):")
if scores == 'y':

    trips_csv = input("Enter the csv filename containing trip data:")
    if os.path.exists(trips_csv):
        print("Trips: ")
        with open("trips.csv") as file:
            reader = csv.reader(file)

            for row in reader:
                print("   ".join(row))

    else:

        print('Trips not read from file - file not found:', trips_csv)


else:
    print("Bye!")

row_list = []

data_list = []
flag = True
while flag:
    try:

        # get input from the user
        miles_driven = float(input("Enter miles driven:\t\t"))
        gallons_used = float(input("Enter gallons of gas used:\t"))

        # calculate and round miles per gallon
        mpg = miles_driven / gallons_used
        mpg = round(mpg, 2)

        data_list.append(miles_driven)
        data_list.append(gallons_used)
        data_list.append(mpg)

        row_list.append(data_list)
        with open('trips.csv', 'a', newline='') as file:

            writer = csv.writer(file)
            writer.writerows(row_list)
            row_list.clear()
            data_list.clear()
        with open('trips.csv', 'r')as f:

            reader = csv.reader(f)
            for row in reader:
                print("                ".join(row))
    except ValueError:
        print("Please enter numeric value: Try again!")

    cont = input("Would you like to continue? ")

    if cont == 'y':

        continue

    else:

        print("Trips saved to file: trips.csv")
        flag = False
