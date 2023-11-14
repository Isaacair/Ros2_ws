import os
import time
import rclpy
import subprocess
import threading
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, ExecuteProcess,RegisterEventHandler,TimerAction
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from geometry_msgs.msg import Twist
import subprocess
import launch
from nav2_simple_commander.robot_navigator import BasicNavigator
from geometry_msgs.msg import PoseStamped, PoseWithCovarianceStamped
from launch.actions import SetLaunchConfiguration

def generate_launch_description():
    my_package='diffdrive_arduino'
    use_sim_time = LaunchConfiguration('use_sim_time', default='false')

    robot_file = os.path.join(get_package_share_directory(my_package), 'urdf', 'diffbot.urdf.xacro')

    
    diffbot_launch=IncludeLaunchDescription(
           PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(my_package),'launch','diffbot.launch.py')]),
           launch_arguments={'use_sim_time':'false'}.items()
    ) 
   
    lidar_launch=IncludeLaunchDescription(
           PythonLaunchDescriptionSource([os.path.join(get_package_share_directory(my_package),'launch','rplidar.launch.py')]))

    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([os.path.join(get_package_share_directory('slam_toolbox'),'launch', 'online_async_launch.py')]),
        launch_arguments= {'use_sim_time':'false','params_file':'./src/diffdrive_arduino/bringup/config/mapper_params_online_async.yaml'}.items())

    rviz=Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            parameters=[{'use_sim_time': use_sim_time}],
            output='screen')
    
    ld = LaunchDescription()
    ld.add_action(diffbot_launch)
    ld.add_action(lidar_launch)
    ld.add_action(slam_launch)
    ld.add_action(rviz)
    
    
    
    
    return ld



generate_launch_description()

def save_map():
    print("saving map")
    rclpy.init(args=None)
    
    map_file_name = "my_map"
    map_file_path = os.path.join(os.path.expanduser("~"), "maps", map_file_name)
    

    subprocess.run(["ros2", "run", "nav2_map_server", "map_saver_cli", "-f", "maps/my_map"])
    rclpy.shutdown()

def timer_callback():
    save_map()
    subprocess.run(['ros2', 'launch', 'nav2_bringup', 'bringup_launch.py', 'use_sim_time:=false', 'map:=maps/my_map.yaml'], check=True)
    
    
    
def start(duration):
    print("timer started")
    timer = threading.Timer(duration, timer_callback)
    timer.start()

start(25)


     
