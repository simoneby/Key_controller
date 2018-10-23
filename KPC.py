#Key Pad Controller

from LED_board import *

#from Key_controller.Keypad import Keypad

from Keypad import *

class KPC:


    def __init__(self):
        self.Led_board = LED_board()
        self.keypad=Keypad()
        self.override_signal=None
        self.CUMP=None
        self.signals = ["4", "3", "2", "1", "#"]
        self.CP=""
        self.new_pas=None
        self.new_pas2=None
        self.path = "pw.txt" #path to filename
        self.attempt=None

        self.LEDid=None
        self.light_duration=None

        # setter opp keypad kun en gang
        self.keypad.setup()


    def get_CUMP(self):
        return self.CUMP


    def reset_CUMP(self):
        self.CUMP=None

    #legger til underveis,
   # def add__to_CUMP(self,number):
   #     self.CUMP+=number

    def get_new_pas(self):
        return self.new_pas

    def get_new_pas2(self):
        return self.new_pas2

    def set_new_pas(self,pas):
        self.new_pas=pas

    def set_new_pas2(self,pas):
        self.new_pas2=pas

    def set_override_signal(self,c):
        self.override_signal=c


    def get_override_signal(self):
        return self.override_signal


    def does_allmost_nothing(self):
        print("did almost something")
        return


    def pw_attempt(self):
        symbol = self.get_next_signal()
        while signal_is_digit(symbol):
            self.attempt += symbol
            symbol = self.get_next_signal()
        return self.attempt


    def get_CP(self):
        pw = open(self.path, "r")
        self.CP = pw.readline()
        pw.close()
        return self.CP

    # Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED Board.
    # This should be done when the user first presses the keypad.
    # starter ved å trykke på firkant,
    def init_passcode_entry(self):
        self.reset_CUMP()
        self.set_override_signal(None)
        self.Led_board.power_up()



    def reset_agent(self):
        self.reset_CUMP()
        self.set_override_signal(None)
        self.set_new_pas(None)
        self.set_new_pas2(None)
        self.LEDid=None
        self.light_duration=None

    def refresh_agent(self):
        self.set_override_signal(None)
        self.set_new_pas(None)
        self.set_new_pas2(None)
        self.LEDid=None
        self.light_duration=None

    def get_next_signal(self):
        return self.signals.pop()

    # Return the override-signal, if it is non-blank; otherwise query the keypad for the next pressed key.
    def get_next_signal1(self):
        signal=None
        if self.get_override_signal()==None:
             signal=self.keypad.get_next_signal()
        else:
            signal=self.get_override_signal()
        return str(signal)


    #def does_nothing():
     #   return

    # Check that the password just entered via the keypad matches that in the password file.
    # Store the result (Y or N) in the override-signal.
    # initiate the appropriate lighting pattern for login success or failure.
    def verify_login(self):
        if self.pw_attempt() == self.get_CP():
            self.set_override_signal('Y')
            self.twinkle_leds()
        else:
            self.set_override_signal('N')
            self.Led_board.wrong_password()

    #trengs denne eller kan vi bruke get-next-signal?
    #tror kanskje det er bedre å lage dette i FSM
    def enter_new_password2(self):
        if self.validate_passcode_change():
            pas=None
            np=self.keypad.get_next_signal()
            while np!='*':
                pas+=np
                self.set_new_pas2(pas)

    #trengs denne eller kan vi bruke get-next-signal?
    def enter_new_password(self):
        pas=None
        np=self.keypad.get_next_signal()
        while np!='*':
            pas+=np
        self.set_new_pas(pas)


    #Check that the new password is legal. If so, write the new password in the password file.
    # A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9.
    # denne skal sjekkes to ganger?
    def validate_passcode_change(self):
        legal=False
        for digit in self.get_new_pas():
                legal=signal_is_digit(digit)

        if len(self.get_new_pas())<4 or not legal :

            self.set_override_signal('N')
            return False

        else:
            self.set_override_signal('Y')
            return True


    def verify_password(self):
        if self.get_new_pas()==self.get_new_pas2():
            self.set_override_signal('Y')
            self.change_pw(self.get_new_pas2())
            self.twinkle_leds()

        else:
            self.set_override_signal('N')
            self.Led_board.wrong_password()


    def change_pw(self, password):
        password = str(password)
        pw = open(self.path, "w")
        pw.write(password)
        pw.close()

    # ledNr is the Led number, ledDr is the led Duration
    # midlertidig

    def light_one_led(self):
        print("Light number " + str(self.LEDid + 1) + " for " + str(self.light_duration) + " milliseconds")

    def set_LED(self):
        self.LEDid=int(self.get_next_signal())

    def set_duration(self):
        sym=self.get_next_signal()
        while signal_is_digit(sym):
            self.light_duration+=sym
            sym=self.get_next_signal()
        self.light_duration = int(sym)


    #request the flashing of all LEDs
    # midlertidig
    def flash_leds(self):
        print("all lights are flashing")

    #request the twinkling of all LEDs.
    def twinkle_leds(self):
        self.Led_board.twinkle_all_leds(self)

    #initiate the ”power down” lighting sequence.

    def exit_action(self):
        self.reset_agent()
        self.Led_board.power_down(self)






def signal_is_digit(signal): return 48 <= ord(signal) <= 57
def signal_is_any(signal): return signal_is_digit(signal) or signal == "*" or signal == "#"
def signal_is_led(signal): return 48 <= ord(signal) <= 53
def is_hashtag(signal): return signal == "#"
def is_star(signal): return signal == "*"

kpc = KPC()
print(kpc.get_next_signal())
print(kpc.get_next_signal())
print(kpc.get_next_signal())
print(kpc.get_next_signal())
print(kpc.get_next_signal())