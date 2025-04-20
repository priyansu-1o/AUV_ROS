#!/usr/bin/env python

import rospy
import threading
from std_msgs.msg import String

class Node:
    def __init__(self):
        rospy.init_node('simple_terminal_node')
        self.pub = rospy.Publisher('terminal_inputs', String, queue_size=10)
        self.running = True

    def read_input(self, str):
        while self.running:
            try:
                text = input(f"{str}> ")
                if text.lower() == 'quit':
                    self.running = False
                    rospy.signal_shutdown("User exit")
                    break
                self.pub.publish(f"{str}:{text}")
            
            except (KeyboardInterrupt, EOFError):
                self.running = False
                break

    def run(self):
        threads = [
            threading.Thread(target=self.read_input, args=('Joestar',)),
            threading.Thread(target=self.read_input, args=('Jolyne',))
        ]
        for t in threads: 
            t.start()
        
        rospy.spin()
        
        for t in threads: 
            t.join()

if __name__ == '__main__':
    node = Node()
    node.run()