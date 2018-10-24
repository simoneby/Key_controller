# LED-BOARD
import RPi.GPIO as GPIO
import time
from random import randint


class LED_board:
    # the pins used on the r-pi
    pins = [16, 20, 21]

    # -1 is input, 0 is low and 1 is high
    pin_led_states = [
        [1, 0, -1],  # 0
        [0, 1, -1],  # 1
        [-1, 1, 0],  # 2
        [-1, 0, 1],  # 3
        [1, -1, 0],  # 4
        [0, -1, 1]   # 5
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
        for i in range(0,len(self.pin_led_states)-1):
            self.set_pin(self.pin_led_states[i][0], -1)
        #for pin_index, pin_state in enumerate(self.pin_led_states[led_number]):
         #   self.set_pin(pin_index, -1)

    def flash_all_leds(self, seconds):

        end_time = time.time() + seconds

        while time.time() < end_time:
            second_end_time = time.time() + 0.2
            while time.time() < second_end_time:
                for i in range(6):
                    self.light_led(i)
            time.sleep(0.5)

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

        end_time = time.time() + seconds
        while time.time() < end_time:
            self.light_led(led_to_blink)
            time.sleep(0.4)

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

    def wrong_password(self):  # will flash for 3 seconds if wrong password

       seconds = 3
       end_time = time.time() + seconds

       while time.time() < end_time:
            second_end_time = time.time() + 0.2
            while time.time() < second_end_time:
                for i in range(6):
                    self.light_led(i)
            time.sleep(0.2)


    def lars_flash_leds(self, seconds):
        end_time = time.time() + seconds
        while time.time() < end_time:
            second_end_time = time.time() + 0.2
            while time.time() < second_end_time:
                for i in range(6):
                    self.light_led(i)
            time.sleep(0.2)


#if __name__ = "__main__":
#    object = LED_board
#    LED_board.lars_flash_light(10)
