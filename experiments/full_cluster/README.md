# Full Cluster

- Contains 20 Raspberry Pi 3 B+
- Currently on `EECSNet` subnet `TH113` at `172.31.42.1-20`
- `.20` is the master node
- Based on the `ubuntu-18.04.4-preinstalled-server-arm64+raspi3.img.xz` ISO **NEED TO CONFIRM THAT THIS IS CURRENT**
- `ubuntu` / `ubuntu` -> `ubuntu1234`

## Hardware

- 20x: Raspberry Pi 3 B+
- Custom based on the 750 Watt Corsair ATX
- Netgear 24-Port Switch (**GET MODEL**)
- Tripplite Industrial Surge Protector (0.3 Watts?!)
- Kill-a-watt

## Experiment

- Date: 4/27/2020
- Desc: Cluster Idle breakdown
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