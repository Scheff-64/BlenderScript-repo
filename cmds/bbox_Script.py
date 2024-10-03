import maya.cmds as cmds

def CreateBoundingBoxCollision(objectOriented = True):
    #Hitta alla meshar i scenen
    objects = cmds.ls(type = "mesh", long = True) 
    
    parents = []
    #Sortera ut bara parents
    for mesh in objects:
        splitNames = mesh.split("|")
        if splitNames[1] not in parents: 
            parents.append(splitNames[1])
            
    #Ta fram bounding box datan för varje mesh
    for mesh in parents:
        
        if objectOriented:
            preRotate = cmds.getAttr(f"{mesh}.rotate")[0]
            cmds.setAttr(f"{mesh}.rotate",0,0,0)
        
        bbox = cmds.exactWorldBoundingBox(mesh)
        
        xMin,yMin,zMin,xMax,yMax,zMax = bbox
        
        xSize = xMax - xMin
        ySize = yMax - yMin
        zSize = zMax - zMin
        #Skapa mesh för att visa hur "collision mesh" ser ut.
        bboxPreview = cmds.polyCube(w = xSize, h = ySize, d = zSize, name = f"{mesh}_col") 
        
        if objectOriented:
            #Sätt tillbaka rotation för bounding box och mesh
            cmds.setAttr(f"{bboxPreview[0]}.rotate", preRotate[0],preRotate[1],preRotate[2])
            cmds.setAttr(f"{mesh}.rotate", preRotate[0],preRotate[1],preRotate[2])
        
        #Få tag på translate för current mesh
        #meshTranslate = cmds.getAttr(f"{mesh}.translate")[0]
        meshTranslate = cmds.objectCenter(mesh)
        
        #Sätta translate för bboxPreview 
        cmds.setAttr(f"{bboxPreview[0]}.translate", meshTranslate[0],meshTranslate[1],meshTranslate[2])
        
        #Sätter jag wireFrame och color för snyggt
        cmds.setAttr(f"{bboxPreview[0]}.overrideEnabled",1)
        cmds.setAttr(f"{bboxPreview[0]}.overrideShading",0)
        cmds.setAttr(f"{bboxPreview[0]}.overrideColor",4)

CreateBoundingBoxCollision(objectOriented = True)