# LED-BOARD
import RPi.GPIO as GPIO

class led_board:

    # the pins used on the r-pi
    pins = [18, 23, 24]

    # -1 is input, 0 is low and 1 is high
    pin_led_states = [
      [1, 0, -1], # 0
      [0, 1, -1], # 1
      [-1, 1, 0], # 2
      [-1, 0, 1], # 3
      [1, -1, 0], # 4
      [0, -1, 1]  # 5
    ]

    def setup(self):
        GPIO.setmode(GPIO.BCM)

    def set_pin(self, pin_index, pin_state):
        # if pin state is -1, that is the input.
        if pin_state == -1:
            GPIO.setup(pins[pin_index], GPIO.IN)
        # if pin state is 0 (low) or 1 (high), those are the outputs. The direction of the LEDs will determine which will light up.
        else:
            GPIO.setup(pins[pin_index], GPIO.OUT)
            GPIO.output(pins[pin_index], pin_state)

    def light_led(self, led_number):
        for pin_index, pin_state in enumerate(pin_led_states[led_number]):
            set_pin(pin_index, pin_state)

    def turn_off_led(self, led_number):
        for pin_index in enumerate(pin_led_states[led_number]):
            set_pin(pin_index, 0)

    def flash_all_leds(self, seconds):

        sleep(seconds)

    def power_up(self):

    def power_down(self):




    set_pin(0, -1)
    set_pin(1, 0)
    set_pin(2, 1)

    while True:
        x = int(raw_input("Pin (0 to 5):"))
        light_led(x)


    # Voltage
    GPIO.output(outpin,GPIO.HIGH)
    GPIO.output(outpin,GPIO.LOW)



    def twinkle_all_leds(self, seconds):

    def first_keystroke(self):

    def wrong_password(self):

    def successfull_login(self):

    def powering_down(self):

    def specified_duration_blink(self, led_to_blink):


