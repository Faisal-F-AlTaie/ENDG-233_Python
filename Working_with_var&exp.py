d1 = float(input())
d2 = float(input())
t1 = float(input())
t2 = float(input())

delta_position = d2 - d1
delta_time = t2 - t1
avg_velocity = delta_position / delta_time
avg_accel = avg_velocity / delta_time

print(f"Delta position = {delta_position:.2f} meters") 
print(f"Delta time = {delta_time:04.1f} seconds") 
print(f"Calculated velocity = {avg_velocity:.2f} m/s") 
print(f"Calculated acceleration = {avg_accel:.1f} m/s^2") 