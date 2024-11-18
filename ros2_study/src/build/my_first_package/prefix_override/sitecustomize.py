import sys
if sys.prefix == '/usr':
    sys.real_prefix = sys.prefix
    sys.prefix = sys.exec_prefix = '/workspace/user/kjy/ROS/ros2_study/src/install/my_first_package'
