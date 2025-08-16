# This program demonstrates how to control a servo

# Import the relevant libraries
import RPi.GPIO as GPIO
import time
 
# GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)
 
# set GPIO Pins
ServoPin = 7                                        # GPIO pin for the servo

# set GPIO direction (IN / OUT)
GPIO.setup(ServoPin, GPIO.OUT)                      # Set ServoPin's mode to output


# The servo is controlled using Pulse Width Modulation (PWM)
# The next few lines of code take care of the required setup for this functionality
# The details are not important; you should not modify this code
# --- Start of the PWM setup ---
# Set PWM parameters
pwm_frequency = 50
duty_min = 2.5 * float(pwm_frequency) / 50.0
duty_max = 12.5 * float(pwm_frequency) / 50.0

    # Helper function to set the duty cycle
def set_duty_cycle(angle):
    return ((duty_max - duty_min) * float(angle) / 180.0 + duty_min)

    # Create a PWM instance
pwm_servo = GPIO.PWM(ServoPin, pwm_frequency)

# --- End of the PWM setup ---




# Main program 
try:
        
    # This code repeats forever
    while True:

        # Move the servo
        angle = 0
        pwm_servo.start(set_duty_cycle(angle))
        print ("Moving to angle 0")
        time.sleep(1)
                       
        angle = 180
        pwm_servo.start(set_duty_cycle(angle))
        print ("Moving to angle 180")
        time.sleep(1)

            
# Reset by pressing CTRL + C
except KeyboardInterrupt:
        print("Program stopped by User")
        GPIO.cleanup()
