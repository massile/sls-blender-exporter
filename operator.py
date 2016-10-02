import bpy

class Exporter(bpy.types.Operator):
	bl_label = 'Export to .sls'
	bl_idname = 'export.sls'
	
	def execute(self, context):
		self.report({'INFO'}, 'This works !')
		return {'FINISHED'}
