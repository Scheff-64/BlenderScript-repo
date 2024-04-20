import bpy

# col_name = "monkeys"
# collection = bpy.data.collections.new(name=col_name)
# bpy.context.scene.collection

# Link our Collection "monkeys" that only exist in blender files to the scene outliner. 
# scene_collection = bpy.context.scene.collection 
# scene_collection.children
# scene_collection.children.link(collection)

# Link Selected object to collection
# obj = bpy.context.active_object
# obj
# collection.objects.link(obj)

# Removes object from previous collection
# bpy.data.collections['Collection'].objects.unlink(obj)

# Moves all objects name "Suz" to the new collections and removes them from the old collection
# source_collection = bpy.data.collections['Collection']
# destination_collection = collection
# for obj in bpy.data.objects:
#      if "Suz" in obj.name:
#          source_collection.objects.unlink(obj)
#          destination_collection.objects.link(obj)



col_name = "cubes"
collection = bpy.data.collections.new(name=col_name)
bpy.context.scene.collection

scene_collection = bpy.context.scene.collection 
scene_collection.children
scene_collection.children.link(collection)

source_collection = bpy.data.collections['Collection']
destination_collection = bpy.data.collections.new(name="cubes")
scene_collection.children.link(destination_collection)

for obj in bpy.data.objects:
    if "Cube" in obj.name:
        source_collection.objects.unlink(obj)
        destination_collection.obhects.link(obj)