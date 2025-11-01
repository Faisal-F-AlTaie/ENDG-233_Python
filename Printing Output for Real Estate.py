                                                  # Pseudocode
current_price = int(input())                      # Read the current price
last_months_price = int(input())                  # Read the last month price

change_in_p = current_price - last_months_price  # Calculate the change in the house price                                             
                                                 # Calculate the monthly mortgage
change_in_m = (current_price * 0.051) / 12                                                 
print("This house is $" + str(current_price) + ". The change is $" + str(change_in_p) + " since last month.")
print("The estimated monthly mortgage is $" + str(round(change_in_m, 2)) + ".")                        # Display the house price and change in house price
                                                                                          # Display the mortgage amount 
   