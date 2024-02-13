bl_info = {
    "name" : "AddonsPacker",
    "description": "For internal use only",
    "author" : "Vladislav Ciocoi",
    "blender" : (2, 90, 0),
    "version" : (1, 0, 0),
    "location": "3D View > Tools",
    "category": "Development"
}

if 'bpy' not in locals():
    import bpy
    from bpy.props import PointerProperty
    from . import operators
    from . import properties
    from . import sidepanel
    from . import prefs
else:
    import imp
    imp.reload(operators)
    imp.reload(properties)
    imp.reload(sidepanel)
    imp.reload(prefs)

classes = (
    properties.AP_Properties,
    operators.BuildAddon,
    prefs.AP_Prefs,
    sidepanel.SidePanel
)

def register():
    from bpy.utils import register_class

    for cls in classes:
        register_class(cls)

    bpy.types.Scene.addon_packer_props = PointerProperty(type=properties.AP_Properties)

def unregister():
    from bpy.utils import unregister_class

    for cls in reversed(classes):
        unregister_class(cls)

    del bpy.types.Scene.addon_packer_props
