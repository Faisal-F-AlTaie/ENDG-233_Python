hours = int(input('Enter the number of hours spent per week.\n'))    # Read the number of hours from the user
print('Number of input hours:', hours)      # Print the input number of hours
minutes = hours * 60            # Calculate number of minutes from hours
print('Converted to minutes:', minutes)     # Print the converted number of minutes
seconds = minutes * 60          # Calculate number of seconds from minutes
print('Converted to seconds:', seconds)     # Print the converted number of seconds
expected_hours = hours * 52                 # Calculate the total number of hours per year
print('Expected hours in a year:', expected_hours)      # Print the expected hours in a year
