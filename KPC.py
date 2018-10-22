#Key Pad Controller

from LED_board import *
from Keypad import *


class KPC:




    def __init__(self):
        self.Led_board = LED_board()
        self.Keypad = Keypad()
        path = "" #path to filename


    def init_passcode_entry(self):

    def get_next_signal(self):

    def verify_login(self):

    def validate_passcode_change(self):

    def light_one_led(self):

    def flash_leds(self):

    def twinkle_leds(self):
        Led_board.twinkle_all_leds(self)

    def exit_action(self):
        Led_board.power_down(self)


