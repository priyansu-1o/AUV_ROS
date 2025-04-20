#!/usr/bin/env python3
import rospy
from std_msgs.msg import String

user=""

def callback(msg):
    global user
    if not msg.data.startswith(f"[{user}]"):
        print(msg.data)

def chat():
    global user
    rospy.init_node('chat',anonymous=True)
    user=input("Enter you name : ")

    pub=rospy.Publisher('chatter',String,queue_size=10)
    rospy.Subscriber('chatter',String,callback)

    rate=rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            msg=input(f"{user} : ")
            format_msg=f"[{user}] : {msg}"
            pub.publish(String(format_msg))
            rate.sleep()

        except rospy.ROSInterruptException:
            pass
        except:
            break

if __name__=='main_':
    chat()
