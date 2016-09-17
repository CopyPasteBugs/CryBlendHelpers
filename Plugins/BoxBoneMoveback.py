bl_info = {
    "name": "Moveback proxies for Skeletons for CryEngine 5",
    "author": "ArticLion",
    "category": "Object",
    "blender": (2, 77, 0)   
}

import bpy
import os
import struct
import sys
import mathutils
import math
from math import radians
from bpy.props import (BoolProperty)
from bpy.props import (EnumProperty)
from bpy.props import (FloatProperty)



          
class BoneBoxMoveback(bpy.types.Operator):
    bl_idname = "object.boneboxmoveback"   # unique identifier for buttons and menu items to reference.
    bl_label = "CryHelpers : Moveback _boneGeometry"     # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    
    
    def MovebackBoxColliders(self, context):
        scene = context.scene;
        selected = context.selected_objects
        #i = len(selected)
        #print ("selected count:", i)
        #print (selected[0].type)
        
        arma = next((x for x in selected if x.type == 'ARMATURE'), None)
        #geombones = (x for x in selected if x.name.endswith('boneGeometry'))
        
        #if (arma is not None):
        #    print ("find arma in selected: " + arma.data.name)
            
        #for x in geombones:
        #    print ("find geombone in selected: " + x.name)
        if (arma is not None):   
            for bone in arma.data.bones:
                #print ("bone" + bone.name)
                geomToMove = next((x for x in selected if x.name.startswith(bone.name)), None)
                if (geomToMove is not None):
                    geomToMove.rotation_euler = (0.0,0.0,0.0)
                    geomToMove.scale = (1.0,1.0,1.0)
                    geomToMove.location = bone.head_local
            
        pass   
                                          
    def execute(self, context):
        self.MovebackBoxColliders(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(BoneBoxMoveback.bl_idname)

def register():
    bpy.utils.register_class(BoneBoxMoveback)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(BoneBoxMoveback)