import maya.cmds as cmds


class MR_Window(object):
    
    # conatructor
    def __init__(self):
        self.window = "MR_Window"
        self.title = "Cube Creator"
        self.size = (400, 400)
        
        # close old window
        if cmds.window(self.window, exists = True):
            cmds.deleteUI(self.window, window = True)
            
        # create new window
        self.window = cmds.window(self.window, title = self.title, widthHeight = self.size)
        
        cmds.columnLayout(adjustableColumn = True)
        
        cmds.text(self.title)
        cmds.separator(height = 20)
        
        self.cubeName = cmds.textFieldGrp(label = "Cube Name: ")
        self.cubeSize = cmds.floatFieldGrp(numberOfFields = 3, label = "Size: ", value1 = 1, value2 = 1, value3 = 1)
        
        
        self.cubeSubdivs = cmds.intSliderGrp(field = True, label = "subdivs",
                        minValue = 1, maxValue = 10, value = 1)
                        
        self.cubeCreateBtn = cmds.button(label = "Create Cube", command = self.createCube)
        # display new window
        cmds.showWindow()
    
    
    def createCube(self, *args):
        
        name = cmds.textFieldGrp(self.cubeName, query = True, text = True)
        
        width = cmds.floatFieldGrp(self.cubeSize, query = True, value1 = True)
        height = cmds.floatFieldGrp(self.cubeSize, query = True, value2 = True)
        depth = cmds.floatFieldGrp(self.cubeSize, query = True, value3 = True)
        
        subdivs = cmds.intSliderGrp(self.cubeSubdivs, query = True, value = True)
        
        cmds.polyCube(name = name, width = width, height = height, depth = depth,
                        subdivisionsWidth = subdivs, subdivisionsHeight = subdivs, subdivisionsDepth = subdivs,)
        
        
myWindow = MR_Window()
