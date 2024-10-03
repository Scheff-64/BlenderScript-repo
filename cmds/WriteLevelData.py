import maya.cmds as cmds
import os


selection = cmds.ls(sl=True)

# Open the file for writing
home_dir = os.path.expanduser("~")
file_path = os.path.join(home_dir, "Documents", "Data.txt")

with open(file_path, 'w') as fileName:
    for item in selection:
        # Get translate values
        transX = cmds.getAttr('.translateX')
        transY = cmds.getAttr('.translateY')
        transZ = cmds.getAttr('.translateZ')
        
        # Get rotation values
        rotX = cmds.getAttr('.rotateX')
        rotY = cmds.getAttr('.rotateY')
        rotZ = cmds.getAttr('.rotateZ')
        
        # Write data to file
        fileName.write(f"|Object: {item}|\n"
                       f"|x = {transX}|\n"
                       f"|y = {transY}|\n"
                       f"|z = {transZ}|\n"
                       f"|rot X = {rotX}|\n"
                       f"|rot Y = {rotY}|\n"
                       f"|rot Z = {rotZ}|\n")
