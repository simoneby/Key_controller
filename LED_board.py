# LED-BOARD
import RPi.GPIO as GPIO
import time
from random import randint


class LED_board:
    # the pins used on the r-pi
    pins = [18, 23, 24]

    # -1 is input, 0 is low and 1 is high
    pin_led_states = [
        [1, 0, -1],  # 0
        [0, 1, -1],  # 1
        [-1, 1, 0],  # 2
        [-1, 0, 1],  # 3
        [1, -1, 0],  # 4
        [0, -1, 1]  # 5
    ]

    def setup(self, pins, pin_led_states):
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

        self.pins = pins
        self.pin_led_states = pin_led_states

    def set_pin(self, pin_index, pin_state):
        # if pin state is -1, that is the input.
        if pin_state == -1:
            GPIO.setup(self.pins[pin_index], GPIO.IN)
        # if pin state is 0 (low) or 1 (high), those are the outputs. The direction of the LEDs will determine which will light up.
        else:
            GPIO.setup(self.pins[pin_index], GPIO.OUT)
            GPIO.output(self.pins[pin_index], pin_state)

    def light_led(self, led_number):
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, pin_state)

    def turn_off_led(self, led_number):
        for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
            self.set_pin(pin_index, -1)

    def flash_all_leds(self, seconds):

        stop = time.time() + seconds

        while time.time() < stop:
            for i in range(0, len(self.pin_led_states) - 1):
                for pin_index, pin_state in enumerate(self.pin_led_states[i]):
                    self.set_pin(pin_index, pin_state)
                    time.sleep(0.01)
                    self.turn_off_led(i)

    def power_up(self):
        for i in range(0, len(self.pin_led_states) - 1):
            self.light_led(i)
            time.sleep(0.2)
            self.turn_off_led(i)

    def power_down(self):
        for i in range(len(self.pin_led_states) - 1, 0, -1):
            self.light_led(i)
            time.sleep(0.2)
            self.turn_off_led(i)

    def specified_duration_blink(self, led_to_blink, seconds):

        self.light_led(led_to_blink)
        time.sleep(seconds)
        self.turn_off_led(led_to_blink)

    def twinkle_all_leds(self, seconds):  # successful login.
        stop = time.time() + seconds

        while time.time() < stop:
            # will first blink 0, 2, 4
            for i in range(0, len(self.pin_led_states) - 1, 2):
                self.light_led(i)
                time.sleep(0.05)
                self.turn_off_led(i)
            # then 5, 3, 1
            for k in range(len(self.pin_led_states) - 1, 0, -2):
                self.light_led(k)
                time.sleep(0.05)
                self.turn_off_led(k)

    def wrong_password(self):  # ikke ferdig
        while True:
            for i in range(0, len(self.pin_led_states)):
                for pin_index, pin_state in enumerate(self.pin_led_states[i]):
                    self.set_pin(pin_index, pin_state)
                    time.sleep(0.01)
                    self.set_pin(pin_index, -1)

    # set_pin(0, -1)
    # set_pin(1, 0)
    # set_pin(2, 1)

    # while True:
    #    x = int(raw_input("Pin (0 to 5):"))
    #   light_led(x)
