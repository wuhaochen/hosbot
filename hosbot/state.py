import time

import hoscon
import utils

class GameState(object):
    def __init__(self, name, identifiers, action):
        self.name = name
        self.identifiers = identifiers
        self.action = action

    def is_current_state(self):
        return all([utils.get_pixel_rgb(pos) == rgb
                    for pos, rgb in self.identifiers])


class DefaultGameState(GameState):
    def __init__(self, name, action):
        self.name = name
        self.action = action

    def is_current_state(self):
        return True


def do_at_start_menu():
    x, y = hoscon.pos.SELECTION
    utils.left_click(x, y)
    time.sleep(0.5)
    while startmenu.is_current_state():
        y += 50
        if y > 1000:
            print('Cannnot get into selection, start directly.')
            x, y = hoscon.pos.START
            utils.left_click(x, y)
        utils.left_click(x, y)
        time.sleep(0.5)

startmenu = GameState(name='Start Menu',
                      identifiers=hoscon.states.STARTMENU,
                      action=do_at_start_menu)


def do_at_selection_menu():
    x, y = hoscon.pos.SORTLVLUP
    utils.left_click(x, y)
    time.sleep(0.5)
    x, y = hoscon.pos.FIRSTHERO
    utils.left_click(x, y)
    time.sleep(0.5)
    x, y = hoscon.pos.START
    utils.left_click(x, y)
    time.sleep(10)

selectionmenu = GameState(name='Selection Menu',
                          identifiers=hoscon.states.SELECTIONMENU,
                          action=do_at_selection_menu)


def do_at_end_menu():
    x, y = hoscon.pos.LEAVEEND
    utils.left_click(x, y)

endmenu = GameState(name='Exit Menu',
                    identifiers=hoscon.states.ENDMENU,
                    action=do_at_end_menu)


def do_at_exp_menu():
    x, y = hoscon.pos.LEAVEEXP
    utils.left_click(x, y)

expmenu = GameState(name='Exp Menu',
                    identifiers=hoscon.states.EXPMENU,
                    action=do_at_exp_menu)


def do_at_inactive():
    x, y = hoscon.pos.REJOIN
    utils.left_click(x, y)

inactivemenu = GameState(name='Inactive Menu',
                         identifiers=hoscon.states.INACTIVE,
                         action=do_at_inactive)


def do_at_other():
    x, y = utils.get_attack_pos()
    utils.left_click(x, y)
    time.sleep(0.2)
    utils.keystroke(ord('Z'))
    time.sleep(0.5)
    utils.keystroke(ord('A'))
    time.sleep(0.5)
    utils.left_click(x, y)

default = DefaultGameState(name='Other', action=do_at_other)