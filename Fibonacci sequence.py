def fibonacci(n):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n ==1:
        return 1
        
    fib_list =[0,1]
    
    for i in range(n-1):
        fib_list = fib_list + [fib_list[i] + fib_list[i+1]]
        
    return fib_list[n]


start_num = int(input())
print(f'fibonacci({start_num}) is {fibonacci(start_num)}')