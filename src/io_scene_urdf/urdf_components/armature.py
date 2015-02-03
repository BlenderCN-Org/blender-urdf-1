import bpy, math
from mathutils import Vector, Matrix, Euler
import copy
from io_scene_urdf.urdf_components.joint import URDFJoint
from io_scene_urdf.urdf_components.link import URDFLink
class URDFArmature:

    def __init__(self, urdf):


        self.name = urdf.name
        self.urdf = urdf
        self.links = []
        self.joints = []
        # Lists of bones 
        #self.roots = self._walk_urdf(self.urdf.link_map[urdf.get_root()])
        


    def _walk_urdf(self, link, parent_bone = None):
        ''' Recursively build up bone structure starting from base link
        Input: parent_link, parent_bone
        Output: List of URDFJoints (bones) defined by the joint and its child_link
        (A bone is made up of a joint and its child_link)
        '''
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
        ''' Find joint and child link of the provided link
        Input: link <Type: URDFLink>
        Output: (joint, child_link) (<Type: URDFJoint>, <Type: URDFLink>)
        '''
        joints = [joint for joint in self.urdf.joints if joint.parent == link.name]
        return [(joint, self.urdf.link_map[joint.child]) for joint in joints]


    def build(self):
        # # Create armature and object
        # bpy.ops.object.add(
        #     type='ARMATURE', 
        #     enter_editmode=True,
        #     location=(0,0,0))
        # ob = bpy.context.object
        # ob.show_x_ray = True
        # ob.name = self.name
        # amt = ob.data
        # amt.name = self.name+'_armature'
        # amt.show_axes = True

        # bpy.ops.object.mode_set(mode='EDIT')
        # for root in self.roots:
        #     root.build_editmode(ob)

        # bpy.ops.object.mode_set(mode='OBJECT')
        # for root in self.roots:
        #     root.build_objectmode(ob)
        for link in self.urdf.links:
            self.links.append(URDFLink(link))

