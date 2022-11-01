from ament_index_python.packages import get_package_share_path

import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.conditions import IfCondition, UnlessCondition
from launch.substitutions import Command, LaunchConfiguration

from launch_ros.actions import Node
from launch_ros.parameter_descriptions import ParameterValue

def generate_launch_description():
    urdf_tutorial_path = get_package_share_path('urdf_tutorial')
    phantomx_arm_description_path = get_package_share_path('phantomx_arm_description')

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                [os.path.join(urdf_tutorial_path, 'launch'), '/display.launch.py']),
            launch_arguments={'model': os.path.join(phantomx_arm_description_path, 'urdf/phantomx.xacro') }.items(),
        ),
    ])
