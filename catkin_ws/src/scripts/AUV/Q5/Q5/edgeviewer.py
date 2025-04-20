import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class subscriber:
    def init(self):
        rospy.init_node("Edge viewer")
        self.sub = rospy.Subscriber('edge_image', Image, self.image_callback)
        self.bridge = CvBridge()

    def image_callback(self,msg):
        try:
            cvimage = self.bridge.imgmsg_to_cv2(msg,"monoleft")
            cv2.imshow("edge detection",cvimage)
            cv2.waitKey(1)
        except Exception as e:
            rospy.logerr(e)

    def run(self):
        self.init()
        rospy.spin()
        cv2.destroyAllWindows()

if __name__ == '__main__':
    edgeviewer = subscriber()
    edgeviewer.run()

