import bpy, math
from mathutils import Vector, Matrix, Euler
import copy
from urdf_components.joint import URDFJoint

class URDFArmature:

    def __init__(self, name, urdf):


        self.name = name
        self.urdf = urdf

        self.roots = self._walk_urdf(self.urdf.link_map[urdf.get_root()])
        print('DEBUG:::::::::::::::::::' + self.name)


    def _walk_urdf(self, link, parent_bone = None):

        bones = []
        for joint, child_link in self._get_urdf_connections(link):
            if parent_bone:
                # be careful: if joint is a zero-length joint,
                # it gets merged into parent bone (because Blender does not
                # support 0-length joints)! so bone and parent_bone
                # may be equal.
                bone = parent_bone.add_child(joint, child_link)
            else:
                bone = URDFJoint(joint, child_link)

            self._walk_urdf(child_link, bone)
            bones.append(bone)
        return bones

    def _get_urdf_connections(self, link):
        ''' 

        '''
        joints = [joint for joint in self.urdf.joints if joint.parent == link.name]
        return [(joint, self.urdf.link_map[joint.child]) for joint in joints]


    def build(self):
        # Create armature and object
        bpy.ops.object.add(
            type='ARMATURE', 
            enter_editmode=True,
            location=(0,0,0))
        ob = bpy.context.object
        ob.show_x_ray = True
        ob.name = self.name
        amt = ob.data
        amt.name = self.name+'_armature'
        amt.show_axes = True

        bpy.ops.object.mode_set(mode='EDIT')
        for root in self.roots:
            root.build_editmode(ob)

        bpy.ops.object.mode_set(mode='OBJECT')
        for root in self.roots:
            root.build_objectmode(ob)