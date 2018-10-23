
class Rule:

    # symbol er det eller de symbolene som gjør at man går til neste state
    # action er handlingen som utføres når regelen fyres


    def __init__(self, state1, state2, symbol, action):
        self.state1 = state1
        self.state2 = state2
        self.allowed_symbols = symbol
        self.action = action

    def match(self, current_state, symbol):
        if current_state == self.state1 and (self.allowed_symbols == symbol or self.allowed_symbols(symbol) == True)
            return True
        else
            return False

    def get_next_state(self):
        return self.state2

    def do_action(self):
        self.action()



