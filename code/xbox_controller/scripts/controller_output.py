#!/usr/bin/env python

import rospy
from std_msgs.msg import Float32
from sensor_msgs.msg import Joy

def joy_callback(joy_data):
    left_updown      = Float32()
    left_updown.data = joy_data.axes[1]
    pub_left_updown.publish(left_updown)

    left_leftright      = Float32()
    left_leftright.data = joy_data.axes[0]
    pub_left_leftright.publish(left_leftright)

    right_updown      = Float32()
    right_updown.data = joy_data.axes[3]
    pub_right_updown.publish(right_updown)

    right_leftright      = Float32()
    right_leftright.data = joy_data.axes[2]
    pub_right_leftright.publish(right_leftright)

def joy_xbox_controller():
    global pub_left_updown, pub_left_leftright
    global pub_right_updown, pub_right_leftright
    topic_l_updown      = 'xbox_controller/left_stick_updown'
    topic_l_leftright   = 'xbox_controller/left_stick_leftright'
    topic_r_updown      = 'xbox_controller/right_stick_updown'
    topic_r_leftright   = 'xbox_controller/right_stick_leftright'
    pub_left_updown     = rospy.Publisher(topic_l_updown,    Float32, queue_size=10)
    pub_left_leftright  = rospy.Publisher(topic_l_leftright, Float32, queue_size=10)
    pub_right_updown    = rospy.Publisher(topic_r_updown,    Float32, queue_size=10)
    pub_right_leftright = rospy.Publisher(topic_r_leftright, Float32, queue_size=10)
    rospy.Subscriber('/joy', Joy, joy_callback)
    rospy.init_node('XboxControllerOuput')
    rospy.spin()

if __name__ == '__main__':
    joy_xbox_controller()
