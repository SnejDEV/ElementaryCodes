#!/usr/bin/python3
import sys,rospy
from rosfunda.srv import nos,nosRequest

def client(a,b):
    rospy.wait_for_service("add")
    try:
        r = rospy.ServiceProxy("add",nos)
        responseObj = r(a,b)
        return responseObj.sum
    except rospy.ServiceException as e:
        print("Service request failed")
        print("Exception: ".format(e))


if __name__=="__main__":
    if(len(sys.argv)==3):
        print(client(int(sys.argv[1]),int(sys.argv[2])))
    else:
        print("Incorrect command line args")
        print(sys.argv)
        sys.exit(1)
