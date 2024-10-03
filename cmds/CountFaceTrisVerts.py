import maya.cmds as cmds


def CurrentSelectionPolygonal(obj):
    shape_node = cmds.listRelatives(obj, shapes = True)
    
    node_type = cmds.nodeType(shape_node)
    
    if node_type == "mesh":
        return True
        
    return False


def CheckSelection():
    selected_objects = cmds.ls(sl=True)
    if (len(selected_objects) < 1):
        cmds.error("Please select a polygon-mesh model form the scene")
        
    last_selected = selected_objects[-1]
    is_polygon = CurrentSelectionPolygonal(last_selected)
    if(is_polygon):
        print("That is a polygon, good job!")
        

def GetData():
    selected_objects = cmds.ls(sl=True)
    obj = selected_objects[-1]
    vertex_N = cmds.polyEvaluate(obj, vertex=True)
    print(f"vertices: {vertex_N}")
    edge = cmds.polyEvaluate(obj, edge=True)
    print(f"edges: {edge}")
    face = cmds.polyEvaluate(obj, face=True)
    print(f"faces: {face}")


CheckSelection()
GetData()