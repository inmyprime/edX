#!/usr/bin/env python  
import rospy

from std_msgs.msg import Int16
from project1_solution.msg import TwoInts

pub = rospy.Publisher('sum', Int16, queue_size=10)

def callback(data):
 	#print (data.a, data.b)
  	pub.publish(Int16(data.a + data.b))
    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('sum_two_ints', anonymous=True)

    rospy.Subscriber("two_ints", TwoInts, callback)
        
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()