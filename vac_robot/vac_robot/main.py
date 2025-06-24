import rclpy
from vac_robot.lidar import LIDAR
from vac_robot.imu import IMU
from vac_robot.system_monitor import SystemMonitor

def main(args=None):
    rclpy.init(args=args)
    lidar_node = LIDAR()
    imu_node = IMU()
    system_monitor = SystemMonitor("isha_compute")

    # Use a MultiThreadedExecutor if timers are on different frequencies
    executor = rclpy.executors.MultiThreadedExecutor()
    executor.add_node(lidar_node)
    executor.add_node(imu_node)
    executor.add_node(system_monitor)

    try:
        executor.spin()
    finally:
        lidar_node.destroy_node()
        imu_node.destroy_node()
        system_monitor.destroy_node()
        rclpy.shutdown()

if __name__ == '__main__':
    main()