# Mini Cluster

- Contains 2-6 Pis
- Currently on `HawthNet` subnet `MAIN` at `172.16.0.11-16`
- `.11` is the master node
- Based on the `ubuntu-18.04.4-preinstalled-server-arm64+raspi3.img.xz` ISO
- `ubuntu` / `ubuntu` -> `ubuntu1234`

## Hardware

- 2x, 4x, 6x: Raspberry Pi 3 B+
- Standard USB Power Supplies
- 1x ASUS Switch (GX-D1081)
- Tripplite Industrial Surge Protector (0.3 Watts?!)
- Kill-a-watt

## Experiment

- Date: 4/19/2020
- Desc: 0/2/4/6 with and without switch
- Note: Kill-a-watt moved around as required
- Note: USB power supplies unplugged when not in use (makes a difference)
- Note: Benchmark results taken twice
- Note: Surge protector draw NOT included in the below table

```bash
sshpass -p ubuntu1234 ssh-copy-id ubuntu@172.16.0.1$a # in a loop
./dmux.sh ubuntu 172.16.0.11-16 'cryptsetup benchmark' # adjust 11-16 as required for the different tests
```

## Results

| Hardware        | Idle   | Bench     |
|-----------------|--------|-----------|
| Switch          | `1.4`  | `1.5` \+  |
| 2x Pis          | `4.9`  | `12.1`    |
| Switch + 2x Pis | `6.5`  | `13.7`    |
| 4x Pis          | `9.7`  | `24.1`    |
| Switch + 4x Pis | `11.4` | `25.9` \* |
| 6x Pis          | `14.6` | `36.2`    |
| Switch + 6x Pis | `16.3` | `37.9` \* |

### Notes:

1. All power is in Watts.
2. Idle readings fluctuated between 3 values (EG 6.6, 6.7, 6.8); center value always used; expected resulting precision `+/- 0.1`. The with and without switch were all in the expected range of `+/- 0.1` based on the switch alone.
3. Bench reading fluctuated much more, making the middle reading infeasible to capture, the peak readings are recorded instead. Although the readings varied more, they are repeatable.
4. \+ Incongruence noted, the benchmark that resulted in this value had only 2x Pis.
4. \* Switch appears to draw slightly more than power here.