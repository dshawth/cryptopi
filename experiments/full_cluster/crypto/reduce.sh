#!/usr/bin/env bash

for i in {0..9}; do
    grep aes-cbc r$i.txt > aes/c$i.txt
    grep serpent-cbc r$i.txt > serpent/c$i.txt
    grep twofish-cbc r$i.txt > twofish/c$i.txt
done
