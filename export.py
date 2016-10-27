import bpy
from . import convert

def export(report, filename):
	file = open(filename, 'w')

	armature = next(obj for obj in bpy.context.selected_objects if obj.type == 'ARMATURE')
	skeleton = convert.fromArmatureToSkeleton(armature)

	mesh = next(obj for obj in bpy.context.selected_objects if obj.type == 'MESH')
	slsMesh = convert.fromMeshToSlsMesh(mesh)

	file.write(skeleton.toSls())
	file.write(slsMesh.toSls())
	file.close()
