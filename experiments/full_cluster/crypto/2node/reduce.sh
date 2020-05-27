#!/usr/bin/env bash

# make directories to hold the raw data
mkdir -p aes serpent twofish

# for each iteration of cryptsetup benchmark
for i in {0..9}; do
    grep aes-cbc raw/r$i.txt > aes/c$i.txt
    grep serpent-cbc raw/r$i.txt > serpent/c$i.txt
    grep twofish-cbc raw/r$i.txt > twofish/c$i.txt
done
