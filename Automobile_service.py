print('Welcome to ENDG_AutoServices. We are happy to provide the following services:\n')
print('1. Oil Change\t\t$35')
print('2. Tire Rotation\t$19')
print('3. Car Wash\t\t$7\n')

# Get user input
service_num = int(input('Please enter requested service number:'))

# Define service options and prices
if service_num == 1:
    service_name = 'Oil Change'
    service_cost = 35
elif service_num == 2:
    service_name = 'Tire Rotation'
    service_cost = 19
elif service_num == 3:
    service_name = 'Car Wash'
    service_cost = 7
else:
    print('Service not available')
    exit()

# Calculate total cost with 5% GST
total_cost = service_cost * 1.05

# Output the results
print(f'\nService requested:\t{service_name}')
print(f'Service cost:\t\t${service_cost}')
print(f'Total cost:\t\t${total_cost:.2f}')
