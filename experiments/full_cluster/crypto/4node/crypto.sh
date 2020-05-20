#!/usr/bin/env bash

for i in {0..9}; do
    bash dmux.sh ubuntu 172.31.42.1-4 'cryptsetup benchmark' > r$i.txt
done
