#Key Pad Controller

from LED_board import *


class KPC:

    def __init__(self):
        Led_board = LED_board()

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


