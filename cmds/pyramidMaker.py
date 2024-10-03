import maya.cmds as cmds
 
 
def PyramidMaker(levels):
    for level in range(levels):
        transY = (levels - level) - 0.5
        print(f"Height Value: {transY}")
        for row in range(level + 1):
            transX = row - (level / 2)
            for column in range(level +1):
                cube = cmds.polyCube()
                transZ = column - (level / 2)
                cmds.move(transX, transY, transZ, cube)
PyramidMaker(4)