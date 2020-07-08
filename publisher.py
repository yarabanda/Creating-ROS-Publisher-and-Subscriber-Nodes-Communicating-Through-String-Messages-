#!/usr/bin/env python3 

import rospy
from std_msgs.msg import String

def publisher():
	 pub = rospy.Publisher('string_message', String, queue_size=10) #topic name is string_message 
	 rospy.init_node('publisher', anonymous=True)  #node name is publisher 
	 rate = rospy.Rate(10)  #the rate is 10 messages/second
	 while not rospy.is_shutdown():
	 	hello_str = "hello there %s" % rospy.get_time()
	 	rospy.loginfo(hello_str)
	 	pub.publish(hello_str)
	 	rate.sleep()
	 	
	 	
if __name__ == '__main__':
	try:
		publisher()
	except rospy.ROSInterruptException:
		pass 
	 