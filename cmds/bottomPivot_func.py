def bottomPivot():

    selection = cmds.ls(sl=1)
    
    # print(selection)
    
    if selection == []:
        cmds.warning("Selection is empty!")
        
    for selected in selection:
    
        # center pivot, outsid for loop selection not selected
        cmds.xform(selected, cp=1)
        
        # get the bounding box, outsid for loop selection not selected
        bounding_box = cmds.xform(selected, q=1, bb=1, ws=1)
        
        # assign variables to bounding_box
        x_min, y_min, z_min, x_max, y_max, z_max = bounding_box
        
        #print(bounding_box)
        
        # move pivot to bottom y point, selection[0] if outside for loop not selected
        cmds.move(y_min, [selected+'.scalePivot', selected+'.rotatePivot' ], y=1, absolute=1 )
        
        # move object to grid in y. remove to avoid object transform.
        cmds.move(y_min*-1, selected, r=1, y=1)
        

bottomPivot()