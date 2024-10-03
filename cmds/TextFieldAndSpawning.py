import maya.cmds as mc

global objectCountField
global objectRadiusField


def showUI():
    # must put global variable inside func
    global objectCountField
    global objectRadiusField
    
    myWin = mc.window(title="Prompt", widthHeight = (300,300))
    mc.columnLayout()
    
    #Create field
    objectCountField = mc.intField(minValue=1)
    objectRadiusField = mc.floatField(minValue=1.0)
    
    mc.text(label="Number you would like to create")
    mc.text(label="Radius of your sphere")
    
    mc.button(label="Cube", command = buttonMethod, enable=True)
    
    # This is what show our window on screen
    mc.showWindow(myWin)

    


#sphere and cube objects in here. * for multiple args
def buttonMethod(*args):
    mc.polyCube()
    numspheres = mc.intField(objectCountField, query=True, value=True)
    radSphere = mc.floatField(objectRadiusField, query=True, value=True)
    
    # offset the posistion of the spheres as they are created
    for i in range(numspheres):
        mc.polySphere(radius = radSphere)
        mc.move((i * radSphere * 3.0), 0, 0)
        
showUI()
    