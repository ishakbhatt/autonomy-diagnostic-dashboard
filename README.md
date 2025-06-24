# Autonomy Diagnostics Dashboard
Diagnostic Dashboard for Autonomous Vehicles 


## Milestones
* simulate system performance of a robotics system (e.g. CPU/memory/network/sensor activity)
* log & visualize potential latency bottlenecks or reliability flags
* analyze system behavior, pinpoint issues, and provide insight to engineers

## Deliverables
1. Python system monitor simulating or collecting:
    * certain metrics such as CPU, memory, disk, network load
    * simulated CAN/Lidar/Cam message delays (timing jitter or data drop)
    * latency of mock ROS messages
2. CSV or SQLite logging
    * store event timestamps, delays, system state
    * mimic SQL queries to extract insights
3. Minimal dashboard 
    * graphs showing performance changes
    * tables with max delays, % drop in sensor messages
    * Indicators and warnings
4. README that will be a one-pager demonstrating the tool's capabilities

# Full system description 
The mock system is a mobile robot that has various sensors and currently is just able to do perception. Later on, I will add behavior and control topics. This mobile robot is a vaccuum robot that is tasked with vacumming the entire room by doing frontier exploration. To start, it has a lidar, IMU, wheel encoders, and Jetson Nano. Additional components may be added. 

