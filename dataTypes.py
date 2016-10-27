def listToSls(array):
    return ''.join([element.toSls() for element in array])

class Joint:
    def __init__(self, index, name, matrix, parent):
        self.index = index
        self.name = name
        self.matrix = matrix
        self.parent = parent

    def toSls(self):
        quat = self.matrix.to_quaternion()
        pos = self.matrix.col[3]
        return \
"""
  - index: %i
    parent: %i
    name: %s
    orientation: %f %f %f %f
    position: %f %f %f
""" % (self.index,
       self.parent.index if self.parent else -1,
       self.name,
       quat.x, quat.y, quat.z, quat.w,
       pos[0], pos[1], pos[2])

class Skeleton:
    def __init__(self, name, joints):
        self.name = name
        self.joints = joints

    def toSls(self):
        jointsStr = listToSls(self.joints)
        return \
"""
skeleton:
  name: %s
  joints: %s
""" % (self.name, jointsStr)

class WeightVert:
    def __init__(self, start, count):
        self.start = start
        self.count = count
    def toSls(self):
        return \
"""
      start: %s
      count: %s
""" % (self.start, self.count)

class Vertex:
    def __init__(self, index, weights):
        self.index = index
        self.weights = weights

    def toSls(self):
        weightsStr = listToSls(self.weights)
        return \
"""
  - index: %s
    weights: %s
""" % (self.index, weightsStr)

class Face:
    def __init__(self, id0, id1, id2):
        self.id0 = id0
        self.id1 = id1
        self.id2 = id2

    def toSls(self):
        return \
"""
  - indices: %s %s %s
""" % (self.id0, self.id1, self.id2)

class Weight:
    def __init__(self, joint, bias, position):
        self.joint = joint
        self.bias = bias
        self.position = position

    def toSls(self):
        return \
"""
  - joint: %s
    bias: %s
    position: %s %s %s
""" % (self.joint,
       self.bias,
       self.position.x, self.position.y, self.position.z)

class SlsMesh:
    def __init__(self, name, vertices, faces, weights):
        self.name = name
        self.vertices = vertices
        self.faces = faces
        self.weights = weights

    def toSls(self):
        verticesStr = listToSls(self.vertices)
        facesStr = listToSls(self.faces)
        weightsStr = listToSls(self.weights)
        return \
"""
mesh:
  name: %s
  vertices: %s
  faces: %s
  weights: %s
""" % (self.name, verticesStr, facesStr, weightsStr)
