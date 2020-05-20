# Scripts

## dmux

The dmux script allows simple execution of shell commands on each node in the cluster. It collects the results and writes them to a file.

Usage:

```bash
./dmux.sh COMMAND [OUTFILE]
```

Some useful commands using dmux:

```bash
# shutdown all nodes
./dmux.sh "sudo shutdown -t 1" /dev/null

# reboot all
./dmux.sh "sudo shutdown -r -t 1" /dev/null

# crypto benchmark
./dmux.sh "cryptsetup benchmark" crypto-results2

# disable governer
./dmux.sh "sudo echo performance | sudo tee /sys/devices/system/cpu/cpu0/cpufreq/scaling_governor"
```


## other

```bash
# hosts alive
nmap -sn 172.31.42.1-20
```