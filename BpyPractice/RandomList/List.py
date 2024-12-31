import bpy

import random

coordinates = []

object_count = 10
for _ in range(object_count):
    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    z = random.uniform(-5, 5)
    coordinates.append([x, y, z])

for _ in range(object_count):

    x = random.uniform(-5, 5)
    y = random.uniform(-5, 5)
    z = random.uniform(-5, 5)
    bpy.ops.mesh.primitive_ico_sphere_add(radius=1, location=(x, y, z))