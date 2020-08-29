#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def callback(msg):
    rospy.loginfo("CallerID : {}".format(rospy.get_caller_id()))
    rospy.loginfo("I heard {}".format(msg.data))

def listener():
    rospy.init_node('listener',anonymous=True)
    rospy.Subscriber('chatter',String,callback)
    rospy.spin()

if __name__=='__main__':
    listener()
