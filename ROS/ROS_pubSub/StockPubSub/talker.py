#!/usr/bin/python3
import rospy     
from std_msgs.msg import String

def talker():                                                   #talker method 
    pub = rospy.Publisher('chatter', String, queue_size=10)     #setting up publish topic, and the type of msgs that can be 
                                                                #published through the topic     
    rospy.init_node('talker', anonymous=True)                   #starting a talker node(talker is the publisher node)     
    rate = rospy.Rate(1)                                        #creating rate object configured to 1hz                   

    while not rospy.is_shutdown():                              #if ^C isn't executed
        s="Hi listener"                                         #Storing msg in s 
        s = s+" "+str(rospy.get_time())                         #concatenate time to s to ease debug during msg logging
        rospy.loginfo(s)                                        #log msg to cmd line for debug purposes
        pub.publish(s)                                          #publish message(internally works as through the created pub node)
        rate.sleep()                                            #sleep alias delay at a rate of 1hz

if __name__=='__main__':                                        #creating code start point 
    try :
        talker()
    except rospy.ROSInterruptException:                         #at licit/illicit ^C exceptions, pass(do nothing)
        pass
