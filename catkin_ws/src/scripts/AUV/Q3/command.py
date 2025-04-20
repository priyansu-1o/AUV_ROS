#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":
    rospy.init_node("command")
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(5)
    
    while not rospy.is_shutdown():
        try:
            msg = input("Enter command (FORWARD/BACKWARD/LEFT/RIGHT/STOP): ").strip().upper()
            cmd = Twist()
            
            if msg == 'FORWARD':
                cmd.linear.x = 1.0
                print('bot_direction = EAST')
            elif msg == 'BACKWARD':
                cmd.linear.x = -1.0
                print('bot_direction = WEST')
            elif msg == 'LEFT':
                cmd.angular.z = 1.0
                print('bot_direction = NORTH')
            elif msg == 'RIGHT':
                cmd.angular.z = -1.0
                print('bot_direction = SOUTH')
            elif msg == 'STOP':
                cmd.linear.x = 0.0
                cmd.angular.z = 0.0
                print('bot_direction = STOPPED')
            else:
                print("Invalid command!")
                continue
                
            pub.publish(cmd)
            rate.sleep()
            
        except (KeyboardInterrupt, EOFError):
            break