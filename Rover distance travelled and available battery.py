#Prashanth_Krishna
#Input directional angle and time of travel to ouput distance travelled and battery usage

#Import libraries
import math

#Constants
speed_of_rover = 1.5
battery_loss_rate = 2.7
maximum_battery = 100

#Inputs
angle_in_deg = float(input("Enter angle from 0 - 90(degrees):"))
time_in_seconds = float(input("Enter travel time(seconds):"))

#Conversion
angle_in_rad = math.radians(angle_in_deg)

#Calculations
distance_travelled = speed_of_rover*time_in_seconds

sina = math.sin(angle_in_rad)

cosa = math.cos(angle_in_rad)

horizontal_dt = sina*distance_travelled

vertical_dt = cosa*distance_travelled

estimated_battery_usage = time_in_seconds*battery_loss_rate

battery_remaining = maximum_battery-estimated_battery_usage

total_battery_needed = estimated_battery_usage*2

#Outputs
print("-------------------------------------------")
print("Input angle:",(angle_in_deg),"degrees")
print("Input time:",(time_in_seconds),"seconds")
print(f"Distance travelled:{distance_travelled:.3f} m")
print(f"Horizontal distance travelled:{horizontal_dt:.3f} m")
print(f"Vertical distance travelled:{vertical_dt:.3f} m")
print("-------------------------------------------")

#Sequential output
if(estimated_battery_usage>maximum_battery):#if battery used exceeds total battery, rover can't reach
    print("The robot cannot reach the desired location,\nbecause the required battery would be",(estimated_battery_usage),"%,\nwhich is greater than the maximum battery capacity of",(maximum_battery),"%")
elif(total_battery_needed>maximum_battery):#if battery needed for way there and back exceeds total battery, rover can't reach back
    print("The robot has reached the desired location,\nbut can not return because the required battery to travel back is",(estimated_battery_usage),"%,\nwhich is greater than the battery remaining of",(battery_remaining),"%")
else:#if battery needed for way there and back does not exceed total battery, rover can reach back
    print("The robot has reached the desired location,\nand can return because the required battery to travel back is",(estimated_battery_usage),"%,\nwhich is less than the battery remaining of",(battery_remaining),"%")

#Test       angle, time           expected(dt,hdt,vdt,battery)                        actual(dt,hdt,vdt,battery)                        comment
#1          0, 0                    0,0,0,no change                                   0,0,0,no change                                   zero case normal
#2          0, 5                    7.5,0,7.5, 13.5% loss, can return                 7.5,0,7.5, 13.5% loss, can return                 ok
#3          30,40                   52.5, 26.25, 45.466, 94.5% loss, can't return     52.5, 26.25, 45.466, 94.5% loss, can't return     ok
#4          75,40                   60, 57.656, 15.529, 108% loss, can't reach        60, 57.656, 15.529, 108% loss, can't reach        ok
#5          27.5,6.76               10.14,4.682,8.994, 18.252 loss, can return        10.14,4.682,8.994, 18.252 loss, can return        float ok
#6          a,b                     error                                             error                                             ok
