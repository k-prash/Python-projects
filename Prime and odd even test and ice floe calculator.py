#Prashanth_Krishna
#Prime/odd function and floe function using modularisation

#PRIME AND ODD/EVEN TEST 
def prime_odds(n):
    #define a function with an integer input n
    #Using an if statement, assign special cases for integers 0,1 and 2
    
    if n == 0:
       #0 is a special case as it has no other multiples but is not prime, and thus an outlier to our tests
       print("The integer is not prime and even")
       return ''
    
    elif n == 1:
        #1 is a special case as it has no other multiples but is not prime, and thus an outlier to our tests
        print("The integer is not prime and odd")
        return ''
    
    elif n == 2:
        #2 is a special case as it's the only even prime integer, and thus an outlier to our tests
        print("The integer is prime and even")
        return ''
    
    else:
        #for all other integers n we run a test that checks the remainder of n divided by all other integers preceding it in the range (2,n)
        for i in range(2, n):

            if n % i == 0:
            #if n has a remainder of 0 when divided by any of the integers in the range (2,n), it is not prime

                if n % 2 == 0:
                    #for all non-prime integers n we run another test that checks whether the remainder of n divided by 2 is 0
                    #if the remainder is 0 then n is not prime and even
                    print("The integer is not prime and even")
                    return ''

                else:
                    #if the remainder is not 0 then n is not prime and odd
                    print("The integer is not prime and odd")
                    return ''

            else:
            #if n doesn't have a remainder of 0 when divided by any of the integers in the range (2,n), it is prime
            #because all prime numbers except 2 are odd, we can let the for loop finish and then confirm the integer can only be prime and odd
                ""
    print("The integer is prime and odd")
    return''

#ICE FLOE FUNCTIONS
def floe_input():
    #define a floe input function to ask the user to input measurements for the freeboard ice
    height = float(input("Enter freeboard height:"))
    length = float(input("Enter freeboard length:"))
    breadth = float(input("Enter freeboard breadth:"))
    return height,length,breadth
    #return the freeboard measurements to the caller


def floe_process(height,length,breadth):
    #define a function to take three meausrements as inputs and calculate the floe volume
    h_multiplier = 9
    floe_thickness = height*h_multiplier
    floe_area = length*breadth
    volume = floe_thickness*floe_area
    return volume
    #return the floe volume to the caller


def floe_output(volume):
    #define a function that takes a volume input and outputs the floe volume to the user
    print("The volume of the floe is",volume,"m^2")
    return ''
    #return the print statement to the user


def main():
    #define the main function
    #ask for an integer input and call the prime_odds function to test whether said integer is prime/not prime and odd/even
    int1 = int(input("Please enter an integer:"))
    prime_odds(int1)

    #call the three ice floe functions for freeboard inputs, floe calculations, and floe volume output
    height, length, breadth = floe_input()
    calc = floe_process(height,length,breadth)
    floe_output(calc)

main()
