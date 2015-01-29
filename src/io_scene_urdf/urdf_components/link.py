import bpy, math
from mathutils import Vector, Matrix, Euler
import copy
class URDFLink:

    def __init__(self, urdf_link):

        self.name = urdf_link.name
        print('DEBUG:::::::::::::::::::' + self.name)

        self.inertial = urdf_link.inertial
        self.visual = urdf_link.visual
        self.collision = urdf_link.collision

        self._get_origin()

        print("Link %s at %s" % (self.name, self.xyz))

    def _get_origin(self):
        """ Links do not define proper origin. We still try to extract one
        to correctly place the bones' tails when necessary (like, when a bone
        is not connected to any other child bone).
        """
        xyz = (0,0,0)
        rpy = None

        if self.inertial:
            xyz = self.inertial.origin.xyz
            rpy = self.inertial.origin.rpy
        elif self.collision:
            xyz = self.collision.origin.xyz
            rpy = self.collision.origin.rpy
        elif self.visual:
            xyz = self.visual.origin.xyz
            rpy = self.visual.origin.rpy

        self.xyz = Vector(xyz)
        if rpy:
            self.rot = Euler(rpy, 'XYZ').to_quaternion()
        else:
            self.rot = Euler((0,0,0)).to_quaternion()
