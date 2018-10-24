#Finite State Machine
#simone sin branch?

from Rule import*
from KPC import*

class FSM:

    # bruker ikke denne listen til noe, bare for å holde oversikt
    possible_states = ["S_init", "S_Read", "S-verify", "S-active",
                       "S-Read2", "S-Validate", "S-Rule3",
                       "S-verify-new-pw", "S-Lid", "S-time", "S-logout"]
    def __init__(self, kpc):
        self.kpc = kpc
        self.state = "S-init"
        self.rule_book = []

    # add a new rule to the end of the FSM’s rule list.
    def add_rule(self, state1, state2, symbol, action):
        rule = Rule(state1, state2, symbol, action, self.kpc)
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
                print(rule.show_rule())
                self.fire_rule(rule)
                match = True
                break
        if match == False:
            print('no rules matched :( ')


    # check whether the conditions of a rule are met
    def apply_rule(self):
        return

    # use the consequent of a rule to a) set the next state of the FSM, and b) call the appropriate agent action method.
    def fire_rule(self, rule):
        rule.do_action()
        self.state = rule.get_next_state()
        return

    # begin in the FSM’s default initial state and then repeatedly call get next signal and run rules until the FSM enters its default final state.
def main_loop():
    kpc = KPC()
    fsm = FSM(kpc)
    # Håndterer innlogging. Man kommer enten videre til active eller så går man tilbake til starten.
    fsm.add_rule("S-init", "S-read", "#", KPC.init_passcode_entry)
    fsm.add_rule("S-read", "S-read", "digits", KPC.pw_attempt)
    fsm.add_rule("S-read", "S-verify", "*", KPC.verify_login)
    fsm.add_rule("S-verify", "S-active", "Y", KPC.go_to_active)
    fsm.add_rule("S-verify", "S-init", "N", KPC.go_back_to_start)
    fsm.add_rule("S-read", "S-init", "#", KPC.go_back_to_start)

    # Håndterer lysene. Vil lyse opp lys om man trykker korrekt. Går ellers tilbae til active.
    fsm.add_rule("S-active", "S-led", "Lid", KPC.set_LED)
    fsm.add_rule("S-led", "S-time", "digits", KPC.record_duration)
    fsm.add_rule("S-led", "S-active", "any", KPC.go_back_to_active)
    fsm.add_rule("S-time", "S-time", "digits", KPC.record_duration)
    fsm.add_rule("S-time", "S-active", "*", KPC.set_duration)
    fsm.add_rule("S-time", "S-active", "any", KPC.go_back_to_active)

    # Skal håndtere passordbytte.
    fsm.add_rule("S-active", "S-read2", "*", KPC.init_new_passcode_entry)
    fsm.add_rule("S-read2", "S-read2", "digits", KPC.new_pw)
    fsm.add_rule("S-read2", "S-validate", "*", KPC.validate_passcode_change)
    fsm.add_rule("S-read2", "S-active", "any", KPC.go_back_to_active)
    fsm.add_rule("S-validate", "S-read3", "Y", KPC.init_retype_passcode_entry)
    fsm.add_rule("S-validate", "S-active", "N", KPC.go_back_to_active)
    fsm.add_rule("S-read3", "S-read3", "digits", KPC.retype_new_pw)
    fsm.add_rule("S-read3", "S-verify", "*", KPC.verify_password)  # Hvis verified vil verify_password endre passord
    fsm.add_rule("S-read3", "S-active", "any", KPC.go_back_to_active)
    # Går tilbake til aktiv uansett om passord byttes eller ikke:
    fsm.add_rule("S-verify", "S-active", "any", KPC.does_allmost_nothing)

    # Logger ut
    fsm.add_rule("S-active", "S-logout", "#", KPC.want_to_logout)
    fsm.add_rule("S-active", "S-active", "any", KPC.does_allmost_nothing)
    fsm.add_rule("S-logout", "S-end", "#", KPC.exit_action)
    fsm.add_rule("S-logout", "S-active", "any", KPC.go_back_to_active)

    print("--------")
    print("current state: " + fsm.state)
    print("--------")

    while not (fsm.state == "S-end"):
        symbol = kpc.get_next_signal()
        print("symbol is: " + symbol)
        fsm.run_rules(fsm.state, symbol)
        print("--------")
        print("current state: " + fsm.state)
        print("--------")
        time.sleep(1)
    return



if __name__ == "__main__":
    main_loop()

