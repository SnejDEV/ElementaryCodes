#!/usr/bin/python3
'''import rospy
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
'''
#!/usr/bin/python3
import rospy,time,sys
from geometry_msgs.msg import Twist

def msg():
    try:    
        twist.linear.x = float(input("Linear x: "))
        twist.angular.z = float(input("Angular z: "))
    except:
        sys.exit("Program Execution Terminated")

def pubInit():
    global pub
    rospy.init_node("talk",anonymous=True)
    pub = rospy.Publisher("/turtle1/cmd_vel",Twist,queue_size=10)

if __name__=="__main__":
    global twist 
    twist = Twist()
    pubInit()
    print("Invalid inputs terminates code execution")
    while not(rospy.is_shutdown()):
        msg()
        try:
            pub.publish(twist)
        except rospy.ROSInterruptException:
            pass
        time.sleep(5)
