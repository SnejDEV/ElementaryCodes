#!/usr/bin/python3
import rospy
from turtlesim.msg import Pose

def callback(msg):
    rospy.loginfo("x = {}".format(msg.x))
    rospy.loginfo("y = {}".format(msg.y))
    rospy.loginfo("theta = {}".format(msg.theta))
    rospy.loginfo("x = {}".format(msg.linear_velocity))
    rospy.loginfo("x = {}".format(msg.angular_velocity))

def PoseSub():
    rospy.init_node("PoseSub",anonymous=True)
    rospy.Subscriber("/turtle1/pose",Pose,callback)
    rospy.spin()

if __name__ == "__main__":
    try:
        PoseSub()
    except rospy.ROSInterruptException:
        pass
