import pymel.core as pm


def auto_rename_object(obj_to_rename):
    suffix = object_suffix(obj_to_rename)
    print(suffix)
    
def auto_rename_selection():
    sel = pm.selected()
    for i in sel:
        auto_rename_object(i)
    
    
def get_next_index():
    pass
    

def object_suffix(obj):
    suffix_table = {
        pm.nt.Mesh: '_geo',
        pm.nt.NurbsSurface: '_geo',
    }
    for nt, suffix in suffix_table.items():
        if isinstance(obj, nt):
            print('Here')
            return suffix

  