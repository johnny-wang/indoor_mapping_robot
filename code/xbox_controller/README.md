Copy `xbox_controller/` directory to `catkin_ws`.

Run
```
catkin_make
catkin_make install
source ~/catkin_ws/devel/setup.bash   # if necessary
roslaunch xbox_controller xbox_controller.launch
```

Left and right joystick actions will be published to topics:
```
/xbox_controller/left_stick_leftright
/xbox_controller/left_stick_updown
/xbox_controller/right_stick_leftright
/xbox_controller/right_stick_updown
```
where values range from -1 to 1.
