import rclpy
from rclpy.node import Node
from example_interfaces.msg import Int64
class fan_sub_node(Node):
    def __init__(self):
        super().__init__('fan_subscriber')
        self.subscriber=self.create_subscription(Int64,'fan_topic',self.fan_callback,10)
       
       
        
    def fan_callback(self,message):
        out=str(message.data)
        self.get_logger().info(out)

        
def main(args=None):
    rclpy.init(args=args)
    fansubscriber= fan_sub_node()
    rclpy.spin(fansubscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()