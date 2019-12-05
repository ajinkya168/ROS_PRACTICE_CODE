#! /usr/bin/env python
from time import sleep
import RPi.GPIO as GPIO
import rospy
from std_msgs.msg import Int32
#step_count=0.0
#float(step_count)
#x=0.0
#float(x)
#range=0.0
#float(range)
DIR = 28
STEP =29
CW = 1
CCW = 0
#LOOP=1000 SPR =200
EN=25
M0=24
M1=23
M2=22
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(EN,GPIO.OUT)
GPIO.setup(M0,GPIO.OUT)
GPIO.setup(M1,GPIO.OUT)
GPIO.setup(M2,GPIO.OUT)
GPIO.setup(DIR, GPIO.OUT)
GPIO.setup(STEP, GPIO.OUT)
GPIO.output(EN, GPIO.LOW)
GPIO.output(DIR, GPIO.HIGH)
#step_count = SPR
#lp=LOOP
delay=0.05
GPIO.output(M0,GPIO.LOW)
GPIO.output(M1,GPIO.LOW)
GPIO.output(M2,GPIO.LOW)
GPIO.output(EN, GPIO.LOW)
#while(1):
 #angle=input(' enter angle ')
 #print(angle)
 

def run():
	rospy.Subscriber('motor_topic',Int32,callback)
	rospy.spin()

def callback(angle):
	rospy.loginfo("starting motor..")
       	step_count=float((angle.data)/(1.8))
 #step_count=input(' enter no of steps ')
        rospy.loginfo(round(step_count))
	rospy.loginfo(int(step_count))

# print(int(step_count))
	if step_count > 0:
		rospy.loginfo("rotating motor %d clockwise",angle.data)
		for x in range(step_count):
		 GPIO.output(EN, GPIO.LOW)
		 GPIO.output(DIR, GPIO.HIGH)
		# print('seedha ghumo')
		 GPIO.output(STEP, GPIO.HIGH)
		#print('mai high hu')
		 sleep(delay)
		 GPIO.output(STEP, GPIO.LOW)
		#print('mai low hu')
		 sleep(delay)
		sleep(0.005)
	else:
		rospy.loginfo("rotating motor %d anticlockwise",angle.data)
		step_count=(step_count)*(-1)
		print(step_count)
		#GPIO.output(DIR, GPIO.LOW)
		# print('ulta ghumo')
		for x in range(step_count):
		 GPIO.output(DIR, GPIO.LOW)
		#print('ulta ghumo')
		 GPIO.output(EN, GPIO.LOW)
		#GPIO.output(DIR, GPIO.LOW)
		 GPIO.output(STEP, GPIO.HIGH)
		#print('mai ulta high hu')
		 sleep(delay)
		 GPIO.output(STEP, GPIO.LOW)
		#print('mai ulta low hu')
		 sleep(delay)
		sleep(0.005)
	GPIO.output(EN,GPIO.HIGH)
	GPIO.cleanup()

if __name__=='__main__':
	rospy.init_node('run',anonymous=True)
	run()
