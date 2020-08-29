#!/usr/bin/python3
import rospy
from geometry_msgs.msg import Twist

def talker(pub,twist):
    pub.publish(twist)

def inp(twist):
    print("Linear Velocity")
    twist.linear.x = float(input("Enter linear velocity, x : "))
    print("Angular Velocity")
    twist.angular.z = float(input("Enter angular velocity, z : "))

if __name__ == "__main__":
    
    twist = Twist()
    rospy.init_node("talker",anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)
    
    while(not(rospy.is_shutdown())):
        inp(twist)
        try:    
            talker(pub,twist)
        except rospy.ROSInterruptException:
            pass
