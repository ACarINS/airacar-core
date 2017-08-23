#!/usr/bin/env python
"""ACarIns core AI .

Right now its simple example, but working on extending it
"""
__author__ = 'Taras Emelyanenko <php.laboratory at gmail.com>'
__version__ = '0.1'
__license__ = 'BSD'
# Python libs
import sys, time


# Ros libraries
import roslib
import rospy

from std_msgs.msg import String
import std_msgs




VERBOSE = True


class airacar_feature:
    def __init__(self):
        '''Initialize ros publisher, ros subscriber'''
        # topic where we publish
        self.image_pub = rospy.Publisher("/airacar/output",
                                         String, queue_size=10)


        # subscribed Topic
        self.subscriber = rospy.Subscriber("/airacar/input",
                                           String, self.callback, queue_size=1)
        if VERBOSE:
            print "subscribed to /airacar/output"

    def callback(self, ros_data):
        '''Callback function of subscribed topic.
        Here commands get processed and features detected'''
        if VERBOSE:
            print 'received command: "%s"' % ros_data

        time1 = time.time()

        time2 = time.time()


        #### Create New command ####
        msg = std_msgs.msg.String()
        # msg.header.stamp = rospy.Time.now()

        msg.data = "yes, sir"
        # Publish new image
        self.image_pub.publish(msg)




def main(args):
    '''Initializes and cleanup ros node'''
    ic = airacar_feature()
    rospy.init_node('airacar_feature', anonymous=True)
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print "Shutting down ROS  Aira Car Core"



if __name__ == '__main__':
    main(sys.argv)