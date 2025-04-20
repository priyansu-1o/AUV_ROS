#!/usr/bin/env python3

import rospy
from turtlesim.msg import Pose

def pose_callback(msg):
    rospy.loginfo(f"Turtle Pose - x: {msg.x:.2f}, y: {msg.y:.2f}, theta: {msg.theta:.2f}")

def turtle_pose_subscriber():
    rospy.init_node("pose_subscriber")
    rospy.Subscriber("/turtle1/pose", Pose, pose_callback)
    rospy.loginfo("Subscriber node started")
    rospy.spin()

if __name__ == "__main__":
    turtle_pose_subscriber()