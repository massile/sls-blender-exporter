import bpy
from . import convert

def export(report, filename):
	file = open(filename, 'w')

	armature = next(obj for obj in bpy.context.selected_objects if obj.type == 'ARMATURE')
	skeleton = convert.fromArmatureToSkeleton(armature)

	file.write(skeleton.toSls())
	file.close()
