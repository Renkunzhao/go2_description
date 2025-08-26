import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():

    # 替换为你的包名
    pkg_name = 'go2_description'
    pkg_share_dir = get_package_share_directory(pkg_name)
    
    # 获取 URDF 文件的完整路径
    urdf_file = os.path.join(pkg_share_dir, 'urdf', 'go2_description.urdf')

    # 将 URDF 内容读入 robot_description 参数
    with open(urdf_file, 'r') as infp:
        robot_desc = infp.read()

    # 启动 joint_state_publisher_gui 节点
    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        name='joint_state_publisher_gui'
    )

    # 启动 robot_state_publisher 节点
    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',
        parameters=[{'robot_description': robot_desc}]
    )

    # 启动 rviz2 节点
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        output='screen',
        arguments=['-d', os.path.join(pkg_share_dir, 'rviz', 'go2.rviz')]
    )

    return LaunchDescription([
        joint_state_publisher_gui_node,
        robot_state_publisher_node,
        rviz_node
    ])