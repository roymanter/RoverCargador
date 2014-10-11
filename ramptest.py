import RPi.GPIO as GPIO
import time
import Platform
	
if __name__=="__main__":
	GPIO.setwarnings(False)
	movement = Platform.Platform();
	
	# FORWARD
	print "FORWARD"
	movement.state(1)
	movement.setVelocity(75)
	time.sleep(2)

	# STOP
	print "STOP"
	movement.state(0)
	time.sleep(2)
	
	# BACKWARD
	print "BACKWARD"
        movement.state(2)
	movement.setVelocity(75)
        time.sleep(2)
	
	# STOP
	print "STOP"
	movement.state(0)
