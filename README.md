# go2\_description

This ROS2 package provides the URDF model for the Unitree Go2 robot, ported from the original work by Unitree Robotics.

  - Original Repository: [https://github.com/unitreerobotics/unitree\_ros.git](https://github.com/unitreerobotics/unitree_ros.git)
  - Original Author: Unitree Robotics
  - ROS 2 Port Maintainer: Kunzhao Ren

-----

## Usage

After a successful build, you can use the launch file to visualize the robot in RViz.
```bash
cd ~/go2_ws
source /opt/ros/humble/setup.bash
colcon build --packages-select go2_description 
source install/setup.bash
ros2 launch go2_description go2_rviz.launch.py
```
This will open an RViz window with the Go2 URDF model.

-----
