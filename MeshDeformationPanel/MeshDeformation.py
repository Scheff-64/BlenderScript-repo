import bpy


class MeshDeformationPanel(bpy.types.Panel):
    bl_label = "Mesh Deformation"
    bl_idname = "PT_Mesh_Deformation_Panel"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Deform Tools'

    def draw(self, context):
        layout = self.layout
        layout.operator("object.modifier_add", text="Add Lattice Modifier").type = 'LATTICE'
        layout.operator("object.modifier_add", text="Add Deform Modifier").type = 'SIMPLE_DEFORM'

def register():
    bpy.utils.register_class(MeshDeformationPanel)

def unregister():
    bpy.utils.unregister_class(MeshDeformationPanel)

if __name__ == "__main__":
    register()