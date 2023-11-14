import pickle
import rclpy
from std_msgs.msg import Float32MultiArray
from example_interfaces.msg import Int64
from std_msgs.msg import String
from rclpy.node import Node
import os
from statistics import mode

class SensorsubNode(Node):
    def __init__(self):
        super().__init__('subscribernode')
        self.subscriber=self.create_subscription(Float32MultiArray,'sensortopic',self.sensorcallback,10)
        self.fan_publisher=self.create_publisher(Int64,'fan_topic',10)
        models_dir = os.path.join(os.getcwd(), 'models')  
        model_file = os.path.join(models_dir, 'final_model.pkl')
        
        with open(model_file, 'rb') as f:
            self.model = pickle.load(f)
       
        
    def sensorcallback(self,message):
        speeds={1:10,2:20,3:30,4:40}
        self.arr=[]
        l=[list(map(int,message.data))]
        output=self.model.predict(l)[0]
        if len(self.arr)<=9:
            self.arr.append(output)
        else:
            self.arr.append(output)
            self.arr.pop(0) 
            
        d=Int64()
        d.data=int(speeds[mode(self.arr)])
        self.fan_publisher.publish(d)
        self.get_logger().info(str(d.data))

        
def main(args=None):
    rclpy.init(args=args)
    sensorsubscriber= SensorsubNode()
    rclpy.spin(sensorsubscriber)
    rclpy.shutdown()

if __name__ == '__main__':
    main()
