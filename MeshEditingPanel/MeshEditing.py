import bpy

class MeshEditingPanel(bpy.types.Panel):
    bl_label = "Mesh Editing"
    bl_idname = "PT_Mesh_Editing_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Mesh_Tools'

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.extrude_region_move", text="Extrude")
        layout.operator("mesh.bevel", text="Bevel")
        layout.operator("mesh.loopcut_slide", text="Loop Cut")

def register():
    bpy.utils.register_class(MeshEditingPanel)

def unregister():
    bpy.utils.unregister_class(MeshEditingPanel)

if __name__ == "__main__":
    register()