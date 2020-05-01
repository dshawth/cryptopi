# Full Cluster

- Contains 20 Raspberry Pi 3 B+
- Currently on `EECSNet` subnet `TH113` via `pi-gate` at `10.13.0.1` at `172.31.42.1-20`
- `.20` is the master node
- Based on the `ubuntu-18.04.4-preinstalled-server-arm64+raspi3.img.xz` ISO **NEED TO CONFIRM THAT THIS IS CURRENT**
- `ubuntu` / `ubuntu` -> `ubuntu1234`

## Hardware

- 20x: Raspberry Pi 3 B+
- Custom based on the 750 Watt Corsair ATX
- Netgear 24-Port Switch JGS525
- Tripplite Industrial Surge Protector (0.3 Watts?!)
- Kill-a-watt

## Experiment

- Date: 04/27/2020
- Desc: Cluster idle breakdown
- Note: Kill-a-watt moved around as required
- Note: Surge protector draw NOT included in the below table
- Note: Pi Gate still hangs the rack console resulting in incomplete experiment

## Results

| Hardware | Idle |
|----------|------|
| Switch   | 7.0  |
| Cluster  | 61.5 |
| Both     | 71.5 |

## Notes:

1. All power is in Watts.
2. Idle readings fluctuated between 3 values (EG 6.6, 6.7, 6.8); rough center value always used; expected resulting precision `+/- 1.0`.
3. Incongruence noted, the cluster alone measurement was taken with the switch unplugged; it is expected that the connectivity consumed the additional `~3.0` Watts with both the Switch and Cluster contributing to said power consumption.
4. At the low end, the custom PSU in conjunction with the BitScope Blade is less efficient that the standard USB power supplies used in the mini cluster. The efficiency slope of the ATX PSU and the additional power regulation found in the BitScope Blade support this finding. The expected utilization with individual power supplies is `49` Watts at idle, our setup is almost exactly `25%` less efficient.

## Experiment

- Date: 05/01/2020
- Desc: Cluster crypto benchmark power
- Note: Surge protector draw and switch draw are included in the below results:

| Run | Peak |
|-----|------|
| 1   | 144  |
| 2   | 140  |
| 3   | 135  |
| 4   | 136  |
| 5   | 139  |
| 6   | 137  |
| 7   | 136  |
| 8   | 138  |
| 9   | 138  |
| 10  | 137  |

- Mean:  138
- StDev: 2.58

## Notes:

1. All power is in Watts.
2. Bench reading fluctuated much more, making the middle reading infeasible to capture, the peak readings are recorded instead. Although the readings varied more, they are repeatable as seen above.
3. Based on the mini-cluster using traditional Raspberry Pi power supplies, the expected utilization is `121` Watts peak during the crypto benchmarks. As Note 4 in the previous experiment details, our efficiency is `14%` less efficient, however, as the ATX PSU documentation indicates, it expectedly gained efficiency as it approached the middle of it's rated power delivery range.