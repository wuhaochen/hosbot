import sys
import time

import bot
import state

def main():
    states = []
    states.append(state.startmenu)
    states.append(state.selectionmenu)
    states.append(state.endmenu)
    states.append(state.expmenu)
    states.append(state.inactivemenu)
    states.append(state.default)

    shady_bot = bot.HoSBot(states)
    shady_bot.run()
    print('Exit!')

if __name__ == '__main__':
    if len(sys.argv) > 1:
        wait = int(sys.argv[1])
        print("Delay {}s.".format(wait))
        time.sleep(wait)
    print('Start execution.')
    main()