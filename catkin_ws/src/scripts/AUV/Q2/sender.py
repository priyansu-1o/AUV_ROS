#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32  

if __name__ == "__main__":
    rospy.init_node("Sender")

    rospy.loginfo("Sender started")
    setnumber = rospy.Publisher("sending2mul",Int32,queue_size = 10)
    rate = rospy.Rate(2)
    count = 1
    while not rospy.is_shutdown():
        setnumber.publish(2*count)
        rospy.loginfo(f"published : {2*count}")
        count+=1
        rate.sleep()
