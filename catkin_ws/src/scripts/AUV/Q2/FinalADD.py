#!/usr/bin/env python3
import rospy
from std_msgs.msg import Int32

def callback(msg):
    rospy.loginfo(f"received {msg.data}")
    output = Int32()
    output.data = msg.data+5
    rospy.loginfo(f"Final result :- {output.data}")

    
if __name__ == "__main__":
    rospy.init_node("add5")
    rospy.loginfo("resultnode started")
    sub2 = rospy.Subscriber("Multiply10",Int32,callback)
    rospy.spin()


