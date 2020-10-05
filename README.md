# RI_Part2

This Reposity contains only Part 2 of the project.

1. udm_leg contains the details about the robot Quad (four leg).
2. moveit2 is generated with moveit.
3. urdf_project_control consist of node to control the robot.

## Installation
The package need to be install in your catkin workspace.
```
cd catkin_ws/src
git clone https://github.com/Seekcha/RI_Part2.git
catkin build
cd ..
source devel/setup.bash
```

## Execution
### Four legs in RVIZ
Open quad_robot in RVIZ in first terminal:
```
source devel/setup.bash
roslaunch moveit2 demo.launch
```

### Movement
Launch service.launch in second terminal:
```
source devel/setup.bash
roslaunch urdf_project_control service.launch
```

#### Calling Function
Launch in third terminal:
```
source devel/setup.bash
rosservice call /control "mouvement:
 data: 'front'
 ```
