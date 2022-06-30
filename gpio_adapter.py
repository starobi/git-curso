import RPi.GPIO as GPIO

## GPIOAdapter
# This class with its functions will be used from the LedHandler class.
# This class configures and handles the GPIO Pins and the PWM Duty Cycles.
class GPIOAdapter:
    PWM_FREQ=1 # in Hz
    PWM_DUTY_OFF=0 # Duty Cycle, when LED should be disable
    PWM_DUTY_ON=50.0 # Duty Cycle, when LED should be enable
    LED_GPIO=13 # GPIO Pin on Raspberry Pi

    ## Init
    # Setup Output-Mode and GPIO Pin for PWM
    def __init__(self):
        # Setup GPIO Pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.LED_GPIO, GPIO.OUT)
        
        self.pwm = GPIO.PWM(self.LED_GPIO, self.PWM_FREQ)
        # Default Duty Cycle = 0 (LED is OFF)
        self.pwm.start(self.PWM_DUTY_OFF)

    ## Function, when LED should be disabled
    # Duty Cycle will not change (LED stays OFF)
    def led_disable(self): 
        self.pwm.ChangeDutyCycle(self.PWM_DUTY_OFF)

    ## Function, when LED should be enabled
    # Duty cycle will change to 50.0% (LED turns ON)
    def led_blink(self):
        self.pwm.ChangeDutyCycle(self.PWM_DUTY_ON)

    ## Cleanup funtion
    def cleanup(self):
        # Cleans the GPIO Pins after Shutdown
        GPIO.cleanup()
