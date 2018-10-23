#Key Pad Controller

from LED_board import *

#from Key_controller.Keypad import Keypad
#notes from jen
#har laget noen gettere, vet ikke om det er behov for det
#burde i så fall lage noen settere også
#usikker på om tallene og passordene skal gis i streng eller i tall
#det står at passordet burde lagres i en fil, vil vi dette?

from Keypad import *

class KPC:


    def __init__(self):
        self.Led_board = LED_board()
        self.keypad=Keypad()
        self.override_signal=None
        self.CUMP=None
        self.CP=""
        self.new_pas=""
        self.new_pas2=""
        self.path = "pw.txt" #path to filename

        self.LEDid=None
        self.light_duration=None

        # setter opp keypad kun en gang
        self.keypad.setup()

    # Clear the passcode-buffer and initiate a ”power up” lighting sequence on the LED Board.
    # This should be done when the user first presses the keypad.
    # starter ved å trykke på firkant
    def init_passcode_entry(self):
        if self.keypad.get_next_signal()=='#':
            self.CUMP=None
            self.CUMP_OLD=None
            self.set_override_signal(None)
            self.Led_board.power_up()

<<<<<<< HEAD

    def set_override_signal(self,c):
        self.override_signal=c

=======
    def set_override_signal(self,c):
        self.override_signal=c


>>>>>>> 6bee2fc75349a92396872f60f4494196a3c197dd
    def get_override_signal(self):
        return self.override_signal

    def reset_agent(self):
        self.CUMP=None
        self.set_override_signal(None)



    # Return the override-signal, if it is non-blank; otherwise query the keypad for the next pressed key.
    def get_next_signal(self):
        signal=None
        if self.get_override_signal()==None:
             signal=self.keypad.get_next_signal()
        else:
            signal=self.get_override_signal()
        return signal


    #får inn hele passordet eller legger til underveis?
    def store_CUMP(self,number):
        self.CUMP+=number

    #parser til string her
    def get_CUMP(self):
        return str(self.CUMP)

<<<<<<< HEAD
    def get_new_pas(self):
        return self.new_pas

    def get_new_pas2(self):
        return self.new_pas2

    def set_new_pas(self,pas):
        self.new_pas=pas

    def set_new_pas2(self,pas):
        self.new_pas2=pas
=======
    def does_nothing():
        return
>>>>>>> 6bee2fc75349a92396872f60f4494196a3c197dd

    def get_CP(self):
        pw = open(self.path, "r")
        self.CP = pw.readline()
        pw.close()
        return self.CP

    def enter_new_password(self):
        pas=None
        np=self.keypad.get_next_signal()
        while np!='*':
            pas+=np
        self.set_new_pas(pas)

    # Check that the password just entered via the keypad matches that in the password file.
    # Store the result (Y or N) in the override-signal.
    # initiate the appropriate lighting pattern for login success or failure.
    def verify_login(self):
        if self.get_CUMP()==self.get_CP():
            self.set_override_signal('Y')
            self.twinkle_leds()
        else:
            self.set_override_signal('N')
            self.Led_board.wrong_password()
            self.reset_agent()

    #Check that the new password is legal. If so, write the new password in the password file.
    # A legal password should be at least 4 digits long and should contain no symbols other than the digits 0-9.
    # denne skal sjekkes to ganger?
    def validate_passcode_change(self):
        legal=False
        for digit in self.get_new_pas():
                legal=signal_is_digit(digit)

        if len(self.get_new_pas())<4 or not legal :
            self.refresh_agent()
            self.set_override_signal('N')
            return False

        else:
            self.set_override_signal('Y')
            return True

    def enter_new_password2(self):
        if self.validate_passcode_change():
            pas=None
            np=self.keypad.get_next_signal()
            while np!='*':
                pas+=np
                self.set_new_pas2(pas)

    def verify_password(self):
        if self.get_new_pas()==self.get_new_pas2():
            self.set_override_signal('Y')
            self.change_pw(self.get_new_pas2())
            self.twinkle_leds()
            self.refresh_agent()
        else:
            self.set_override_signal('N')
            self.Led_board.wrong_password()
            #skal tilbake til s-read3 her?



    def refresh_agent(self):
        self.set_override_signal(None)
        self.new_pas=None
        self.new_pas2=None

    def change_pw(self, password):
        password = str(password)
        pw = open(self.path, "w")
        pw.write(password)
        pw.close()

    # ledNr is the Led number, ledDr is the led Duration
    # midlertidig

    def light_one_led(self, ledNr, ledDr):
        print("Light number " + str(ledNr + 1) + " for " + str(ledDr) + " milliseconds")


    #request the flashing of all LEDs
    # midlertidig
    def flash_leds(self):
        print("all lights are flashing")

    #request the twinkling of all LEDs.
    def twinkle_leds(self):
        self.Led_board.twinkle_all_leds(self)

    #initiate the ”power down” lighting sequence.

    def exit_action(self):
        self.Led_board.power_down(self)

    #def reset(self):




def signal_is_digit(signal): return 48 <= ord(signal) <= 57
def signal_is_any(signal): return signal_is_digit(signal) or signal == "*" or signal == "#"
def signal_is_led(signal): return 48 <= ord(signal) <= 53

print(signal_is_any("3"))
print(signal_is_any("%"))
print(signal_is_any("#"))
print(signal_is_digit("9"))
print(signal_is_led("3"))
