bl_info = {
    "name": "Meebit (.vox)",
    "author": "Dagfinn Parnas based on technistguru/MagicaVoxel_Importer",
    "version": (0, 8, 0),
    "blender": (2, 80, 0),
    "location": "File > Import-Export",
    "description": "Import Meebit from .vox file",
    "warning": "",
    "wiki_url": "",
    "support": 'TESTING',
    "category": "Import-Export"}


if "bpy" in locals():
    import importlib
    if "meebit_core" in locals():
        importlib.reload(meebit_core)


# Responsibility
# - Defines a python package
# - Registers the ImportMeebit via register()
# - ImportMeebit defines the user interface of the import and the user exposed options
# - ImportMeebit.execute() triggers the import through meebit_core.import



import os

import bpy
import bmesh
from bpy_extras.io_utils import ImportHelper
from bpy.props import StringProperty, IntProperty, FloatProperty, BoolProperty, CollectionProperty, EnumProperty
from bpy.types import Operator

import struct

"""
This imports Meebits VOX files to Blender.

It uses code from the following repo under gpl 3.0 license.
https://github.com/technistguru/MagicaVoxel_Importer

Vox file format:
https://github.com/ephtracy/voxel-model/blob/master/MagicaVoxel-file-format-vox.txt
https://github.com/ephtracy/voxel-model/blob/master/MagicaVoxel-file-format-vox-extension.txt

Usage:
Import add-on via Edit-Preferences
Run from "File->Import" menu and then select meebit .vox file
"""
class ImportMeebit(Operator, ImportHelper):
    bl_idname = "import_meebit.vox"
    bl_label = "Import meebit"
    bl_options = {'PRESET', 'UNDO'}
    
    files: CollectionProperty(name="File Path",
                              description="File path used for importing the meebit .vox file",
                              type=bpy.types.OperatorFileListElement) 

    directory: StringProperty()
    
    filename_ext = ".vox"
    filter_glob: StringProperty(
        default="*.vox",
        options={'HIDDEN'},
    )

    voxel_size: FloatProperty(name = "Voxel Size",
                                description = "Side length, in blender units, of each voxel.",
                                default=0.025)
    
    material_type: EnumProperty(name = "",
                                description = "How color and material data is imported",
                                items = (
                                    ('None', 'None', "Don't import palette."),
                                    ('SepMat', 'Separate Materials', "Create a material for each palette color."),
                                    ('VertCol', 'Vertex Colors', "Create one material and store color and material data in vertex colors."),
                                    ('Tex', 'Textures', "Generates textures to store color and material data.")
                                ),
                                default = 'Tex')

    gamma_correct: BoolProperty(name = "Gamma Correct Colors",
                                description = "Changes the gamma of colors to look closer to how they look in MagicaVoxel. Only applies if Palette Import Method is Seperate Materials.",
                                default = True)
    gamma_value: FloatProperty(name = "Gamma Correction Value",
                                default=2.2, min=0)
    
    override_materials: BoolProperty(name = "Override Existing Materials", default = False)
    
    cleanup_mesh: BoolProperty(name = "Cleanup Mesh",
                                description = "Merge overlapping verticies and recalculate normals.",
                                default = True)
    
    create_lights: BoolProperty(name = "Add Point Lights",
                                description = "Add point lights at emissive voxels for Eevee.",
                                default = False)
    
    join_meebit_armature: BoolProperty(name = "Rig with Meebit armature",
                            description = "Rig if there exist an armature with name 'MeebitArmature'",
                            default = True)

    scale_meebit_armature: BoolProperty(name = "Scale Meebit armature to fit",
                            description = "Scale armature dimension to fit meebit dimensions",
                            default = True)                            

    #todo
    create_volume: BoolProperty(name = "Generate Volumes",
                                description = "Create volume objects for volumetric voxels.",
                                default = False)
    
    organize: BoolProperty(name = "Organize Objects",
                            description = "Organize objects into collections.",
                            default = True)
    

    def execute(self, context):
        from . import meebit_core

        paths = [os.path.join(self.directory, name.name) for name in self.files]
        if not paths:
            paths.append(self.filepath)
        
        # Must be in object mode
        try:
            bpy.ops.object.mode_set(mode='OBJECT')
        except:
            print("Failed to set object mode. Continuing")
            pass
        

        for path in paths:
            meebit_core.import_meebit_vox(path, self)
        
        return {"FINISHED"}
    
    def draw(self, context):
        layout = self.layout
        
        layout.prop(self, "voxel_size")
        
        material_type = layout.column(align=True)
        material_type.label(text = "Palette Import Method:")
        material_type.prop(self, "material_type")
        
        if self.material_type == 'SepMat':
            layout.prop(self, "gamma_correct")
            if self.gamma_correct:
                layout.prop(self, "gamma_value")
        if self.material_type != 'None':
            layout.prop(self, "override_materials")
        
        layout.prop(self, "cleanup_mesh")
        layout.prop(self, "create_lights")
        layout.prop(self, "organize")
        layout.prop(self, "join_meebit_armature")
        layout.prop(self, "scale_meebit_armature")
        #layout.prop(self, "create_volume")
        


def menu_func_import(self, context):
    self.layout.operator(ImportMeebit.bl_idname, text="Meebit (.vox)")

def register():
    bpy.utils.register_class(ImportMeebit)
    bpy.types.TOPBAR_MT_file_import.append(menu_func_import)

def unregister():
    bpy.utils.unregister_class(ImportMeebit)
    bpy.types.TOPBAR_MT_file_import.remove(menu_func_import)


if __name__ == "__main__":
    register()        