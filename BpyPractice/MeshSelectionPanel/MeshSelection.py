import bpy

class MeshSelectionPanel(bpy.types.Panel):
    bl_label = "Mesh Selection"
    bl_idname = "PT_Mesh_Selection_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Selection Tool'

    def draw(self, context):
        layout = self.layout
        layout.operator("mesh.select_all", text = "Select all").action = 'SELECT'
        layout.operator("mesh.select_all", text = "Select inverse").action = 'INVERT'
        layout.operator("mesh.select_mode", text = "Vertecies").type = 'VERT'
        layout.operator("mesh.select_mode", text = "Edges").type = 'EDGE'
        layout.operator("mesh.select_mode", text = "Faces").type = 'FACE'
        

def register():
    bpy.utils.register_class(MeshSelectionPanel)

def unregister():
    bpy.utils.unregister_class(MeshSelectionPanel)

if __name__== "__main__":
    register()