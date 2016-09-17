bl_info = {
    "name": "Create Box proxies for Skeletons for CryEngine 5",
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



          
class BoneBox(bpy.types.Operator):
    bl_idname = "object.bonebox"   # unique identifier for buttons and menu items to reference.
    bl_label = "CryHelpers : Create basic _boneGeometry"     # display name in the interface.
    bl_options = {'REGISTER', 'UNDO'}  # enable undo for the operator.
    
    
    def CreateBoxColliders(self, context):
        scene = context.scene;
        selected = context.selected_objects
        i = len(selected)
        print ("selected count:", i)
        print (selected[0].type)
        if (selected[0].type == 'ARMATURE'):
            #print ("This is ARMA with 300 bones!")
            for bone in selected[0].data.bones:
                armature = selected[0]
                self.CreateColliderForBone(context, armature, bone)    
            
    def CreateColliderForBone(self, context, arm, bone):
        #print ("bone name" + bone.name)
        self.CreateNewBox(context, bone.name, bone.head_local, bone, arm)
        pass
    
    def CreateNewBox(self, context, name, origin,bone, arm):
        distance = (bone.head - bone.tail).length
        #print ("distance {0}".format(distance))
        bpy.ops.mesh.primitive_cube_add(
                                radius=0.15 * distance, 
                                calc_uvs=True, 
                                view_align=False, 
                                enter_editmode=False, 
                                location= bone.head_local, 
                                rotation=(0.0, 0.0, 0.0))
                                
        #location=(bone.head - bone.tail) * bone.matrix,
        #location= bone.head_local, 
        ob = bpy.context.object
        ob.name = name + "_boneGeometry"
        ob.show_name = True
        me = ob.data
        me.name = name
        
        #parenting produce wrong mesh orient on export
        #ob.parent = arm
        #ob.parent_bone = bone.name
        #ob.parent_type = 'BONE'
        
        #Apply rot & scale for box
        bpy.ops.object.select_all(action='DESELECT')
        ob.select  = True
        bpy.ops.object.transform_apply(location=False, rotation=True, scale=True)
        bpy.ops.object.select_all(action='DESELECT')
        
        #so we unparent now
        #ob.parent = None
        #ob.parent_bone = ''
        #ob.parent_type = 'OBJECT'
        
        
                                 
    def execute(self, context):
        self.CreateBoxColliders(context)
        return {'FINISHED'}

def menu_func(self, context):
    self.layout.operator(BoneBox.bl_idname)

def register():
    bpy.utils.register_class(BoneBox)
    bpy.types.VIEW3D_MT_object.append(menu_func)
    
def unregister():
    bpy.utils.unregister_class(BoneBox)