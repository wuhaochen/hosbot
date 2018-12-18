import time
import win32con

import hoscon
import utils

class HoSBot(object):
    def __init__(self, states):
        self.states = states


    def is_enabled(self):
        return not utils.is_keydown(win32con.VK_LCONTROL)


    def stepforward(self):
        for state in self.states:
            if state.is_current_state():
                state.action()
                break
        time.sleep(1)


    def run(self):
        while self.is_enabled():
            self.stepforward()