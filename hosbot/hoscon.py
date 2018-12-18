class UIPositions(object):
    GAMEMENU = (115, 35)
    START = (955, 1005)
    LEAVEEND = (110, 1035)
    LEAVEEXP = (155, 1010)
    REJOIN = (860, 622)
    SELECTION = (1000, 600)
    SORTLVLUP = (1333, 160)
    FIRSTHERO = (349, 258)


pos = UIPositions


class StatePixels(object):
    """Sample a few pixels to help determning current state.

    Each constant is a list of (pos, rgb) samples. If all pos match sample,
    we are confident it is in the given state.
    """
    STARTMENU = [((43, 34), (254, 158, 170)),
                 ((37, 32), (254, 164, 175)),
                 ((49, 44), (50, 5, 24)),
                 ((107, 34), (255, 242, 227))]
    SELECTIONMENU = [((43, 34), (0, 0, 0)),
                     ((1896, 25), (0, 0, 0)),
                     ((970, 1005), (225, 175, 180))]
    ENDMENU = [((91, 1035), (97, 24, 46)),
                 ((105, 1033), (123, 91, 96)),
                 ((112, 1035), (116, 29, 51))]
    EXPMENU = [((43, 35), (252, 140, 153)),
               ((35, 27), (254, 158, 168)),
               ((140, 1012), (255, 202, 207))]
    INACTIVE = [((851, 472), (255, 242, 228)),
                ((866, 625), (1, 0, 0)),
                ((860, 622), (123, 33, 59))]

states = StatePixels