import bpy, math
from mathutils import Vector, Matrix, Euler
import copy
from io_scene_urdf.urdf_components.link import URDFLink
class URDFJoint:

    # cf urdf_parser_py.urdf.Joint.TYPES
    FIXED = "fixed"
    PRISMATIC = "prismatic"
    REVOLUTE = "revolute"

    def __init__(self, urdf_joint, urdf):
        '''
        Initilize an instance of URDFJoint with 
            urdf_joint: joint data parsed from the .urdf file, type: list
            urdf: result from parsed URDF file
        '''
        self.urdf = urdf
        self.name = urdf_joint.name
        self.type = urdf_joint.type

        # If origin information is available
        if urdf_joint.origin:
            self.xyz = Vector(urdf_joint.origin.xyz)
            if urdf_joint.origin.rpy:
                self.rot = Euler(urdf_joint.origin.rpy, 'XYZ').to_quaternion()
            else:
                self.rot = Euler((0, 0, 0)).to_quaternion()
        else:
            self.xyz = Vector(0,0,0)
            self.rot = Euler((0, 0, 0)).to_quaternion()

        self.parent = None
        self.child = None

        self._add_parent(urdf_joint)
        self._add_child(urdf_joint)
        
        print('Joint ' + self.name + ' has PARENT = ' + self.parent.name + ' and CHILD = ' +self.child.name)
        
    def _add_parent(self, urdf_joint):
        '''
        Find joint's parent link 
        '''
        if urdf_joint.parent:
            for link in self.urdf.links:            
                if link.name == urdf_joint.parent:
                    print('Found parent link of joint ' + self.name)
                    self.parent = self.urdf.link_map[urdf_joint.parent]
                else:
                    pass
        else:
            print('Invalid URDF file, joint ' + self.name + ' has no parent')
        if self.parent == None:
            print('Invalid URDF file, couldn not find link ' + link.name + ' that is parent of joint ' + self.name)
        
    def _add_child(self, urdf_joint):
        '''
        Find joint's child link 
        '''
        if urdf_joint.child:
            for link in self.urdf.links:
                if link.name == urdf_joint.child:
                    self.child = self.urdf.link_map[urdf_joint.child]
                    print('Found child link of joint ' + self.name)
                else:
                    pass
        else:
            print('Invalid URDF file, joint ' + self.name + ' has no child')
        if self.child == None:
            print('Invalid URDF file, couldn not find link ' + link.name + ' that is child of joint ' + self.name)




