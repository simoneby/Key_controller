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
        rule.show_rule()
        self.rule_book.append(rule)
        return

    # query the agent for the next signal.
    def get_next_signal(self):
        return

    # go through the rule set, in order, applying each rule until one of the rules is fired.
    def run_rules(self, current_state, symbol):
        match = False
        for rule in self.rule_book:
            if rule.match(current_state, symbol):
                self.fire_rule(rule)
                print("rule matched!")
                match = True
        if match == False:
            print('no rules matched :( ')


    # check whether the conditions of a rule are met
    def apply_rule(self):
        return

    # use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method.
    def fire_rule(self, rule):
        rule.do_action()
        return

    # begin in the FSM’s default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.
    def main_loop(self):
        return

fsm = FSM()
fsm.add_rule("S-init", "S-read", "any", KPC.init_passcode_entry)
fsm.add_rule("S-read", "S-read", "digits", KPC.pw_attempt)
fsm.add_rule("S-read", "S-verify", "*", KPC.verify_login)
fsm.add_rule("S-read", "S-init", "#", KPC.does_allmost_nothing)
fsm.add_rule("S-verify", "S-active", "Y", ??)
fsm.add_rule("S-verify", "S-init", "any", KPC.does_allmost_nothing)
fsm.add_rule("S-active", "S-logout", "#", ??)
fsm.add_rule("S-logout", "S-init", "#", ??)
fsm.add_rule("S-logout", "S-active", "any", ??)
fsm.add_rule("S-active", "S-lid", "Lid", ??)
fsm.add_rule("S-lid", "S-time", ??, ??)
fsm.add_rule("S-lid", "S-active", "any", ??) #refresh_agent?
fsm.add_rule("S-time", "S-active", "*", ??) #gjør action her
fsm.add_rule("S-time", "S-active", "any", KPC.does_allmost_nothing) #refresh_agent?
fsm.add_rule("S-active", "S-read2", "*", ??)
fsm.add_rule("S-read2", "S-read2", "digits", ??)
fsm.add_rule("S-read2", "S-validate", "*", ??)
fsm.add_rule("S-read2", "S-active", "any", ??) #refresh_agent?
fsm.add_rule("S-validate", "S-read3", "Y", ??)
fsm.add_rule("S-validate", "S-active", "any", KPC.does_allmost_nothing) #refresh_agent?
fsm.add_rule("S-read3", )










fsm.run_rules("S-init", "3")

