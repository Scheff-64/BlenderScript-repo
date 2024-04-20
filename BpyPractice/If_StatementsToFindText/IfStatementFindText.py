import bpy
import math

location_offset = 3
index = 0

# for i in range(10):
#     bpy.ops.mesh.primitive_cube_add(location=(i * location_offset, 0, 0))
#     bpy.ops.mesh.primitive_ico_sphere_add(location=(i * location_offset, 0, location_offset))
#     bpy.ops.mesh.primitive_monkey_add(location=(i * location_offset, 0, 2 * location_offset))
#    
for obj in bpy.context.selected_objects:
    if "ico" in obj.name:
        obj.location.z *= 4
    if "cube" in obj.name:
        obj.rotation_euler.z = math.radians(45)
    if "suzanne" in obj.name:
        obj.scale *= 0.5

# index = 0
# for obj in bpy.data.objects:
#      if "Cube" in obj.name:
#          obj.name = f""obj.cube.{index:03d}" 
#          obj.data.name = f"mesh.cube.{index:03d}"
#          index += 1

# import bpy
#
# for i in range(5):
#     bpy.ops.mesh.primitive_monkey_add(size=2, location=(i*3, 0, 0))
#
# if list is not here ----vvvv the name will have the index number 10, 11, 12 etc. Instead of 1, 2, 3,.....
# for i, obj in enumerate(list(bpy.data.objects)):
#     obj.name = 'Suzanne_' + str(i+1)
