import maya.cmds as cmds
 
 
def TriangleThreshold():
    triCountThresh = 1000
    # creates a list of all the meshes in the scene
    objList = cmds.ls(type="mesh", long=True)
    # gives a warning if there is no meshes
    if len(objList) == 0:
        cmds.warning("There is no mesh in your scene")
    else:
        for obj in objList:        
            # gets the traingle count from the obj    
            triCount = cmds.polyEvaluate(obj, triangle=True)
            # Checks if the meshes are above the threshold        
            if triCount >= triCountThresh:
                print(f'{obj} has {triCount} triangles')
            else:
                pass
 
TriangleThreshold()