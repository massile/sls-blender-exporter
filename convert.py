from .dataTypes import *

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
    mesh.data.update(calc_tessface=True)

    verts = mesh.data.vertices
    faces = [f for f in mesh.data.polygons]

    slsVertices = []

    vertexLength = 0
    for face in faces:
        for i, _ in enumerate(face.vertices):
            vertexId = face.vertices[i]
            vertexFace = verts[vertexId]
            sumWeights = sum([group.weight for group in vertexFace.groups])

            vertex  = Vertex(vertexLength, WeightVert(0,0))
            vertexLength += 1
            slsVertices.append(vertex)

    return SlsMesh(mesh.name, slsVertices, [], [])
