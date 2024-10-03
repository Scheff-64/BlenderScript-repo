import maya.cmds as cmds
 
 
class MF_Window(object):
    # constructor
    def __init__(self):
        self.window = "MF_Window"
        self.title = "FK Control Creator"
        self.size = (400,200)
        self.displaySelected = "empty"
        self.CreateWindow()
    def CreateWindow(self, *args):
        """
        Creates GUI
        """
        # Deletes old window if open
        if cmds.window(self.window, exists=True):
            cmds.deleteUI(self.window, window=True)
        # Creates new window    
        self.window = cmds.window(self.window, title= self.title, widthHeight=self.size)
        cmds.columnLayout()
        cmds.text(self.title)
        cmds.separator(height=20)
        cmds.textField(self.displaySelected,width=200,bgc=[0.1,0.1,0.1], ed=False)
        cmds.button(label="Update list", command=self.set_textField)
        cmds.separator(height=20)
        cmds.button(label="Create", command="FKScript()")
        cmds.button(label="Close", command="FKScript()")
        # Display new window
        cmds.showWindow()
    def set_textField(self, *args):
        """"
        Writes a list to the GUI textField
        """
        self.sel = cmds.ls(selection=True)[0]
        cmds.textField(self.displaySelected, edit=True, text=self.sel)
    def FKScript(self):
        """
        Creates orient constraints for all joints found in scene
        """
        # select selected joint
        selection = cmds.ls(assemblies=True)
        topJnt = cmds.ls(selection, type="joint")[0]
        # Get all joints in the chain that belongs to the selected joint
        descendents = cmds.listRelatives(topJnt, allDescendents=True)
        descendents.append(topJnt)
        allJnts = descendents
        allJnts.reverse()
        allJnts.pop(-1)
        for jnt in allJnts:
            # create NURBS circle
            nurbsCircle = cmds.circle()
            # NURBS circle shall be names after the joint that is selected
            ctrl = cmds.rename(nurbsCircle[0], f"{jnt}_ctrl")
            #Group NURBS circle
            #Name Grp to "jointName_ctrl_fixGrp"
            fixGrpName = cmds.group(ctrl, name=f"{ctrl}_fixGrp")
            #match transform on fixGrp to the joint that is selected
            cmds.matchTransform(fixGrpName, jnt)
            # rotate ctrl(NURBS) circle y 90
            cmds.setAttr(f"{ctrl}.rotateY", 90)
            # freeze transform on ctrl
            cmds.makeIdentity(ctrl, apply=True)
            # delete history for ctrl
            cmds.delete(ctrl, ch = True)
            # create a orient constraint between ctrl and
            cmds.orientConstraint(ctrl, jnt)
            parentJnt = cmds.listRelatives(jnt, parent=True)
            if parentJnt is not None:
                cmds.parentConstraint(parentJnt, fixGrpName, maintainOffset=True)
myWindow = MF_Window()