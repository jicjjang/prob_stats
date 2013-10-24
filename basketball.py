import random

def oneplayer_10_inarow():
    shots = []
    for x in range(15):
        r = random.random()
        if r < 0.5:
            shots.append(1)
        else:
            shots.append(0)

    #print shots

    ten_in_a_row = 0
    for x in range(6):
        if sum(shots[x:x+10]) == 10:
            ten_in_a_row += 1

    return ten_in_a_row


def onegame():
    all_player = 0
    for player in range(10):
        if oneplayer_10_inarow() > 0:
            all_player += 1

    return all_player

def oneseason():
    hit = 0
    for x in range(82):
        if onegame() > 0:
            hit += 1

    return hit

if __name__=='__main__':
    s = 0
    ntrials = 1000
    for x in range(ntrials):
        if onegame() > 0:
            s += 1;

    print s/float(ntrials)

    s = 0
    for x in range(ntrials):
        if oneseason() > 0:
            s += 1;

    print s/float(ntrials)            
    
