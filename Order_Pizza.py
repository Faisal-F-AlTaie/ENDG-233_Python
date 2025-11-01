# Use the provided code to create a flowchart. Your instructor will review the solution in class.

numPizza = int(input())                 # Read input from user
savings = numPizza * 9.99 * 0.15        # Calculation of savings
subTotal = numPizza * 9.99 * 0.85       # Calculation of subtotal
totalDue = subTotal * 1.05              # Calculation of total with 5% tax

print('You Saved: $', round(savings, 2))     # Print savings value formatted to two decimal places
print('Subtotal: $', round(subTotal, 2))     # Print subtotal value formatted to two decimal places
print('Total due: $', round(totalDue, 2))    # Print total value formatted to two decimal places