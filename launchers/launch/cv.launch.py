from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription(
        [
            Node(
                package='show_pic',
                executable='main'
            ),
            
            Node(
                package='rqt_image_view',
                executable='rqt_image_view'
            )
        ]
    )