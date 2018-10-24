#Key Pad Controller

from LED_board import *

#from Key_controller.Keypad import Keypad

from Keypad import *

# Begynner bakerst

signals = ["#", "#", "*", "1", "3", "3", "8","N", "*", "1", "3", "3", "4", "*", "Y", "*","4", "3", "2", "1", "#"]

class KPC:

    def length_of_signals(self):
        return len(signals)

    def __init__(self):
        self.Led_board = LED_board()
        self.keypad=Keypad()
        self.path = "pw.txt"  # path to filename
        # setter opp keypad kun en gang
        self.keypad.setup()

        self.override_signal=None
        self.attempt=""
        self.last_signal=None
        self.LEDid=None
        self.light_duration=None
        self.Ldur=""
        self.CP = None
        self.new_pw = ""
        self.retype_new_pw = ""


    def set_override_signal(self,c):
        self.override_signal=c

    def go_back_to_start(self):
        self.reset_agent()
        print("-> exiting...")

    def go_back_to_active(self):
        self.reset_agent()
        print("-> didnt understand... going back to active")

    def go_to_active(self):
        self.reset_agent()
        print("-> going to active mode")

    def get_override_signal(self):
        return self.override_signal


    def does_allmost_nothing(self):
        print(" --- didnt do anything -- ")


    def pw_attempt(self):
        self.attempt = self.attempt + self.last_signal
        return self.attempt

    def new_pw(self):
        self.new_pw = self.new_pw + self.last_signal
        return self.new_pw

    def retype_new_pw(self):
        self.retype_new_pw = self.retype_new_pw + self.last_signal
        return self.retype_new_pw

    def get_CP(self):
        pw = open(self.path, "r")
        self.CP = pw.readline()
        pw.close()
        return self.CP

    # Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED Board.
    # This should be done when the user first presses the keypad.
    # starter ved å trykke på firkant,

    def init_passcode_entry(self):
        self.Led_board.power_up()
        print("Led board powered up")

    def init_new_passcode_entry(self):
        print("Ready to type in new password")

    def init_retype_passcode_entry(self):
        print("Ready to retype new password")


    def reset_agent(self):
        self.override_signal = None
        self.attempt = ""
        self.last_signal = None
        self.LEDid = None
        self.light_duration = None
        self.Ldur = ""
        self.retype_new_pw = ""
        self.new_pw = ""

    def refresh_agent(self):
        self.override_signal = None
        self.attempt = ""
        self.last_signal = None
        self.LEDid = None
        self.light_duration = None
        self.Ldur = ""

    def get_next_signal(self):
        while len(signals) > 0:
            self.last_signal = signals.pop()
            print("next signal: ")
            print(self.last_signal)
            return self.last_signal

    # Return the override-signal, if it is non-blank; otherwise query the keypad for the next pressed key.
    def get_next_signal1(self):
        signal=None
        if self.get_override_signal()==None:
             signal=self.keypad.get_next_signal()
        else:
            signal=self.get_override_signal()
        return str(signal)


    # Check that the password just entered via the keypad matches that in the password file.
    # Store the result (Y or N) in the override-signal.
    # initiate the appropriate lighting pattern for login success or failure.
    def verify_login(self):
        if self.attempt == self.get_CP():
            self.set_override_signal('Y')
            #self.twinkle_leds()
            print("correct pw, lights are twinkling")
        else:
            self.set_override_signal('N')
            #self.Led_board.wrong_password()
            print("incorrect pw, lights are blinking boo")
        self.attempt = ""


    #Check that the new password is legal. If so, write the new password in the password file.
    # A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9.
    # denne skal sjekkes to ganger?

    def validate_passcode_change(self):
        if len(self.new_pw) < 5:
            self.set_override_signal('N')
            print("new password is not strong enough")
        else:
            print("new password is strong enough")
            self.set_override_signal('Y')
            self.reset_agent()


    def verify_password(self):
        if self.retype_new_pw==self.new_pw:
            self.set_override_signal("Y")
            print("The password is changed")
            self.change_pw(self.new_pw)
            #self.twinkle_leds()

        else:
            self.set_override_signal("N")
            print("Wrong retyping of password, is not changed")
            self.Led_board.wrong_password()
        self.reset_agent()

    def change_pw(self, password):
        password = str(password)
        pw = open(self.path, "w")
        pw.write(password)
        pw.close()

    # ledNr is the Led number, ledDr is the led Duration
    # midlertidig

    def light_one_led(self):
        print("Light number " + str(self.LEDid + 1) + " ligts up for " + str(self.light_duration) + " seconds")

    def set_LED(self):
        self.LEDid = int(self.last_signal)

    def set_duration(self):
        sym=self.get_next_signal()
        while signal_is_digit(sym):
            self.light_duration+=sym
            sym=self.get_next_signal()
        self.light_duration = int(sym)

    def record_duration(self):
        self.Ldur = self.Ldur + self.last_signal

    def set_duration(self):
        self.light_duration = int(self.Ldur)
        self.light_one_led()
        self.Ldur = ""
        self.light_duration = None
        self.LEDid = None


    #request the flashing of all LEDs
    # midlertidig
    def flash_leds(self):
        print("all lights are flashing")

    #request the twinkling of all LEDs.
    def twinkle_leds(self):
        print("all lights are twinkling")
        self.Led_board.twinkle_all_leds(self)

    #initiate the ”power down” lighting sequence.

    def exit_action(self):
        self.reset_agent()
        #self.Led_board.power_down(self)
        print("exiting action...")

    def want_to_logout(self):
        print("Want to log out? Press #")





def signal_is_digit(signal): return 48 <= ord(signal) <= 57
def signal_is_any(signal): return signal_is_digit(signal) or signal == "*" or signal == "#"
def signal_is_led(signal): return 48 <= ord(signal) <= 53
def is_hashtag(signal): return signal == "#"
def is_star(signal): return signal == "*"

