#! /usr/bin/env python3

import rclpy
import cv2
import numpy as np
from rclpy.node import Node
from std_msgs.msg import String
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

class ImageShow(Node) :
    def __init__(self) :
        super().__init__('image_show')
        self.image_sub = self.create_subscription(Image, 'image_raw',self.callback, 10)
        self.image_pub = self.create_publisher(Image, 'show_image', 10)
        self.bridge = CvBridge()
    
    def callback(self, data) :
        try:
            cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        except CvBridgeError as e:
            print(e)
            
        shape = cv_image.shape
        x_max = shape[1]
        y_max = shape[0]
        
        cv2.line(cv_image, pt1=(int(x_max / 2), 0), pt2=(int(x_max / 2), y_max), color=(255,255,255), thickness=1, lineType=cv2.LINE_4)
        cv2.line(cv_image, pt1=(0, int(y_max / 2)), pt2=(x_max, int(y_max / 2)), color=(255,255,255), thickness=1, lineType=cv2.LINE_4)
        
        try:
            self.image_pub.publish(self.bridge.cv2_to_imgmsg(cv_image, 'bgr8'))
        except CvBridgeError as e:
            print(e)
        
        

def main():
    try:
        rclpy.init()
        images = ImageShow()
        rclpy.spin(images)
        images.destroy_node()
        rclpy.shutdown()
    except KeyboardInterrupt as e:
        print('\nShutting down')
        cv2.destroyAllWindows()

if __name__ == '__main__':
    main()
