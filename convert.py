from .dataTypes import Skeleton, Joint, SlsMesh

def fromBonesToJoints(bone, parentJoint = None, joints = []):
	# To clear the joints parameter when the script is called more than once
	if not parentJoint:
		joints = []

	joint = Joint(len(joints), bone.name, bone.matrix_local, parentJoint)
	joints.append(joint)

	for child in bone.children:
		fromBonesToJoints(child, joint, joints)

	return joints

def fromArmatureToSkeleton(armature):
	rootBone = next(bone for bone in armature.data.bones if not bone.parent)
	joints = fromBonesToJoints(rootBone)

	return Skeleton(armature.name, joints)

def fromMeshToSlsMesh(mesh):
	return SlsMesh(mesh.name, [], [], [])
