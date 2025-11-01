# Read input values
low = int(input())
high = int(input())
x = int(input())

# Initialize counter
count = 0

# Loop through range from low to high (inclusive)
for i in range(low, high + 1):
    if i % x == 0:
        count += 1

# Output the result
print(count)
