from os import listdir
import bpy
import os

class SidePanel(bpy.types.Panel):
    bl_label = "AddonPacker"
    bl_idname = "AP_main_panel"
    bl_space_type = "VIEW_3D"   
    bl_region_type = "UI"
    bl_category = "Addons Packer"
    bl_context = "objectmode"   


    @classmethod
    def poll(self,context):
        return context.object is not None

    def draw(self, context):
        layout = self.layout
        scene = context.scene
        props = scene.addon_packer_props
        directory_path = props.addons_folder

        layout.separator()
        row = layout.row()

        row.prop(props, 'addons_folder')
        row = layout.row()
        box = row.box()
        boxrow = box.row()
        folders = listdir(directory_path)
        for folder_name in folders:
            if os.path.isdir(os.path.join(directory_path, folder_name)) and folder_name != "PackedFiles":
                boxrow = box.row()
                boxrow.operator("build.addon", text = folder_name).zip_name=folder_name
