# General and Cryptography Benchmarks on Raspberry Pi Clusters

The cluster consists of 20 Raspberry Pi 3 B+ single board computers (SBCs) with an extra two Raspberry Pi 3 B+ SBCs for the gateway and power monitoring.

**This repo is being moved over from the private GitLab.**

## Physical Nodes

When looking at the front (blue side).

|    |    |    |    |    |    |    |    |    |     |
|  - |  - |  - |  - |  - |  - |  - |  - |  - |  -  |
|  1 |  2 |  3 |  4 |  5 |  6 |  7 |  8 |  9 | 10  |
| 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20* |
|    |    |    |    |    |    |    |    |    |     |

- node numbers correspond to the last octet in **`172.31.42.X`**
- \* master
- gateway is currently at **`10.13.19.1`**

## Host Names

- `master`
- `worker1`, `worker2`, ...

