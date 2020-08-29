#!/usr/bin/python3
import rospy
from std_msgs.msg import String

def talker(a):
    pub = rospy.Publisher("chatter",String,queue_size=10)
    rospy.init_node("talker",anonymous=True)
    pub.publish(a)

def inp():
    a=str(input("Enter data to be transmitted: "))
    try:
        talker(a)
    except rospy.ROSInterruptException:
        pass

if __name__=='__main__':
    while(not(rospy.is_shutdown())):
        inp()
