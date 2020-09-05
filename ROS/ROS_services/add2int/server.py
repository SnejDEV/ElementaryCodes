#!/usr/bin/python3 
import rospy
from rosfunda.srv import nos,nosResponse            #import the nos and nosResponse service header files 

def handler(req):
    print("Processing requests")
    sum = req.a+req.b                               #add req object's attributes a and b
    return nosResponse(sum)                         #return the response object to the callback, therefore responds to the service

def server():
    rospy.init_node("add_server",anonymous=False)   #initialize server node
    rospy.Service("add",nos,handler)                #start the service add, and wait for requests, 
                                                    #if any pass it to the handler function
    print("Waiting for requests")
    rospy.spin()                                    #keep the server running, waiting for incoming requests

if __name__=="__main__":
    server()  
