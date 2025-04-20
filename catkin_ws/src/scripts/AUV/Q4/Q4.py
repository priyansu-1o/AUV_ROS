import depthai as dai
import cv2

pipeline = dai.Pipeline()

mono = pipeline.createMonoCamera()
mono.setResolution(dai.MonoCameraProperties.SensorResolution.THE_400_P)
mono.setFps(30)
mono.setBoardSocket(dai.CameraBoardSocket.LEFT)

xout = pipeline.create(dai.node.XLinkOut)
xout.setStreamName("monoleft")
mono.out.link(xout.input)

with dai.Device(pipeline) as device :
    queue = device.getOutputQueue(name="monoleft", maxSize=4)
    cv2.namedWindow("leftcam")
    while True:
            frame = queue.get() 
            leftframe = frame.getCvFrame()
            cv2.imshow("leftcam",leftframe)

            if cv2.waitKey(1) == 113:
                break
