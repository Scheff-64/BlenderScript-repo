import maya.cmds as cmds


def VertexColorOffset():
    # selects the group
    get_grp_selection = cmds.ls("bulletGroup")
    
    transfom_list = cmds.listRelatives(get_grp_selection, c=True)
    #print(transfom_list)
    
    #shapes = cmds.listRelatives(transfom_list, shapes=True)
    #print(shapes)
    
    for index, bullet in enumerate(transfom_list):
        
        try:
            existing_color_sets = cmds.polyColorSet(bullet, q=True, acs=True)
        					
            # Check if there is already a posOffset color set
            if "posOffset" in existing_color_sets:
                cmds.polyColorSet(bullet, d=True, cs="posOffset")
        except:
            pass
        
        # add the color set
        cmds.polyColorSet(bullet, colorSet = "posOffset",rpt="rgb", create=True, clamped = False)
        
        # get a list of vertices
        vertices = cmds.getAttr(bullet + ".vrts", multiIndices=True)
        #print(vertices)
        
        # make sure we don't go out of range
        if(index+1 >= len(transfom_list)):
            break
        next_bullet = transfom_list[index+1]
        
        # for each vertex i want to get the position of the current one and next vertex
        for i in vertices:
            
            vertex_pos = cmds.xform(f"{bullet}.vtx[{i}]", q=True, translation=True, worldSpace=True)
            next_vertex_pos = cmds.xform(f"{next_bullet}.vtx[{i}]", q=True, translation=True, worldSpace=True)
            
            # calculate the offset 
            offset_X = next_vertex_pos[0] - vertex_pos[0]
            offset_Y = next_vertex_pos[1] - vertex_pos[1]
            offset_Z = next_vertex_pos[2] - vertex_pos[2]
            offset = (offset_X , offset_Y, offset_Z)
            
            # set the rgb color to the vertex
            cmds.polyColorPerVertex(f"{bullet}.vtx[{i}]", rgb = offset, colorDisplayOption = True)
            #cmds.polyColorPerVertex(f"{bullet}.vtx[{amount}]", rgb = (1,0,0), colorDisplayOption = True)

VertexColorOffset()