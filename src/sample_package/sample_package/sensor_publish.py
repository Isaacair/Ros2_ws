from std_msgs.msg import Float32MultiArray
import rclpy 
from rclpy.node import Node

class SensorPublisherNode(Node):
    def __init__(self):
    	super().__init__('sen_publisher')
    	self.senpublisher=self.create_publisher(Float32MultiArray,'sensortopic',10)
    	self.create_timer(0.5,self.publishfunc)
    	
    def publishfunc(self):
    
    	lmsg=Float32MultiArray()
    	lmsg.data=[696.0,1252.0,1321.0,1321.0,2431.0]
    	self.senpublisher.publish(lmsg)
        
    		


def main(args=None):
    rclpy.init(args=args)
    sensorpublisher= SensorPublisherNode()
    rclpy.spin(sensorpublisher)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
