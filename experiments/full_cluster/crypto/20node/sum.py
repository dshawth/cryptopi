#!/usr/bin/env python3

import os

runs = 10

for alg in ['aes', 'serpent', 'twofish']:
    enc128 = []
    dec128 = []
    enc256 = []
    dec256 = []  
    for fileName in sorted(os.listdir(alg)):
        with open(os.path.join(alg, fileName)) as data:
            for line in data.readlines():
                line = line.split()
                if line[1] == '128b':
                    enc128.append(float(line[2]))
                    dec128.append(float(line[4]))
                if line[1] == '256b':
                    enc256.append(float(line[2]))
                    dec256.append(float(line[4]))
    # output
    print(alg,'enc','128b',round(sum(enc128)/runs, 2))
    print(alg,'dec','128b',round(sum(dec128)/runs, 2))
    print(alg,'enc','256b',round(sum(enc256)/runs, 2))
    print(alg,'dec','256b',round(sum(dec256)/runs, 2))

