import bpy
import random
import math

ico_sphere_radius = 0.5
scale_fac = 1.0
# angle = math.radians(137.5)
angle = math.radians(random.uniform(137.0, 138.0))
count = 300

for n in range(count):
    current_angle = n *angle

    current_radius = scale_fac * math.sqrt(n)

    x = current_radius * math.cos(current_angle)
    y = current_radius * math.sin(current_angle)
    

    bpy.ops.mesh.primitive_ico_sphere_add(radius=ico_sphere_radius, location=(x, y, 0))
