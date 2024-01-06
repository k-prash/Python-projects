#Prashanth_Krishna 
#Grade validation, calculation and submission

#Input for the number of students
number_of_students = int(input("Enter how many students need to be graded:"))
print("")#Print blank line for user readability
print("")
#for loop which loops for the number of students inputted
for i in range(1,(number_of_students+1)):                     
    print("Student",i,)#Print student ID for user recognition

    
    print("------------------ Coding Grade -------------------")#Sectional barriers to differentiate between the different inputs        
    coding_grade = int(input("Enter the coding grade:"))#Grade input
    if coding_grade in range(50,101):#if statement to validate the grade inputted for the set range
            print("")
            print("Coding grade validated.")#If grade in valid range, print confirmation message to user
    else:
        #If grade not in valid range begin while loop which loops input until user has input a valid grade in the set range
        while coding_grade not in range(50,101):
            print("")
            print("The grade inputted is outside the valid range of 50-100.")
            coding_grade = int(input("Please re-enter the coding grade in the valid range 50-100:"))
        print("")
        print("Coding grade validated.")


    #Testing grade section almost identical to coding grade section apart from name
    print("------------------ Testing Grade ------------------")            
    testing_grade = int(input("Enter the testing grade:"))
    if testing_grade in range(50,101):
            print("")
            print("Testing grade validated.")
    else:
        while testing_grade not in range(50,101):
            print("")
            print("The grade inputted is outside the valid range of 50-100.")
            testing_grade = int(input("Please re-enter the testing grade in the valid range 50-100:"))
        print("")
        print("Testing grade validated.")


    #Days late section largely similar to previous sections, apart from difference of set range and thus range of valid user input
    print("------------------ Days late ----------------------")            
    days_late = int(input("Enter the days late:"))
    if days_late in range(3):
            print("")
            print("Days late validated.")
    else:
        while days_late not in range(3):
            print("")
            print("The number of days late inputted is outside the valid range 0-2.")
            days_late = int(input("Please re-enter the number of days late in the valid range 0-2:"))
        print("")
        print("Days late validated.")


    #Calculations for raw total grade and final total grade after days late penalties
    raw_total_grade = (coding_grade + testing_grade)/2
    final_total_grade = (raw_total_grade) - (days_late*5)


    #Echo inputs and print final grades in table format before loop proceeds with next student or loop breaks after no remaining students
    print("------------------ Final Grades -------------------")            
    print("stud-id:   coding:   tests:   late:   raw grade:   final grade:")
    print(i,"          ",coding_grade,"    ",testing_grade,"    ",days_late,"       ",raw_total_grade,"       ",final_total_grade)
    print("")
    print("")


#After all student grade validation, calculation and submission complete, loop breaks and prints confirmation message to user
print("All grade validation, calculation and submission complete.")
