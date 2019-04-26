from datetime import time, datetime
from operator import attrgetter


class KRL:
    def __init__(self, tiba, berangkat, lajur):
        self.tiba = tiba
        self.berangkat = berangkat
        self.lajur = lajur


def max_KRL_in_station(KRLs, n):
    lajurs = {}
    for krl in KRLs:  # group KRLs by its platform
        if krl.lajur in lajurs:
            lajurs[krl.lajur].append(krl)
        else:
            lajurs[krl.lajur] = [krl]
    count_max = 0
    for lajur, krl in lajurs.items():
        krl_sorted = sorted(krl, key=attrgetter('berangkat'))
        count_max += 1  # select first KRL in each platform
        x = 0  # current KRL examined
        for j in range(1, len(krl_sorted)):
            if krl_sorted[j].tiba >= krl_sorted[x].berangkat:
                x = j
                count_max += 1
    return count_max


def s2tm(s):
    return datetime.strptime(s, '%H:%M').time()


KRLs = []
KRLs.append(KRL(s2tm('10:10'), s2tm('10:30'), 1))
KRLs.append(KRL(s2tm('10:10'), s2tm('10:30'), 1))
KRLs.append(KRL(s2tm('10:00'), s2tm('10:20'), 2))
KRLs.append(KRL(s2tm('10:30'), s2tm('12:30'), 2))
KRLs.append(KRL(s2tm('12:10'), s2tm('12:30'), 3))
KRLs.append(KRL(s2tm('09:00'), s2tm('10:05'), 1))

print('Maksimum berhenti: ' + str(max_KRL_in_station(KRLs, 6)))
