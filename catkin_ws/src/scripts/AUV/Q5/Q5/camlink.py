import rospy
import depthai as dai
from sensor_msgs.msg import Image
from cv_bridge import CvBridge

class camlink:
    def init(self):
        rospy.init_node("edge_detector")
        self.bridge = CvBridge()
        self.pub = rospy.Publisher('edge_image', Image, queue_size=10)

        self.pipeline = dai.Pipeline()     
        mono = self.pipeline.createMonoCamera()
        mono.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
        mono.setFps(30)
        mono.setBoardSocket(dai.CameraBoardSocket.LEFT)

        xout = self.pipeline.create(dai.node.XLinkOut)
        xout.setStreamName("monoleft")  
        mono.out.link(xout.input)

        self.device = dai.Device(self.pipeline)
    
    def getframes(self):
        queue = self.device.getOutputQueue(name="edges", maxSize=4)
        while not rospy.is_shutdown():
            inFrame = queue.get()
            frame = inFrame.getCvFrame()
            
            ros_image = self.bridge.cv2_to_imgmsg(frame, "monoleft")
            self.pub.publish(ros_image)

    def run(self):
        try:
            self.getframes()
        except:
            rospy.ROSInterruptException()
            self.device.close()


if __name__ == "__main__":
    newobj = camlink()
    newobj.run()


