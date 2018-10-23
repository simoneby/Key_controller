#Finite State Machine

class FSM():

    # add a new rule to the end of the FSM’s rule list.
    def add_rule(self):
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
