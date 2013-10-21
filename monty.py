import random
import math

def monty_hall(inform=True):
    doors = [1, 0, 0]
    random.shuffle(doors)

    #print doors

    sel_first = math.trunc(random.random() * 3)

    #print sel_first

    sels = [(1,2), (0,2), (0,1)]

    if inform == True: # Monty knows which door has a prize, and opens a door which has no prize
        if doors[sels[sel_first][0]] == 1:
            opened = sels[sel_first][1]
            sel_switch = sels[sel_first][0]
        elif doors[sels[sel_first][1]] == 1:
            opened = sels[sel_first][0]
            sel_switch = sels[sel_first][1]
        else:
            x = math.trunc(random.random() * 2)
            opened = sels[sel_first][x]
            sel_switch = sels[sel_first][abs(x-1)]
    else: # Monty opens door randomly
        x = math.trunc(random.random() * 2)
        opened = sels[sel_first][x]
        sel_switch = sels[sel_first][abs(x-1)]

    #print opened, sel_switch

    if doors[sel_first] == 1:
        return 1, 0  # stick win, 
    elif doors[sel_switch] == 1:
        return 0, 1  # switch win
    else:
        return 0, 0  # Monty win ^^;

if __name__=='__main__':
    trials = 10000
    stick_win = 0
    switch_win = 0

    print 'Monty Knows which door has a prize!'
    for i in range(trials):
        f, s = monty_hall()
        stick_win += f
        switch_win += s
    print stick_win/float(trials), switch_win/float(trials)

    print 'Monty Does Not Know which door has a prize!'
    stick_win = 0
    switch_win = 0
    for i in range(trials):
        f, s = monty_hall(False)
        stick_win += f
        switch_win += s
    print stick_win/float(trials), switch_win/float(trials)
    
