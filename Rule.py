from KPC import *


class Rule:

    # symbol er det eller de symbolene som gjør at man går til neste state
    # action er handlingen som utføres når regelen fyres
    def __init__(self, state1, state2, symbol, action):
        self.dict = {"any": signal_is_any(), "digits": signal_is_digit(), "Lid": signal_is_led(), "#": is_hashtag(),
                     "*": is_star()}
        self.state1 = state1
        self.state2 = state2
        self.allowed_symbols = symbol
        self.action = action

    def match(self, current_state, symbol):
        if current_state == self.state1 and self.dict[self.allowed_symbols](symbol):
            return True
        else:
            return False

    def symbol_match(self, symbol):
        if self.allowed_symbols == "any":
            return signal_is_any(symbol)
        elif self.allowed_symbols == "digits":
            return signal_is_digit(symbol)
        elif self.allowed_symbols(symbol) == "Lid":
            return signal_is_led(symbol)
        elif self.allowed_symbols == "#":
            return "#" == symbol
        elif self.allowed_symbols == "*":
            return "*" == symbol

    def get_next_state(self):
        return self.state2

    def do_action(self):
        self.action()
