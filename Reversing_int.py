num = int(input("Please enter a number: \n"))
print("Original Number:", num)

reverse_number = ""

while num > 0:
    remainder = num % 10
    reverse_number += str(remainder)
    num = num // 10
print("Reversed Number:", reverse_number)