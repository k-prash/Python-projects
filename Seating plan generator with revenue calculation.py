#Prashanth_Krishna
#Program that calculates seating and revenue plans for theatre

#Import random for part-house row randomization and math for rounding up break even calculations
import random
import math



#Function that asks user for inputs
def house_input():
    production_cost = int(input("Enter Production Cost:"))
    bandA_price = int(input("Enter price of one seat in band-A:"))
    bandB_price = int(input("Enter price of one seat in band-B:"))

    return production_cost,bandA_price,bandB_price



#Function that defines full house seating plan 
def full_house_define():
    #Define unary lists for band A and band B full house seats manually, as they're always full
    bandA_FH_list =[[1,1,1,1,1],[1,1,1,1,1]]
    bandB_FH_list =[[1,1,1,1,1],[1,1,1,1,1]]

    return bandA_FH_list,bandB_FH_list



#Function that calculates full house revenue
def full_house_revenue(bandA_FH_list,bandB_FH_list,bandA_price,bandB_price,production_cost):
    #Define variables for full house seats sold in both band A and B
    bandA_FH_seats_sold = 0
    bandB_FH_seats_sold = 0

    #Double for loop which adds every element to itself to find seats sold in band A
    for row in bandA_FH_list:
        for col in row:
            bandA_FH_seats_sold = bandA_FH_seats_sold + col

    #Double for loop which adds every element to itself to find seats sold in band B
    for row in bandB_FH_list:
        for col in row:
            bandB_FH_seats_sold = bandB_FH_seats_sold + col

    #Calculate band revenue from band price and band seats sold
    bandA_FH_revenue = bandA_FH_seats_sold*bandA_price
    bandB_FH_revenue = bandB_FH_seats_sold*bandB_price

    #Calculate full house revenue from band A revenue and band B revenue
    fullhouse_revenue = bandA_FH_revenue + bandB_FH_revenue

    #Calculate break even for full house from production cost and full house revenue
    break_even_FH = production_cost/fullhouse_revenue

    return bandA_FH_revenue,bandB_FH_revenue,fullhouse_revenue,break_even_FH



#Function that defines part-house seating plan
def part_house_define(bandA_price,bandB_price,production_cost):
    #Define number of rows and columns
    row = 2
    col = 5

    #Define null lists for band A and B seats before randomisation
    bandA_PH_list = [[0,0,0,0,0],[0,0,0,0,0]]
    bandB_PH_list = [[0,0,0,0,0],[0,0,0,0,0]]

    #Double for loop which randomises every element in band A and B to 0 or 1, representing empty seat or booked seat respectively
    for r in range(row):
        for c in range(col):
            bandA_PH_list[r][c] = random.randint(0,1)
            bandB_PH_list[r][c] = random.randint(0,1)

    return bandA_PH_list, bandB_PH_list



#Function that calculates part-house revenue(works nearly identical to full-house revenue calculation)
def part_house_revenue(bandA_PH_list,bandB_PH_list,bandA_price,bandB_price,production_cost):
    #Define variables for full house seats sold in both band A and B
    bandA_PH_seats_sold = 0
    bandB_PH_seats_sold = 0

    #Double for loop which adds every element to itself to find seats sold in band A
    for row in bandA_PH_list:
        for col in row:
            bandA_PH_seats_sold = bandA_PH_seats_sold + col

    #Double for loop which adds every element to itself to find seats sold in band B
    for row in bandB_PH_list:
        for col in row:
            bandB_PH_seats_sold = bandB_PH_seats_sold + col

    #Calculate band revenue from band price and band seats sold
    bandA_PH_revenue = bandA_PH_seats_sold*bandA_price
    bandB_PH_revenue = bandB_PH_seats_sold*bandB_price

    #Calculate part-house revenue from band A revenue and band B revenue
    parthouse_revenue = bandA_PH_revenue + bandB_PH_revenue

    #Calculate break even for part-house from production cost and part-house revenue
    break_even_PH = production_cost/parthouse_revenue

    return bandA_PH_seats_sold,bandB_PH_seats_sold,bandA_PH_revenue,bandB_PH_revenue,parthouse_revenue,break_even_PH



