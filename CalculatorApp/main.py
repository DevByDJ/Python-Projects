# Welcome to my Calculator Program
# This is a script I created to understand the concepts of While Loops, if statements and variables/functions

# Created By Danny Joseph

run_calculator = 1;                                                     # This will variable will control the while loop
user_name = input("Enter your name: ")
print("--------------------------")
while run_calculator == 1:                                              # While Loop conditions
    print("\nHello " + user_name, " \nWhat would you like to calculate today?")
    first_num = input("First number: ")
    second_num = input("Second number: ")
    print("Now how would you like to calculate these numbers?")
    print("1.) Add\n2.) Subtract\n3.) Multiply\n4.) Divide\n")
    user_selection = input()                                            # Determines operation performed
    if int(user_selection) == 1:
        total = (int(first_num) + int(second_num))
    if int(user_selection) == 2:
        total = (int(first_num) - int(second_num))
    if int(user_selection) == 3:
        total = (int(first_num) * int(second_num))
    if int(user_selection) == 4:
        total = (int(first_num) / int(second_num))

    print("\nTotal: " + str(total))
    print("Would you like to calculate another? y/n\n")                   # Loops program if user decides 'y'
    user_stay = input()
    if user_stay == "y":
        run_calculator = 1;
    if user_stay == "n":
        run_calculator = 0;

print("\nClosing app..")                                                  # Ends the program.
