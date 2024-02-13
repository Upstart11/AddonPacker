from bpy.types import AddonPreferences

class AP_Prefs(AddonPreferences):

    bl_idname = __name__


    def draw(self, context):
        layout = self.layout
        scene = context.scene
        APProps = scene.addon_packer_props

        
        layout.label(text='Addons Folder Path:')
        layout.prop(APProps, "addons_folder")
