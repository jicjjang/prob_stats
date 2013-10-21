import random
import math

def couple_height_random():
    return random.normalvariate(178, math.sqrt(59.4)), random.normalvariate(163, math.sqrt(52.8))

if __name__=='__main__':
    nsamples = 100000
    couple_height = [couple_height_random() for x in range(nsamples)]

    couple_woman_taller = [(man, woman) for (man, woman) in couple_height if woman > man]

    print 'taller women:', len(couple_woman_taller) / float(nsamples)

    print 'coefficient of variation'
    print 'men:', math.sqrt(59.4)/178
    print 'women:', math.sqrt(52.8)/163
