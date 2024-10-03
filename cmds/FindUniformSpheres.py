import maya.cmds as cmds
import math
 
 
def findUniformSpheres():
    transformList = cmds.ls()
    for mesh in transformList:
        if "pSphere" in str(mesh):
            # check if BBox distance in xmax-xmin,ymax-ymin,zmax-zmin match
            #print(mesh)
            xmin,ymin,zmin,xmax,ymax,zmax = cmds.exactWorldBoundingBox(mesh)
            distX = xmax - xmin
            distY = ymax - ymin
            distZ = zmax - zmin
            x = round(distX, 2)
            y = round(distY, 2)
            z = round(distZ, 2)
            #print(x, y, z)
            if x == y and y == z:
                cmds.select(mesh, add=True)
                # calculate volume
                r = x / 2
                volume = 4/3 * math.pi * math.pow(r, 3.0)
                print(f'{mesh} has a volume of {volume} units')

            # deselects objects that are non uniform
            else:
                cmds.select(mesh, d=True, add=True)
        else:
            cmds.select(mesh, d=True, add=True)
findUniformSpheres()