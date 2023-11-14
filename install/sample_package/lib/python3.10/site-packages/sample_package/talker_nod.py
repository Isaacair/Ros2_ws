import RPi.GPIO as GPIO
import time
import rclpy
from std_msgs.msg import Float64

def measure_distance(channel):
    start_time = time.time()
    while GPIO.input(ir_sensor_pin) == 0:
        pass
    while GPIO.input(ir_sensor_pin) == 1:
        pass
    duration = time.time() - start_time
    distance = duration * 17150  # Speed of sound (343 meters/second) * 100 (for cm) / 2
    distance = round(distance, 2)  # Round to two decimal places for simplicity
    msg = Float64()
    msg.data = distance  # Convert distance from cm to meters
    print(distance)
    publisher.publish(msg)

def setup_ir_sensor(publisher):
    GPIO.setmode(GPIO.BCM)
    global ir_sensor_pin
    ir_sensor_pin = 23  # Replace with the actual GPIO pin number to which the sensor is connected
    GPIO.setup(ir_sensor_pin, GPIO.IN)
    GPIO.add_event_detect(ir_sensor_pin, GPIO.BOTH, callback=measure_distance)

def main():
    rclpy.init()
    node = rclpy.create_node('ir_sensor_publisher')
    global publisher
    publisher = node.create_publisher(Float64, '/sensor/distance', 10)
    setup_ir_sensor(publisher)

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass

    node.destroy_node()
    rclpy.shutdown()
    GPIO.cleanup()

if __name__ == '__main__':
    main()

