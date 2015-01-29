############################################################################
#     Copyright (C) 2014 by Ralf Kaestner                                   #
#     ekyah411@gmail.com                                                    #
#                                                                           #
#                                                                           #  
#     IMPORT URDF FILE INTO BLENDER                                         #
#                                                                           #
#                                                                           #
#     This program is free software; you can redistribute it and#or modify  #
#     it under the terms of the GNU General Public License as published by  #
#     the Free Software Foundation; either version 2 of the License, or     #
#     (at your option) any later version.                                   #
#                                                                           #
#     This program is distributed in the hope that it will be useful,       #
#     but WITHOUT ANY WARRANTY; without even the implied warranty of        #
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the         #
#     GNU General Public License for more details.                          #
#                                                                           #
#     You should have received a copy of the GNU General Public License     #
#     along with this program; if not, write to the                         #
#     Free Software Foundation, Inc.,                                       #
#     59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.             #
#                                                                           #
#############################################################################
import bpy, math
from mathutils import Vector, Matrix, Euler
import copy
#from morse.builder import bpymorse
# roslib
# rospy
from io_scene_urdf.urdf_parser.urdf import URDF
from io_scene_urdf.urdf_components.armature import URDFArmature


def load(operator, context, filepath = ""):
	robot = URDF.from_xml_file(filepath)
	#print(filepath)
	print(robot)
	armature = URDFArmature("nao", robot)
	armature.build()
	print('finished')
	return {"FINISHED"}










	
