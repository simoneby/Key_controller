#Finite State Machine
from Rule import*
from KPC import*

class FSM:

    # bruker ikke denne listen til noe, bare for å holde oversikt
    possible_states = ["S_init", "S_Read", "S-verify", "S-active",
                       "S-Read2", "S-Validate", "S-Rule3",
                       "S-verify-new-pw", "S-Lid", "S-time", "S-logout"]
    rule_book = []

    # add a new rule to the end of the FSM’s rule list.
    def add_rule(self, state1, state2, symbol, action):
        rule = Rule(state1, state2, symbol, action)
        self.rule_book.append(rule)
        return

    # query the agent for the next signal.
    def get_next_signal(self):
        return

    # go through the rule set, in order, applying each rule until one of the rules is fired.
    def run_rules(self):
        return

    # check whether the conditions of a rule are met
    def apply_rule(self):
        return

    # use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method.
    def fire_rule(self):
        return

    # begin in the FSM’s default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.
    def main_loop(self):
        return

fsm = FSM()
fsm.add_rule("S-init", "S-read", "any", KPC.does_nothing())

