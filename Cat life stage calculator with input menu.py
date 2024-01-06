#Prashanth_Krishna
#Input menu with options to determine cat life stage and age in human years

#Input menu
print("Cat Age Main Menu\nA. Months 8 to 24\nB. Years 3 to 6\nX. Exit Program")
print("-------------------------")
menu_option = input("Enter option (A, B or X):")
menu_option = menu_option.upper()
print("-------------------------")

#Nested if output
if(menu_option == "A"):#Menu option A, Junior life stage
    cat_age = int(input("Enter an age in months:"))
    print("-------------------------")
    if cat_age in range (8,25):#Input validation
        human_age = (11 + (cat_age-8))#Human year calculation
        print("Your cat is at it's junior lifestage, and is",(human_age),"years old in human years.")
    else:
        print("ERROR, the input age is outside the given range and thus the program has terminated.")
elif(menu_option == "B"):#Menu option B, Prime life stage
    cat_age = int(input("Enter an age in years:"))
    print("-------------------------")
    if cat_age in range (3,7):
        human_age = (28 + ((cat_age-3)*4))
        print("Your cat is at it's prime lifestage, and is",(human_age),"years old in human years.")
    else:
        print("ERROR, the input age is outside the given range and thus the program has terminated.")
elif(menu_option == "X"):#Menu option X, Exit program
    print("-------------------------")
    print("You have exit the program.")
else:#Invalid menu input
    print("-------------------------")
    print("Invalid menu option error.")



#Test       Menu option, Age           Expected                         Actual                          Comment
#1          A, 8                     junior, 11 yrs                   junior, 11 yrs                      ok
#2          A, 24                    junior, 27 yrs                   junior, 27 yrs                      ok
#3          A, 25                    error input range                error input range                  boundry test ok
#4          B, 2                     error input range                error input range                  boundry test ok
#5          B, 6                     prime, 40 yrs                    prime, 40 yrs                       ok
#6          B, k                     error crash                      error crash                        input test ok
#7          X, N/A                   user has exit the program        user has exit the program          exit program ok
#8          r, N/A                   invalid menu option              invalid menu option                input test ok
