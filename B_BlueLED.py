from pickle import TRUE
import rospy
from gpio_adapter import GPIOAdapter
from std_msgs.msg import Bool



def blueLED_callback(message):
    rospy.loginfo("Blinking: %s", message.data)
    if message.data == TRUE:
        GPIOAdapter.led_blink
    else:
        GPIOAdapter.led_disable

    
def Blue_LED():


    # In ROS, nodes are uniquely named. If two nodes with the same
    # node are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('B_BlueLED', anonymous=True)


    rospy.Subscriber("led_state", Bool, blueLED_callback)


    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()


if __name__ == '__main__':
    Blue_LED()
