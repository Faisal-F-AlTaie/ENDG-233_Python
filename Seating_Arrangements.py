rows = int(input('Enter number of rows: '))
cols = int(input('Enter number of columns: '))

# Starting row letter
row_letter = 'A'

# Loop through each row
for i in range(rows):
    for j in range(1, cols + 1):
        if j < 10:
            print(row_letter + '-0' + str(j), end='\t')
        else:
            print(row_letter + '-' + str(j), end='\t')
    print()  # Go to next line after each row
    
    
    # Move to the next letter in the alphabet
    row_letter = chr(ord(row_letter) + 1)
