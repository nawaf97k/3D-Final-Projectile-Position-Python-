#Calculating final trajectory location in 3D

import math

#Intial parameters
vi = float(input("Intial velocity > "))
bearing = float(input("Angle along horizontal plane (bearing) > "))
elevation = float(input("Angle along vertical plane (elevation) > "))
t = float(input("Final location after time > "))
g = 9.81

#calculations
dxf = vi * math.cos(bearing * 0.0174533 ) * math.cos(elevation * 0.0174533 ) * t
dyf = vi * math.sin(bearing * 0.0174533 ) * math.cos(elevation * 0.0174533 ) * t
dyz = vi * math.sin(elevation * 0.0174533) * t - 0.5 * g * t**2

print("Final X coordinate = ", dxf)
print("Final Y coordinate = ", dyf)
print("Final Z coordinate = ", dyz)