#Function which outputs the data to the user in a dashboard format
def output_data(production_cost,bandA_price,bandB_price,bandA_FH_revenue,bandB_FH_revenue,fullhouse_revenue,break_even_FH,bandA_PH_seats_sold,bandB_PH_seats_sold,bandA_PH_revenue,bandB_PH_revenue,parthouse_revenue,break_even_PH):

    #Use formating on print with triple quotations to format dashboard as desired
    print(f'''

Dashboard:
                                         £
Production cost                          = {production_cost}

Full house revenue:
Band-A: 10 seats sold at £{bandA_price} per seat    = {bandA_FH_revenue}
Band-B: 10 seats sold at £{bandB_price} per seat    = {bandB_FH_revenue}
Revenue: total for one full house        = {fullhouse_revenue}
Number of shows to break-even            = {math.ceil(break_even_FH)}



Part-house revenue:
Band-A: {bandA_PH_seats_sold} seats sold at £{bandA_price} per seat     = {bandA_PH_revenue}
Band-B: {bandB_PH_seats_sold} seats sold at £{bandB_price} per seat     = {bandB_PH_revenue}
Revenue: total for one part-house        = {parthouse_revenue}
Number of shows to break-even            = {math.ceil(break_even_PH)}

''')
    #Use math.ceil to round up break even figures as to find a more accurate result       

    return''



#Function that outputs seating plan for full house and part-house, as well as row by row data for part-house
def output_seating(bandA_FH_list,bandB_FH_list,bandA_PH_list,bandB_PH_list,bandA_price,bandB_price):


    #for loops which loop for the amount of rows in full houseband A, and print each row in band A
    print("Fullhouse Seating:")
    for row in range(len(bandA_FH_list)):
        #Use formatting in print to achieve desired output presentation
        print(f"Band A, Row {row+1} :    {bandA_FH_list[row]}")


    #for loops which loop for the amount of rows in full house band B, and print each row in band B
    for row in range(len(bandB_FH_list)):
        #Use formatting in print to achieve desired output presentation
        print(f"Band B, Row {row+3} :    {bandB_FH_list[row]}")
    print("")
    print("")


    print("Part-house Seating:")
    #Sum seats to find amount of seats sold in each row of band A
    sum_row_A = [sum(i) for i in bandA_PH_list]
    #for loop which loops for the amount of rows in part-house band A, and print each row in band A        
    for row in range(len(bandA_PH_list)):
        #Calculation to find total  income of each row of band A
        row_revenue = bandA_price*sum_row_A[row]
        #Use formatting in print to achieve desired output presentation
        print(f"Band A, Row {row+1} :    {bandA_PH_list[row]}     Row {row+1} sold a total of {sum_row_A[row]} seats, which produce an income of £{row_revenue}")


    #Sum seats to find amount of seats sold in each row of band B
    sum_row_B = [sum(i) for i in bandB_PH_list]
    #for loop which loops for the amount of rows in part-house band B, and print each row in band B
    for row in range(len(bandB_PH_list)):
        #Calculation to find total income of each row of band B
        row_revenue = bandB_price*sum_row_B[row]
        #Use formatting in print to achieve desired output presentation
        print(f"Band B, Row {row+3} :    {bandB_PH_list[row]}     Row {row+3} sold a total of {sum_row_B[row]} seats, which produce an income of £{row_revenue}")


    return''



#Main function to call all other functions
def main():

    #Call input function for production cost, band A price, and band B price
    production_cost,bandA_price,bandB_price = house_input()

    #Call full house define function for full house seating list for band A and B
    bandA_FH_list,bandB_FH_list = full_house_define()

    #Call full house revenue function with band A and B full house seating list, band A and B prices, and production cost to find band A and B full house revenues, full house revenue, and the break even figure
    bandA_FH_revenue,bandB_FH_revenue,fullhouse_revenue,break_even_FH = full_house_revenue(bandA_FH_list,bandB_FH_list,bandA_price,bandB_price,production_cost)

    #Call part-house define function for part house seating list for band A and B
    bandA_PH_list,bandB_PH_list = part_house_define(bandA_price,bandB_price,production_cost)

    #Call part-house revenue function with band A and B part-house seating list, band A and B prices, and production cost to find band A and B part-house revenues, band A and B seats sold, part-house revenue, and the break even figure
    bandA_PH_seats_sold,bandB_PH_seats_sold,bandA_PH_revenue,bandB_PH_revenue,parthouse_revenue,break_even_PH = part_house_revenue(bandA_PH_list,bandB_PH_list,bandA_price,bandB_price,production_cost)

    #Call output data function to output dashboard with all relevant data
    output_data(production_cost,bandA_price,bandB_price,bandA_FH_revenue,bandB_FH_revenue,fullhouse_revenue,break_even_FH,bandA_PH_seats_sold,bandB_PH_seats_sold,bandA_PH_revenue,bandB_PH_revenue,parthouse_revenue,break_even_PH)

    #Call output seating function to output seating for full house and part-house, as well as row by row analysis for part-house 
    output_seating(bandA_FH_list,bandB_FH_list,bandA_PH_list,bandB_PH_list,bandA_price,bandB_price)

main()
