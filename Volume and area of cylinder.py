PI = 3.14

radius = float(input())
height = float(input())

volume = PI * (radius ** 2) * height
surface_area = (2 * PI * radius * height + 2 * PI * radius**2)

print("Volume:", round(volume, 1), "cubic inches")
print("Surface area:", round(surface_area, 1), "square inches")

if (volume > 100): 
    print("That is larger than a 1 kg jar of peanut butter.")
else:
    print("That is smaller than a 1 kg jar of peanut butter.")