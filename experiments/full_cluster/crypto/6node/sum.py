#!/usr/bin/env python3

import os

runs = 10

if os.path.exists('results.txt'):
    os.remove('results.txt')

for alg in ['aes', 'serpent', 'twofish']:
    enc128 = []
    dec128 = []
    enc256 = []
    dec256 = []  

    for fileName in sorted(os.listdir(alg)):
        with open(os.path.join(alg, fileName)) as inFile:
            for line in inFile.readlines():
                line = line.split()
                if line[1] == '128b':
                    enc128.append(float(line[2]))
                    dec128.append(float(line[4]))
                if line[1] == '256b':
                    enc256.append(float(line[2]))
                    dec256.append(float(line[4]))

    with open('results.txt', 'a') as outFile:
        outFile.write('{alg} enc 128b {result}\n'.format(alg=alg, result=round(sum(enc128)/runs, 2)))
        outFile.write('{alg} dec 128b {result}\n'.format(alg=alg, result=round(sum(dec128)/runs, 2)))
        outFile.write('{alg} enc 256b {result}\n'.format(alg=alg, result=round(sum(enc256)/runs, 2)))
        outFile.write('{alg} dec 256b {result}\n'.format(alg=alg, result=round(sum(dec256)/runs, 2)))
