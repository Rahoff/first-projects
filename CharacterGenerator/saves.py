def fightersaves(lvl):
    fort = 0
    ref = 0
    will = 0
    if lvl > 0:
        fort = 2
        ref = 0
        will = 0
    if lvl >= 2:
        fort += 1
        ref += 0
        will += 0
    if lvl >= 3:
        fort += 0
        ref += 1
        will += 1
    if lvl >= 4:
        fort += 1
        ref += 0
        will += 0
    if lvl >= 5:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 6:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 7:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 8:
        fort += 1
        ref += 0
        will += 0
    if lvl >= 9:
        fort += 0
        ref += 1
        will += 1
    if lvl >= 10:
        fort += 1
        ref += 0
        will += 0
    if lvl >= 11:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 12:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 13:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 14:
        fort += 1
        ref += 0
        will += 0
    if lvl >= 15:
        fort += 0
        ref += 1
        will += 1
    if lvl >= 16:
        fort += 1
        ref += 0
        will += 0
    if lvl >= 17:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 18:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 19:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 20:
        fort += 1
        ref += 0
        will += 0
    return [fort, ref, will]


def wizsaves(lvl):
    fort = 0
    ref = 0
    will = 0
    if lvl > 0:
        fort = 0
        ref = 0
        will = 2
    if lvl >= 2:
        fort += 0
        ref += 0
        will += 1
    if lvl >= 3:
        fort += 1
        ref += 1
        will += 0
    if lvl >= 4:
        fort += 0
        ref += 0
        will += 1
    if lvl >= 5:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 6:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 7:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 8:
        fort += 0
        ref += 0
        will += 1
    if lvl >= 9:
        fort += 1
        ref += 1
        will += 0
    if lvl >= 10:
        fort += 0
        ref += 0
        will += 1
    if lvl >= 11:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 12:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 13:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 14:
        fort += 0
        ref += 0
        will += 1
    if lvl >= 15:
        fort += 1
        ref += 1
        will += 0
    if lvl >= 16:
        fort += 0
        ref += 0
        will += 1
    if lvl >= 17:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 18:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 19:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 20:
        fort += 0
        ref += 0
        will += 1
    return [fort, ref, will]


def roguesaves(lvl):
    fort = 0
    ref = 0
    will = 0
    if lvl > 0:
        fort = 0
        ref = 2
        will = 0
    if lvl >= 2:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 3:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 4:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 5:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 6:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 7:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 8:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 9:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 10:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 11:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 12:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 13:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 14:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 15:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 16:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 17:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 18:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 19:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 20:
        fort += 0
        ref += 1
        will += 0
    return [fort, ref, will]


def clericsaves(lvl):
    fort = 0
    ref = 0
    will = 0
    if lvl > 0:
        fort = 2
        ref = 0
        will = 2
    if lvl >= 2:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 3:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 4:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 5:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 6:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 7:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 8:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 9:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 10:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 11:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 12:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 13:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 14:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 15:
        fort += 0
        ref += 1
        will += 0
    if lvl >= 16:
        fort += 1
        ref += 0
        will += 1
    if lvl >= 17:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 18:
        fort += 1
        ref += 1
        will += 1
    if lvl >= 19:
        fort += 0
        ref += 0
        will += 0
    if lvl >= 20:
        fort += 1
        ref += 0
        will += 1
    return [fort, ref, will]