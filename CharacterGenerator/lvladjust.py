import random


def hitpointsadj(con_bonus, lvl, job):
    # Compute the hit points for any given class.
    hp = 0
    if job == 'Fighter':
        hp = 10 + con_bonus
        print("Constitution Bonus - ", con_bonus)
        print("First level HP - ", hp)
        if lvl > 1:
            for i in range(lvl - 1):
                y = random.randint(1, 10)
                x = random.randint(1, 10)
                print("Level-", i + 2, ": Roll one =", y, " Roll two =", x)
                if y > 4:
                    hp = hp + y + con_bonus
                else:
                    hp = hp + x + con_bonus
                print("Level-", i + 2, ": HP = ", hp)

    if job == 'Wizard':
        hp = 4 + con_bonus
        print("Constitution Bonus - ", con_bonus)
        print("First level HP - ", hp)
        if lvl > 1:
            for i in range(lvl - 1):
                y = random.randint(1, 4)
                x = random.randint(1, 4)
                print("Level-", i + 2, ": Roll one =", y, " Roll two =", x)
                if y > 1:
                    hp = hp + y + con_bonus
                else:
                    hp = hp + x + con_bonus
                print("Level-", i + 2, ": HP = ", hp)

    if job == 'Cleric':
        hp = 8 + con_bonus
        print("Constitution Bonus - ", con_bonus)
        print("First level HP - ", hp)
        if lvl > 1:
            for i in range(lvl - 1):
                y = random.randint(1, 8)
                x = random.randint(1, 8)
                print("Level-", i + 2, ": Roll one =", y, " Roll two =", x)
                if y > 3:
                    hp = hp + y + con_bonus
                else:
                    hp = hp + x + con_bonus
                print("Level-", i + 2, ": HP = ", hp)

    if job == 'Rogue':
        hp = 6 + con_bonus
        print("Constitution Bonus - ", con_bonus)
        print("First level HP - ", hp)
        if lvl > 1:
            for i in range(lvl - 1):
                y = random.randint(1, 6)
                x = random.randint(1, 6)
                print("Level-", i + 2, ": Roll one =", y, " Roll two =", x)
                if y > 2:
                    hp = hp + y + con_bonus
                else:
                    hp = hp + x + con_bonus
                print("Level-", i + 2, ": HP = ", hp)

    return hp


def skillsadj(job, intel_bonus, lvl):
    sktotal = 0
    if job == 'Fighter' or job == 'Cleric' or job == 'Wizard' and lvl > 1:
        sktotal = (2 + intel_bonus) * lvl

    if job == 'Rogue' and lvl > 1:
        sktotal = (8 + intel_bonus) * lvl

    return sktotal


def featadj(lvl, job, race):
    # Computes how many feats the character get to pick/
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
    # This computes how man additional ability points for higher level characters
    abi_inc = 0
    for i in range(lvl):
        if (i + 1) % 4 == 0:
            abi_inc += 1

    return abi_inc


def strt_gold(lvl, wealth_type):
    # NPC starting gold from p 127 dm guide.
    npc_wealth = {1: 900, 2: 2000, 3: 2500, 4: 3300, 5: 4300, 6: 5600, 7: 7200,
                  8: 9400, 9: 12000, 10: 16000, 11: 21000, 12: 27000, 13: 35000,
                  14: 45000, 15: 59000, 16: 77000, 17: 100000, 18: 130000, 19: 170000,
                  20: 220000}

    pc_wealth = {1: 900, 2: 900, 3: 2700, 4: 5400, 5: 9000, 6: 13000, 7: 19000, 8: 27000,
                 9: 36000, 10: 49000, 11: 66000, 12: 88000, 13: 110000, 14: 150000, 15: 200000,
                 16: 260000, 17: 340000, 18: 440000, 19: 580000, 20: 760000}

    if wealth_type == 'NPC':
        gold = npc_wealth[lvl]
    else:
        gold = pc_wealth[lvl]

    return "{:0,.0f}".format(gold)
