#1
#Write a program that asks the user for a number of a month and
# then prints out the corresponding season (spring, summer, autumn, winter).
# Save the seasons as strings into a tuple in your program.
# We can define each season to last three months, December being the first month of winter.

seasons="spring", "summer", "autumn", "winter"
number_month=int(input("enter the number of months you want (1-12): "))

#ewinter=12,1 2
#spring=3,4,5
#summer=6,7,8
#autumn=9,10,11

if number_month == 12 or number_month == 1 or number_month == 2:
    print(seasons[3])
elif number_month == 3 or number_month == 4 or number_month == 5:
    print(seasons[0])
elif number_month== 6 or number_month == 7 or number_month == 8:
    print(seasons[1])
elif number_month == 9 or number_month == 10 or number_month == 11:
    print(seasons[2])