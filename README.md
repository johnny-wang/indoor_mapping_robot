## Indoor Mapping Robot

The goal of this project is to create an indoor robot that can autonomously map my apartment space. This project will build upon the Hercules and Odroid setup/install. I will add a Kinect and Xbox 360 controller to the platform which will allow for manual control. Then I will combine the Kinect and encoder data to create a map using Octomap. Lastly, I will use the camera information (and sonar?) with some sort of exploration algorithm to full map my apartment space.

### Hardware
- Hercules 4WD robot
- Kinect 360
- Xbox 360 wirless controller
- HDE Xbox 360 wireless receiver
- Sabrent 4-port USB hub

### Setup
See Hercules and Odroid-install for basic setup.

#### Xbox 360 wireless controller setup
1. Install Joy
```
sudo apt-get install ros-kinetic-joy
```
2. Blacklist the default xpad driver
```
sudo su
echo "blacklist xpad" > /etc/modprobe.d/blacklist.conf
```
3. Unload xpad
```
sudo rmmod xpad
```
4. Install xboxdrv
```
sudo apt-add-repository ppa:grumbel/ppa
sudo apt-get update
sudo apt-get install xboxdrv
```
5. Start xboxdrv
```
sudo xboxdrv
```
6. Plug in wireless receiver and pair with xbox controller
