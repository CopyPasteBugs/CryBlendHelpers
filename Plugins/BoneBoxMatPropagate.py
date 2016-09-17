bl_info = {
    "name": "Propagate material from selected geom proxy for all skeleton's geom proxies for CryEngine 5",
    "author": "ArticLion",
    "category": "Object",
    "blender": (2, 77, 0)   
}

import bpy
import os
import struct
import sys
import mathutils
from math import radians
from bpy.props import (BoolProperty)
from bpy.props import (EnumProperty)
from bpy.props import (FloatProperty)



          
class BoneBoxPropagate(bpy.types.Operator):
    bl_idname = "object.boneboxmatpropagate"   # unique identifier for buttons and menu items to reference.
    bl_label = "CryHelpers : Propagate material for all _boneGeometry"     # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    
    
    def PropagateBoxColliders(self, context):
        scene = context.scene;
        selected = context.selected_objects
        visible = context.visible_objects
        i = len(selected)
        print ("selected count:", i)
        print (selected[0].type)
        
        proxymat = None
        if (selected[0].name.endswith('boneGeometry')):
            proxymat = selected[0].data.materials[0]
        
        geombones = (x for x in visible if x.name.endswith('boneGeometry'))
        
        for ob in geombones:
            if ob.data.materials:
                ob.data.materials[0] = proxymat
                #print ("change mat")
            else:
                ob.data.materials.append(proxymat)
                #print ("add material")    
                                                          
    def execute(self, context):
        self.PropagateBoxColliders(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(BoneBoxPropagate.bl_idname)

def register():
    bpy.utils.register_class(BoneBoxPropagate)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(BoneBoxPropagate)