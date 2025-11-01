# Define your function here 
def exact_change(user_total): 
    num_quarters = user_total // 25
    user_total = user_total - (num_quarters * 25)
    
    num_dimes = user_total // 10
    user_total = user_total - (num_dimes * 10)
    
    num_nickels = user_total // 5
    user_total = user_total - (num_nickels * 5)
    
    num_pennies = user_total 
    
    return [num_pennies, num_nickels, num_dimes, num_quarters]


input_val = int(input())    
num_coins = exact_change(input_val)
    
if input_val <= 0:
    print("no change") 
else:
    # Quarters
    if num_coins[3] > 1:
        print(f"{num_coins[3]} quarters")
    elif num_coins[3] == 1:
        print("1 quarter")
    
    # Dimes
    if num_coins[2] > 1:
        print(f"{num_coins[2]} dimes")
    elif num_coins[2] == 1:
        print("1 dime")
    
    # Nickels
    if num_coins[1] > 1:
        print(f"{num_coins[1]} nickels")
    elif num_coins[1] == 1:
        print("1 nickel")
    
    # Pennies
    if num_coins[0] > 1:
        print(f"{num_coins[0]} pennies")
    elif num_coins[0] == 1:
        print("1 penny")
