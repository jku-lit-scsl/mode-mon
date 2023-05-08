import rospy
from admon_mode_cps_pkg.util.tester import get_test_registry
from std_msgs.msg import String


def talker():
    pub = rospy.Publisher('chatter', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10)  # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        rate.sleep()


if __name__ == '__main__':

    try:
        # create registry
        registry = get_test_registry()
        # init Mode Manager
        print('temp')
    except rospy.ROSInterruptException:
        pass
