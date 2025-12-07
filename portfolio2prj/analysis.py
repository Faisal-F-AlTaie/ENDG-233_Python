# analysis.py
# ENDG 233 F25
# Faisal Al-Taie
# A terminal-based program for analyzing home sales records.
# You must include the code listed below. You may add your own additional functions, variables, etc. 
# You may not import any modules.
# You may only use built-in functions that directly support compound data structures, user entry, printing, or casting (such as len(), input() or int())
# Remember to include comments throughout your code and follow the provided docstring instructions.


# ******************************************************************************************************
# Data is imported from the included records.py file. Both files must remain in the same directory.
# Do not modify the code in this section.
# You may not hardcode (manually enter in the code) any data - all values should be used from records.py.
# An alternate version of records data will be used to test your code.

import records
# ******************************************************************************************************


# ******************************************************************************************************
# DEFINE FUNCTIONS HERE
# You must complete and use all of the functions presented below
# If a function contains the word "pass", you should delete "pass" and complete the functions below
# Use the provided docstring information to determine the exact input/output/behaviour of each function

# You will need to print the following error messages:
## For invalid input of region or menu option: Error! Invalid input. Please try again.
## If the region is valid but there are no records available: There are no records available for the {region} region.
## Once the program is complete: Thank you for using our program.
## See example for format requirements
    
# Fully complete the following functions
# ******************************************************************************************************

def get_region():
    """Prints the prompt to select the region and returns a capitalized valid region name

    Returns:
        user_input (str): a capitalized valid input provided by the user
    """
    # Asking the user for a region until they provide a valid choice or quit 
    while True:
        user_input = input("Enter the region you want to select (e.g. NE) or type '0' to quit: ")

        # If the user enters 0, we signal program to quit
        if user_input == "0":
            return "0"

        #Convert input to uppercase so that it matchs the format in records.py 
        region = user_input.upper()

        # Check if the enetered region exsits in the list 
        if region in records.regions:
            return region

        # any invalid input will promt the text below
        else:
            print("Error! Invalid input. Please try again.")
            continue 
        






def print_options():
    """Prints the inner menu thats prompts the user to select a data analysis option and returns a valid option number

    Returns:
        int: a valid input provided by the user
    """
    # loop until a valid choice is entered 
    while True:
        print()
        print("Enter the number of the option you want to select:")
        print("\t1) Print Average Price")
        print("\t2) Print Maximum Bedrooms and Bathrooms")
        print("\t0) Return to Main Menu")

        # Read users menu selection as a string 
        user_input = input(">> ")


        #only accept 0,1,2 as the valid options 
        if user_input == "0" or user_input == "1" or user_input == "2":
            return int(user_input)

        else:
            # Invalid input, promt to try again 
            print("Error! Invalid input. Please try again.")
   




def get_average_price(region):
    """Takes the selected region and returns the average price of homes in the selected region

    Parameters:
        region (str): a valid region

    Returns:
        (if records in that region exist):
            float: the average price of units in the selected region
        (if no records exist):     
            int: a flag value of -1
    """
    # We start our value at zero so we can accumlate prices from all the matching records
    total_price = 0
    record_tally = 0

    # Loop through all the imported data 
    for record in records.data:
        record_region = record[0] #Region is stored in index 0 (first position) 
        record_price = int(record[1]) # Price is stored at index 1, and we need to cast it to int 

        # Only consider records that match the selected region 
        if record_region == region:
            total_price += record_price
            record_tally += 1

    # If no records are found, return the flag value of -1 
    if record_tally == 0:
        return -1
    
    # Compute and return average price if records are found 
    return total_price / record_tally

        



    
def get_bed_bath_max(region):
    """Takes the selected region and returns the maximum number of rooms and maximum number of bathrooms

    Parameters:
        region (str): a valid region

    Returns:
        (if records in that region exist):
            list: [maximum number of bedrooms, maximum number of bathrooms]
        (if no records exist):     
            int: a flag value of -1
    """
    #Initialize to zero as starting value 
    max_bedrooms = 0
    max_bathrooms = 0
    # We need to see weather at least one record for the region is found, otherwise its false 
    located_record = False

    # Loop through the records 
    for record in records.data:
        record_region = record[0] # 0 index = region 

        # Only process records that match the selected region 
        if record_region == region:
            bedrooms = int(record[2]) #bedrooms stored at index 2
            bathrooms = int(record[3]) #bathrooms stored at index 3 

            # If this is the first matching record then initialize the max values 
            if not located_record:
                max_bedrooms = bedrooms
                max_bathrooms = bathrooms
                located_record = True
            else:
                # Update max bedrooms if this record has more
                if bedrooms > max_bedrooms:
                    max_bedrooms = bedrooms
                # Update max bathrooms if this record has more 
                if bathrooms > max_bathrooms:
                    max_bathrooms = bathrooms

    # If no record was found for the region then we will return the flag of -1 
    if not located_record:
        return -1

    # Return the max bedroom and bathroom counts in a list format 
    return [max_bedrooms, max_bathrooms]

    


def print_average_price(region, average_price):
    """Prints the average price of units in a region or calls the no records message

    Parameters:
        region (str): a valid region
        average_price 
            (float): the average price of the units in a region
            (-1): if there are no records
    """
    print() # This is here just for zylabs formatting purposes 

    # If the flag value (-1) is passed, there are no records for this region
    if average_price == -1:
        print(f"There are no records available for the {region} region.")

    else:
        # Format the average price to two decimal places 
        formatted_price = "${:.2f}".format(average_price)
        print(f"The average unit price for the {region} region is {formatted_price}")
    



def print_bed_bath_max(region, data):
    """Prints the maximum bedrooms and bathrooms in a region or calls the no records message

    Parameters:
        region (str): a valid region
        data 
            (list): [maximum number of bedrooms, maximum number of bathrooms]
            (-1): if there are no records
    """
    print()
    # If the flag value (-1) is passed, there are no records for this region
    if data == -1:
        print(f"There are no records available for the {region} region.")
        
    else:
        #Extract maximum bedrooms and bathrooms from the list 
        max_bedrooms = data[0]
        max_bathrooms = data[1]
        print(f"The {region} region has a maximum of {max_bedrooms} bedrooms and {max_bathrooms} bathrooms")



# ******************************************************************************************************
# MAIN PROGRAM DEFINED BELOW

print("ENDG 233 Sales Analysis Program\n")

# while the program is still in use
while True:

    # Fill in the main code below
    region = get_region()

    # If the user enters 0, exit the loop and end the program 
    if region == "0":
        print("Thank you for using our program.")
        break

    # Show the analysis menu and get a valid menu option from the user
    option = print_options()

    # Option 1: Calculate and print average price for the selected region (We are just calling the functions now)
    if option == 1:
        average = get_average_price(region)
        print_average_price(region, average)

    # Option 2: calculate and print max bedrooms and bathrooms for the selcted region
    elif option == 2:
        num_bed_bath = get_bed_bath_max(region) 
        print_bed_bath_max(region, num_bed_bath)
  


    # Last line before next initial region prompt
    print(f"{'':=^70s}")                                 # Prints a dashed line

