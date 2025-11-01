people = int(input())                       # Read the input number of people
numPieces = people * 2                      # Calculate the number of pieces needed
numPizzas = numPieces / 12.0                # Calculate the number of pizzas needed
numPizzas = round((numPizzas + 0.499))      # Round up to the nearest whole pizza
cost = numPizzas * 14.95                    # Calculate the total cost of the pizzas

print('Pizzas:', numPizzas)                 # Output the number of pizzas needed
print('Cost: $', round(cost, 2))            # Output the total cost for the pizzas