''' Type your code here. '''

### get the user inputs
num_1 = int(input("Enter the first number: \n"))  # Prompt and read the first number
num_2 = int(input("Enter the second number: \n")) #Prompt and read the second number


### find the loop_limit by selecting the smaller number
if num_1 > num_2:
    loop_limit = num_1
else: 
    loop_limit = num_2


### loop through all the numbers in the loop limit backwards from the largest to the 2

for iterator in range(loop_limit, 1, -1):   
    if (num_1 % iterator != 0):          # if the number is not a factor of the 1st int
        continue                         # skip this number and move to the next one
    if (num_2 % iterator != 0):           # if the number is not a factor of the 2nd int                      
        continue                         # skip this number and move to the next one

    ## check if the iterator is a prime number
    isPrime = True  # initialize the flag
    for i in range(2, iterator):  # loop through the values from 2 to (number-1)
        if (iterator % i == 0):      # if a divisor has been found
            isPrime = False           # update flag (the number is not a prime)
            break                   # break (from inner loop)
   

    
    ## GCPF found, print and stop
    if isPrime: # if the flag indicates a prime
        print("The GCD is:", iterator)  # print the GCPF
        break  # exit the outer loop
else:
### if the loop concludes natually, common factors have been not been found
    print("There are no common prime factors")  # print "...no common factors..."