#!/usr/bin/env python

#import
import time
import wiringpi2 as wiringpi
import rospy
from std_msgs.msg import Int16




class led_control():

    def __init__(self):

        self.pin = 5   # 29 on PI2 rev B


        #init GPIO
        #wiringpi.wiringPiSetupGpio() already called by someone  
        wiringpi.pinMode(self.pin, 1)      # sets GPIO 24 to output  
        wiringpi.digitalWrite(self.pin, 1) # sets port 24 to 0 (0V, off)  


        #ROS init
        self.rate = rospy.Rate(10) # 10Hz
        self.subscriber = rospy.Subscriber("led_control_info", Int16, self.callback)


    def callback(self, data):
        led_output = data.data

        if led_output == 0:
            wiringpi.digitalWrite(self.pin, 0)
            print("GPIO LOW")
        elif led_output == 1:
            wiringpi.digitalWrite(self.pin, 1)
            print("GPIO HIGH")
        else:
            print("Error")

    def listener(self):
        rospy.spin()



if __name__ == '__main__':
    rospy.init_node('led_control', anonymous=True)

    try:
        pc = led_control()
        pc.listener()

    except rospy.ROSInterruptException as e:
        print(e)
        pass

    finally:
        if pc:
            wiringpi.digitalWrite(pc.pin, 0)
            wiringpi.pinMode(pc.pin, 0)

