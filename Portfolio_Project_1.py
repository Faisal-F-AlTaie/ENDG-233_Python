# ENDG 233 Fall 2025
# Portfolio Project 1
# race.py
# Program for calculating the time it takes for a car to complete a race depending on car parameters, driver recklessness, and road conditions.


# Required Imports to use mathmatical functions in python such as math.ceil (will use for fuel calculation)
import math

# reduce comments, and imporve spacing (not to much not to little)

# setting a flag
invalid_input = False

# Inputs for car selection, driver selection, race distance, and road condition
car_selection = int(input("Select a car number: "))
driver_selection = int(input("Select a driver number: "))
race_distance = int(input(("How long is the race in kilometers?: ")))
road_condition = str(input("Is the road going to be wet? (True or False): ")) 



# Driver selection: In our input statements, the user must select a driver. There choice will allow us to obtain a value of how reckless each driver is for our calculations below 
if (driver_selection >= 1 and driver_selection <= 3 ):
    if (driver_selection == 1):
        DRIVER_RECKLESSNESS = 1.1

    elif (driver_selection == 2):
        DRIVER_RECKLESSNESS = 1.2

    elif (driver_selection == 3):
        DRIVER_RECKLESSNESS = 1.3  

else: # User must select 1,2, or 3 as a choice, any other input will be rejected by the program 
    invalid_input = True
    print("Input number not recognized.")
    
    

# Car Selection: In our input statments, we promt the user to select a car, each car has a diffrent top speed, fuel capacity, and fuel effeciency which will affect the calculations below
if (car_selection >= 1 and car_selection <= 3):
    if (car_selection == 1):
        TOP_SPEED = 250 # units of Km/h
        FUEL_CAPACITY = 60 # units of L
        FUEL_EFFICIENCY = 7.3 # units of km/L

    elif (car_selection == 2):
        TOP_SPEED = 311 # units of Km/h
        FUEL_CAPACITY = 60 # units of L
        FUEL_EFFICIENCY = 7.3 # units of km/L

    elif (car_selection == 3):
        TOP_SPEED = 375 # units of km/h
        FUEL_CAPACITY = 70 # units of L
        FUEL_EFFICIENCY = 5.2 # units of km/L

else: # User must select 1,2, or 3, any other input will be rejected by the program 
    invalid_input = True
    print("Input number not recognized." )    


# Road Condition: if the road condition above is True, then the road is wet (multiplier = 1.2), otherwise the road is dry (multiplier = 1.0)

if road_condition == "True":
    ROAD_MULTIPLIER = 1.2

elif road_condition == "False":
    ROAD_MULTIPLIER = 1.0

else: # They have to enter "True" or "False" in here (case-sensitive)
    invalid_input = True
    print("Input number not recognized.")    



# Calculations: From our user inputs above, now we will take the associated values from the user choices and calculate, the time to finish the race
if invalid_input == False: # If are flag is False (its not a invalid input) we will execute the calculations 
    
        # Refuling: This section of code will calculate our associated fuel time, that we will need later
    fuel_range = FUEL_CAPACITY * FUEL_EFFICIENCY # fuel_range = How far the car is gonna travel at 100% capacity.
    full_tank_required = math.ceil(race_distance / fuel_range) # Determine how many full tanks you need to finish the race. 
    refules_required = full_tank_required - 1 # How many full tanks of gas we will need to finish the race. We subtract one to show one full tank has been used up
    fuel_time = (5 / 60) * refules_required # 5 minute fuel time expressed in hours, multiplied by how many times you need to refuel. Units of min


        # Time calculations: Taking our  final refuel time now, we will use it and calculate the total_tim with the remaining conditins that may affect total time (driver recklessness, and road condition)
    time_complete_race = (race_distance / TOP_SPEED) # This is the time to complete race with no conditions added. 
    base_time = time_complete_race + fuel_time # This is the time to complete the race without modifiers with the added time to refuel, throughout the race
    time_with_driver_mod = base_time * DRIVER_RECKLESSNESS   # Now we consider the driver recklessness, and treat it as a multiplier
    total_time = time_with_driver_mod * ROAD_MULTIPLIER # Lastly, we take the new time we got from the product of the driver recklessnos, and multiply it by our final modifer which is road condition 

# This is our print statement, which rounds our total time in hours, and diaplys all user input choices, in a nice formatted statement 
    print("The total travel time for Car {0} with Driver {1} to travel {2} km is {3:0.1f} hours.".format(car_selection, driver_selection, race_distance, total_time))


# End Code