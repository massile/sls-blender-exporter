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
        jointsStr = ''.join([joint.toSls() for joint in self.joints])
        return \
"""
skeleton:
  name: %s
  joints: %s
""" % (self.name, jointsStr)
