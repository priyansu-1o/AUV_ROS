#!/usr/bin/env python3

import rospy
from std_msgs.msg import Int32

pub = None
def callback(msg):
    rospy.loginfo(f"Received: {msg.data}")
    result = Int32()
    result.data = msg.data * 10
    pub.publish(result)
    rospy.loginfo(f"Published: {result.data}")

if __name__ == '__main__':
    rospy.init_node("Multiplier")
    receiver1 = rospy.Subscriber("sending2mul",Int32,callback)
    rospy.loginfo("receiver started")
    pub = rospy.Publisher("Multiply10",Int32,queue_size=10)
    rospy.loginfo("pub1 started")
    rospy.spin()
