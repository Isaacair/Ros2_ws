import os
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
def generate_launch_description():

    return LaunchDescription([
        DeclareLaunchArgument('min_angle', default_value='2.094'),  # 120 degrees in radians
        DeclareLaunchArgument('max_angle', default_value='4.189'),  # 240 degrees in radians  

        Node(
            package='rplidar_ros',
            executable='rplidar_composition',
            output='screen',
            parameters=[
            {'angle_min': LaunchConfiguration('min_angle')},
            {'angle_max': LaunchConfiguration('max_angle')},                

            {
                'serial_port': '/dev/serial/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.4:1.0-port0',
                'frame_id': 'laser_frame',
                'angle_compensate': True,
                'scan_mode': 'Standard'}]
                
        )
    ])
