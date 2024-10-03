import maya.cmds as mc


class Tabs:
    
    
    def __init__(self):
        self.win = mc.window(title="Tabs", menuBar = True, widthHeight=(200,200))
        
        fileMenu = mc.menu(label = "Exo´s Menu")
        loadOption = mc.menuItem(label = "Load")
        saveOption = mc.menuItem(label = "Save")
        mc.setParent("..")
        
        fileMenu = mc.menu(label = "Geo List")
        mc.setParent("..")
        
        self.tabs = mc.tabLayout()
        
        fTab = mc.columnLayout()
        mc.tabLayout(self.tabs, edit=True, tabLabel=[fTab, 'First Tab'])
        mc.button(label="A Button")
        mc.setParent("..")
        
        sTab = mc.scrollLayout()
        mc.tabLayout(self.tabs, edit=True, tabLabel=[sTab, 'Second Tab'])
        mc.button(label="A Second Button")
        
        for i in range(20):
            mc.button(label="Button in Loop: " + str(i+1))
        
        mc.setParent("..")
        
        mc.showWindow(self.win)
        

Tabs()
