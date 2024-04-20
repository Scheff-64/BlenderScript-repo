import bpy
from mathutils import Vector

pos = Vector((0.5, 0.5, 0.5))
init_x = pos.x
init_y = pos.y
# base = to 10 might crash blender
base = 4

for zCubes in range(base):
    for yCubes in range(base):
        for xCubes in range(base):
            if zCubes >= 2:
                bpy.ops.mesh.primitive_cube_add(location = pos)
            else:
                bpy.ops.mesh.primitive_ico_sphere_add( location = pos)

            pos.x += 3.0
        
        pos.x = init_x
        pos.y += 3.0

    pos.y = init_y
    pos.z += 3.0
