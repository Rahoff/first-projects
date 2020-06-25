import random


def hitpointsadj(con_bonus, lvl, job):
    hp = 0
    if job == 'Fighter':
        hp = 10 + con_bonus
        if lvl > 1:
            for i in range(lvl - 1):
                hp = hp + random.randint(1, 10) + con_bonus
    if job == 'Wizard':
        hp = 4 + con_bonus
        if lvl > 1:
            for i in range(lvl - 1):
                hp = hp + random.randint(1, 4) + con_bonus
    if job == 'Cleric':
        hp = 8 + con_bonus
        if lvl > 1:
            for i in range(lvl - 1):
                hp = hp + random.randint(1, 8) + con_bonus
    if job == 'Rogue':
        hp = 6 + con_bonus
        if lvl > 1:
            for i in range(lvl - 1):
                hp = hp + random.randint(1, 6) + con_bonus

    return hp


def skillsadj(job, intel_bonus, lvl):
    sktotal = 0
    if job == 'Fighter' or job == 'Cleric' or job == 'Wizard' and lvl > 1:
        sktotal = (2 + intel_bonus) * lvl

    if job == 'Rogue' and lvl > 1:
        sktotal = (8 + intel_bonus) * lvl

    return sktotal


def featadj(lvl, job, race):
    bonusfeats = 0
    start_feats = 1

    if race == 'Human':
        start_feats += 1

    if job == 'Fighter':
        start_feats += 1
        for i in range(lvl):
            if (i + 1) % 2 == 0:
                bonusfeats += 1
    if job == 'Wizard':
        for i in range(lvl):
            if (i + 1) % 5 == 0:
                bonusfeats += 1

    for i in range(lvl):
        if (i + 1) % 3 == 0:
            bonusfeats += 1

    return bonusfeats + start_feats


def ability_increase(lvl):
    abi_inc = 0
    for i in range(lvl):
        if (i + 1) % 4 == 0:
            abi_inc += 1

    return abi_inc