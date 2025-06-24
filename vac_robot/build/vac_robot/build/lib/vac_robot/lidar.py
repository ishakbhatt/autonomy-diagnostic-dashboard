import rclpy
from rclpy.node import Node
from sensor_msgs.msg import PointCloud2
import sensor_msgs_py.point_cloud2 as pc2
import numpy as np
from std_msgs.msg import Header

class LIDAR(Node):
    def __init__(self):
        super().__init__('lidar')
        self.publisher = self.create_publisher(PointCloud2, '/lidar/points', 10)
        self.timer = self.create_timer(0.1, self.publish)  # 10 Hz
        self.num_points = 1000

    def publish(self):
        # semi-circle Lidar scan pattern
        angles = np.linspace(-np.pi / 2, np.pi / 2, self.num_points)
        radius = np.random.uniform(2.0, 10.0, self.num_points)
        x = radius * np.cos(angles)
        y = radius * np.sin(angles)
        z = np.random.normal(0.0, 0.05, self.num_points)  # small noise

        points = list(zip(x, y, z))

        header = Header()
        header.stamp = self.get_clock().now().to_msg()
        header.frame_id = 'lidar_frame'

        pointcloud_msg = pc2.create_cloud_xyz32(header, points)

        self.publisher.publish(pointcloud_msg)

        self.get_logger().info(f'Published PointCloud2 with {self.num_points} points')