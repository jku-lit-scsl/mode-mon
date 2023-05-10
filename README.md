# Proof of Concept Repo for IWCFS'23 Submission

## Towards Increasing Safety in Collaborative CPS Environments

### Abstract
Cyber-Physical Systems (CPS) frequently operate in collaborative environments with other CPS and humans. This collaborative environment has the potential for situations in which CPS endanger humans. We argue that safety in such environments can be increased if the environment is aware of the safety-critical situation and can respond appropriately. In this paper, we describe our preliminary work on a collaborative CPS safety framework that combines distinct modes of operation with adaptive monitoring.

### About
This repository contains a prototypical implementation of the proposed framework architecture.
The repository represents a ready to use ROS package.

## Set-Up

Setup PC and ROS Noetic Ninjemys according to ROBOTIS
eManual: https://emanual.robotis.com/docs/en/platform/turtlebot3/quick-start/#pc-setup

Setup Gazebo Simulation for ROS Noetic Ninjemys according to ROBOTIS
eManual: https://emanual.robotis.com/docs/en/platform/turtlebot3/simulation/#gazebo-simulation

### Third Party

For easy usage as part of the CMake build cycle it is recommended to download the packages locally and include them into
the src folder of the ROS package.

- ```pip install python-statemachine```
- ```pip install paho-mqtt```

Furthermore, an up and running MQTT Broker (e.g., mosquitto) as localhost is required.

### Bring-Up

1. Fetch ROS package into catkin workspace
2. Run: ```catkin_make``` in catkin workspace
3. Start ROS: ```roscore```
4. Start Gazebo multi simulation: ```roslaunch turtlebot3_gazebo multi_turtlebot3.launch```
5. Run ROS package: ```rosrun amon_mode_cps main.py``` (this also starts the monitoring)
6. Trigger a maintenance mode switch for a TurtleBot by publishing it via the MQTT Broker under the `trigger` topic:

```
{
  "mode": "maintenance",
  "device": "tb3_0"
}
```

7. Watch the monitoring and mode switches in the log/forwarded messages in MQTT
