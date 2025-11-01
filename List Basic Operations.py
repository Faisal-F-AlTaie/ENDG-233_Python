my_flower1 = input()
my_flower2 = input()
my_flower3 = input()

your_flower1 = input()
your_flower2 = input()

their_flower = input()

# 1. TODO: Define my_list containing my_flower1, my_flower2, and my_flower3
my_list = [my_flower1, my_flower2, my_flower3]

# 2. TODO: Define your_list containing your_flower1 and your_flower2
your_list = [your_flower1, your_flower2] 

# 3. TODO: Define our_list by concatenating my_list and your_list
our_list = my_list + your_list
print(our_list)

# 4. TODO: Append their_flower to the end of our_list
our_list.append(their_flower)
print(our_list)

# 5. TODO: Replace my_flower2 in our_list with their_flower
our_list[1] = their_flower
print(our_list)

# 6. TODO: Remove the first occurrence of their_flower from
# our_list without using index()
for i in range(len(our_list)):
    if our_list[i] == their_flower:
        our_list = our_list[:i] + our_list[i+1:]
        break
print(our_list)

# 7. TODO: Remove the second element of our_list
our_list = our_list[:1] + our_list[2:]
print(our_list)
