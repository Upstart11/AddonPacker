from bpy.props import (BoolProperty,
                       StringProperty
                       )

from bpy.types import PropertyGroup

class AP_Properties(PropertyGroup):
    obj_use_smooth_groups : BoolProperty(
    name="Smooth Groups",
    description="Surround smooth groups by sharp edges",
    default = True
    )
    addons_folder : StringProperty(
    name="Addons Folder",
    description="Folder where your addon folder are located",
    subtype='FILE_PATH'
    )