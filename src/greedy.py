from datetime import time, datetime
from operator import attrgetter
import csv


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
with open('src/data.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        KRLs.append(KRL(s2tm(row[0]),
                        s2tm(row[1]),
                        int(row[2])))


print('Maksimum berhenti: ' + str(max_KRL_in_station(KRLs, 7)))
