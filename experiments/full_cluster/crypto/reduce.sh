#!/usr/bin/env bash

for i in {0..9}; do
    grep aes-cbc r$i.txt > c$i.txt
done
