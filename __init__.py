bl_info = {
	"name": ".sls exporter",
	"author": "Massinissa Mokhtari",
	"category": "Import-Export",
	"version": (0, 0, 1),
	"blender": (2, 77, 0),
	"location": "File > Export > Export to SLS",
    "description": ".SLS exporter for Blender",
    "wiki_url": "https://github.com/massile/sls-blender-exporter",
    "category": "Import-Export"
}

import bpy
from . import operator

def register():
	bpy.utils.register_class(operator.Exporter)

def unregister():
	bpy.utils.unregister_class(operator.Exporter)
