import rclpy
from rclpy.node import Node
from sensor_msgs.msg import Imu
from std_msgs.msg import Header
import numpy as np

class IMU(Node):
    def __init__(self):
        super().__init__('imu')

        self.publisher = self.create_publisher(Imu, '/imu/data', 10)
        self.timer = self.create_timer(0.02, self.publish)
    
    def publish(self):
        imu_msg = Imu()

        # Header
        imu_msg.header = Header()
        imu_msg.header.stamp = self.get_clock().now().to_msg()
        imu_msg.header.frame_id = 'imu_frame'

        # Simulated orientation (as quaternion)
        imu_msg.orientation.x = 0.0
        imu_msg.orientation.y = 0.0
        imu_msg.orientation.z = 0.0
        imu_msg.orientation.w = 1.0

        # Simulated angular velocity (rad/s)
        imu_msg.angular_velocity.x = np.random.normal(0.0, 0.01)
        imu_msg.angular_velocity.y = np.random.normal(0.0, 0.01)
        imu_msg.angular_velocity.z = np.random.normal(0.0, 0.02)

        # Simulated linear acceleration (m/s^2)
        imu_msg.linear_acceleration.x = np.random.normal(0.0, 0.1)
        imu_msg.linear_acceleration.y = np.random.normal(0.0, 0.1)
        imu_msg.linear_acceleration.z = np.random.normal(9.81, 0.1)  # gravity on z

        self.publisher.publish(imu_msg)
        self.get_logger().info('Published simulated IMU data')