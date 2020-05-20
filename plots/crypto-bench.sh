#!/usr/bin/env bash

# ./crypto-bench.sh | tee tmp-cr
# cat tmp-cr | tail -n 6 > crypto-results
# rm tmp-cr

# results arrays
aes_enc=()
aes_dec=()
serpent_enc=()
serpent_dec=()
twofish_enc=()
twofish_dec=()

for i in {1..10}; do

    # tempfile
    tmp=$(mktemp)
    
    # use dmux to run the benchmark on all cluster nodes
    bash dmux.sh 'cryptsetup benchmark' ${tmp}

    aes_enc+=($(awk '/aes-cbc/ && /256b/ {print $3}' ${tmp} | paste -sd+ | bc))
    aes_dec+=($(awk '/aes-cbc/ && /256b/ {print $5}' ${tmp} | paste -sd+ | bc))

    serpent_enc+=($(awk '/serpent-cbc/ && /256b/ {print $3}' ${tmp} | paste -sd+ | bc))
    serpent_dec+=($(awk '/serpent-cbc/ && /256b/ {print $5}' ${tmp} | paste -sd+ | bc))

    twofish_enc+=($(awk '/twofish-cbc/ && /256b/ {print $3}' ${tmp} | paste -sd+ | bc))
    twofish_dec+=($(awk '/twofish-cbc/ && /256b/ {print $5}' ${tmp} | paste -sd+ | bc))

    # print as results come in
    echo -n 'aes_enc '
    for result in ${aes_enc[@]}; do
        echo -n "$result "
    done; echo

    echo -n 'aes_dec '
    for result in ${aes_dec[@]}; do
        echo -n "$result "
    done; echo

    echo -n 'serpent_enc '
    for result in ${serpent_enc[@]}; do
        echo -n "$result "
    done; echo

    echo -n 'serpent_dec '
    for result in ${serpent_dec[@]}; do
        echo -n "$result "
    done; echo

    echo -n 'twofish_enc '
    for result in ${twofish_enc[@]}; do
        echo -n "$result "
    done; echo

    echo -n 'twofish_dec '
    for result in ${twofish_dec[@]}; do
        echo -n "$result "
    done; echo

    # clean the dmux output
    rm ${tmp}

done

# write the 