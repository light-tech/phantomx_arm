# ROS2 package for Phantom X Pincher robot arm

 [x] View and control the virtual arm in `rviz2` (thank to `urdf_tutorial` and `joint_state_publisher_gui`)

    ```shell
    ros2 launch phantomx_arm_bringup rviz2.launch.py
    ```

 [ ] Control the physical arm via `ros2_control` (needs to migrate the `arbotix_ros` package)

 [ ] Support `MoveIt2` motion planning

Need to install ROS arduino onto the arbotix board using arduino 1.05

Install arbotix_ros package

Configure phantomx_arm_moveit_controller_manager.launch file

-- Create gazebo files to include multiple turtlebots with distinct controller namespaces

-- Incorporate AMCL + move_base for the system and get it rolling for multiple turtlebots inside gazebo

-- Program an effective pick-n-place functionality for multiple phantomx turtlebots in gazebo

