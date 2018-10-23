
class Rule:

    def __init__(self, state1, state2, symbol, action):
        self.state1 = state1
        self.state2 = state2
        self.symbol = symbol
        self.action = action

    def isTrue(self, current_state, symbol):

