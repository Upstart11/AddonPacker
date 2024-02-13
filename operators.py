import os
import shutil
import bpy
from bpy.props import StringProperty

from bpy.types import Operator

class BuildAddon(Operator):
    bl_label = "Build Addon"
    bl_idname = "build.addon"
    bl_options = {'UNDO'}

    zip_name: StringProperty(name="zip_name")

    def execute(self, context):
        props = context.scene.addon_packer_props
        folders_dir = props.addons_folder
        packed_folder_path = os.path.join(folders_dir, "PackedFiles")
        if not os.path.isdir(packed_folder_path):
             os.mkdir(packed_folder_path)
        addon_name = self.zip_name
        addon_archive = addon_name + ".zip"
        existing_zips = os.listdir(packed_folder_path)
        for zip_name in existing_zips:
            if zip_name == addon_archive:
                os.remove(os.path.join(packed_folder_path, zip_name))
        zip_path = os.path.join(packed_folder_path, addon_name)
        shutil.make_archive(zip_path, "zip", root_dir = folders_dir, base_dir = addon_name)
        bpy.ops.preferences.addon_install(overwrite=True, target='DEFAULT', filepath=zip_path +".zip", filter_folder=False, filter_python=True, filter_glob="*.py;*.zip")
        bpy.ops.preferences.addon_enable(module = addon_name)
        
        return {'FINISHED'}