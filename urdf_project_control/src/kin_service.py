#!/usr/bin/env python

from urdf_project_control.srv import *
import rospy
import time
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list



class groupService:

	def __init__(self):
		rospy.init_node('urdf_project_commander')
		moveit_commander.roscpp_initialize(sys.argv)

		self.robot=moveit_commander.RobotCommander()
		self.scene =moveit_commander.PlanningSceneInterface()
		self.front_left_leg =moveit_commander.MoveGroupCommander("front_left_leg")
		self.rear_left_leg =moveit_commander.MoveGroupCommander("rear_left_leg")
		self.front_right_leg =moveit_commander.MoveGroupCommander("front_right_leg")
		self.rear_right_leg =moveit_commander.MoveGroupCommander("rear_right_leg")
		rospy.Service('kin_service', kin_service, self.handle_req)
		rospy.spin()


	def handle_req(self,req):
		try:
			print req
			command = req.movement
			#front
			self.front_left_leg.set_named_target("fl_forward")
			self.rear_left_leg.set_named_target("rl_forward")
			self.front_right_leg.set_named_target("fr_forward")
			self.rear_right_leg.set_named_target("rr_forward")

			count=0

			if(command.data == "front"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.rear_right_leg.set_named_target("rr_backward")
					self.front_right_leg.set_named_target("fr_forward")
					plan1a=self.rear_right_leg.plan()
					time.sleep(1)
					self.front_left_leg.set_named_target("fl_backward")
					self.rear_left_leg.set_named_target("rl_forward")
					plan2a=self.front_left_leg.plan()
					time.sleep(1)

					self.front_right_leg.set_named_target("fr_backward")
					self.rear_right_leg.set_named_target("rr_forward")	
					plan3a=self.front_right_leg.plan()
					time.sleep(1)
					self.rear_left_leg.set_named_target("rl_backward")
					self.front_left_leg.set_named_target("fl_forward")
					plan4a=self.rear_left_leg.plan()
					time.sleep(1)
					count+=1

				count=0
				rep=kin_serviceResponse()
				rep.res.data=True
				rep.message.data="Success"

			elif(command.data == "right"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                   moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.rear_right_leg.set_named_target("rr_right")
					self.front_right_leg.set_named_target("fr_backward")
					plan1a=self.rear_right_leg.plan()
					time.sleep(1)
					self.front_left_leg.set_named_target("fl_right")
					self.rear_left_leg.set_named_target("rl_backward")
					plan2a=self.front_left_leg.plan()
					time.sleep(1)

					self.front_right_leg.set_named_target("fr_right")
					self.rear_right_leg.set_named_target("rr_backward")	
					plan3a=self.front_right_leg.plan()
					time.sleep(1)
					self.rear_left_leg.set_named_target("rl_right")
					self.front_left_leg.set_named_target("fl_backward")
					plan4a=self.rear_left_leg.plan()
					time.sleep(1)
					count+=1
				count=0
				rep=controlResponse()
				rep.res.data=True
				rep.message.data="Success"

			elif(command.data == "back"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                 moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.rear_right_leg.set_named_target("rr_backward")
					self.front_right_leg.set_named_target("fr_forward")
					plan1a=self.rear_right_leg.plan()
					time.sleep(1)
					self.front_left_leg.set_named_target("fl_backward")
					self.rear_left_leg.set_named_target("rl_forward")
					plan2a=self.front_left_leg.plan()
					time.sleep(1)

					self.front_right_leg.set_named_target("fr_backward")
					self.rear_right_leg.set_named_target("rr_forward")	
					plan3a=self.front_right_leg.plan()
					time.sleep(1)
					self.rear_left_leg.set_named_target("rl_backward")
					self.front_left_leg.set_named_target("fl_forward")
					plan4a=self.rear_left_leg.plan()
					time.sleep(1)
					count+=1
				count=0
				rep=controlResponse()
				rep.res.data=True
				rep.message.data="Success"

			elif(command.data == "left"):
				display_trajectory_publisher = rospy.Publisher('/move_group/display_planned_path',
                                                 moveit_msgs.msg.DisplayTrajectory, queue_size=20)
				while(count<=5):
					self.rear_right_leg.set_named_target("rr_left")
					self.front_right_leg.set_named_target("fr_forward")
					plan1a=self.rear_right_leg.plan()
					time.sleep(1)
					self.front_left_leg.set_named_target("fl_left")
					self.rear_left_leg.set_named_target("rl_forward")
					plan2a=self.front_left_leg.plan()
					time.sleep(1)

					self.front_right_leg.set_named_target("fr_left")
					self.rear_right_leg.set_named_target("rr_forward")	
					plan3a=self.front_right_leg.plan()
					time.sleep(1)
					self.rear_left_leg.set_named_target("rl_left")
					self.front_left_leg.set_named_target("fl_forward")
					plan4a=self.rear_left_leg.plan()
					time.sleep(1)
				count=0
				rep=controlResponse()
				rep.res.data=True
				rep.message.data="Success"
			return rep

		except Exception as e:
			rep=kin_serviceResponse()
			print e
			return rep

if __name__ == "__main__":
	groupService()
