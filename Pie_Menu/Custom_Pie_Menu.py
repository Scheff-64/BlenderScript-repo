bl_info = {
    "name": "Pie Menu: Template",
    "description": "Pie menu example",
    "author": "Martin Frykler",
    "version": (0, 0, 1),
    "blender": (3, 5, 0),
    "location": "3D View",
    "warning": "",
    "doc_url": "",
    "category": "Development",
}
import bpy
from bpy.types import Menu


def add_subdiv_modifier(subdiv_viewport_levels, subdiv_render_levels):
    obj = bpy.context.active_object
    
    if obj is None:
        print("Warning: No active object")
        return
    
    if  obj.type != 'MESH':
        print("Warning: The active object need to be a mesh")
        return
    
    bpy.ops.object.modifier_add(type="SUBSURF")
    bpy.context.object.modifiers["Subdivision"].levels = subdiv_viewport_levels
    bpy.context.object.modifiers["Subdivision"].render_levels = subdiv_render_levels
    
    
class MESH_OT_add_subdiv_mod(bpy.types.Operator):
    """Add a subdivision surf modifier to the active mesh"""
    
    bl_idname = "mesh.add_subdiv_mod"
    bl_label = "Add Subdivision Surf Modifier to the Active Mesh Object"
    bl_options = {"REGISTER", "UNDO"}
    
    subdiv_viewport_lvl: bpy.props.IntProperty(
        name="Subdiv ViewPort",
        default=1,
        min=1,
        max=3,
        description="The subdivision Levels applied in the Viewport",
    )
    
    subdiv_render_lvl: bpy.props.IntProperty(
        name="Subdiv Render",
        default=3,
        min=3,
        max=7,
        description="The subdivision Levels applied during the Viewport",
    )
    
    def execute(self, context):
        
        add_subdiv_modifier(self.subdiv_viewport_lvl, self.subdiv_render_lvl)
        
        return {"FINISHED"}

class VIEW3D_MT_PIE_template(Menu):
    # label is displayed at the center of the pie menu.
    bl_label = "Shortcut Menu"

    def draw(self, context):
        layout = self.layout

        pie = layout.menu_pie()
        
        column = pie.split().column()
        column.operator("mesh.edges_select_sharp", text="Select Sharp", icon='RESTRICT_SELECT_ON')
        column.operator("mesh.mark_seam", text="Add Seam", icon='BRUSH_CURVES_CUT')
        
        column = pie.split().column()
        column.operator("mesh.add_subdiv_mod", text="Add Subdiv Mod", icon='MOD_SUBSURF')
        column.operator("object.shade_smooth", text="Shade Smooth", icon='MOD_SMOOTH')
        
        
global_addon_keymaps = []


def register():
    bpy.utils.register_class(MESH_OT_add_subdiv_mod)
    bpy.utils.register_class(VIEW3D_MT_PIE_template)
    
    window_manager = bpy.context.window_manager
    if window_manager.keyconfigs.addon:
        keymap = window_manager.keyconfigs.addon.keymaps.new(name="3D View", space_type="VIEW_3D")

        keymap_item = keymap.keymap_items.new("wm.call_menu_pie", "A", "PRESS", ctrl=True, alt=True)
        keymap_item.properties.name = "VIEW3D_MT_PIE_template"

        # save the key map to deregister later
        global_addon_keymaps.append((keymap, keymap_item))


def unregister():
    bpy.utils.unregister_class(VIEW3D_MT_PIE_template)
    bpy.utils.unregister_class(MESH_OT_add_subdiv_mod)

    window_manager = bpy.context.window_manager
    if window_manager and window_manager.keyconfigs and window_manager.keyconfigs.addon:
        for keymap, keymap_item in global_addon_keymaps:
            keymap.keymap_items.remove(keymap_item)

    global_addon_keymaps.clear()


if __name__ == "__main__":
    register()    