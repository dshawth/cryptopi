# Other SBCs

We also investigated the cryptographic performance of the other ARM-based SBC platforms after selecting the Raspberry 3 B+ for its popularity, wide community support, and inexpensiveness.

- The operating system (OS) options were limited in comparison to the Pi 3 B+.
- We chose the **officially supported** OS for each of our non-selected platforms.

For reference, our selected SBC platform, the Raspberry Pi 3B+, has the below performance on Ubuntu Core 18.04 with cryptsetup version 2.0.2 \*:

|         | AES  | Serpent | Twofish |
|---------|------|---------|---------|
| Encrypt | 51.0 | 28.0    | 41.5    |
| Decrypt | 59.8 | 30.0    | 44.4    |

*All results in MiB/s*

\* We chose Ubuntu Core 18.04 for our selected platform due to the availability of the cryptographic modules and compatibility with the Raspberry Pi 3B+.

## TinkerBoard

- Dist: TinkerOS
- Vers: v2.0.11
- Date: 2019/8/21
- Type: GUI

```bash4
sudo apt update && sudo apt dist-upgrade -y
sudo apt install cryptsetup -y
/sbin/cryptsetup benchmark
```

- Modules: AES
- Enc: 54.1 MiB/s
- Dec: 56.4 MiB/s

## Raspberry Pi 4B

- Dist: Raspbian Buster Lite
- Vers: February 2020
- Date: 2020/02/13
- Type: Term
- User: `pi`
- Pass: `raspberry`

```bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt install cryptsetup -y
cryptsetup benchmark
```

- Modules: AES
- Enc: 44.3 MiB/s
- Dec: 77.3 MiB/s

## BeagleBone Black (REV C)

- Dist: Debian
- Vers: 6.3.0
- Date: 10/05/2018
- Note: OS preinstalled
- User: `debian`
- Pass: `temppwd`

```bash
sudo apt update && sudo apt dist-upgrade -y # dist-upgrade hangs
cryptsetup benchmark
```

- Modules: AES, Serpent, Twofish
- Enc: 21.3 MiB/s, 16.3 MiB/s, 21.5 MiB/s
- Dec: 24.3 MiB/s, 18.9 MiB/s, 24.3 MiB/s

## Libre Computer Board (AML-S905X-CC)

- Dist: Ubuntu
- Vers: Libre 18.04
- Date: 2019-04-24
- Type: Term
- Note: Non-Canonical source
- User: `libre`
- Pass: `computer`

```bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt install cryptsetup -y
cryptsetup benchmark
```

- Modules: None
- Note: Oddly missing as part of all other 18.04 distributions; noted DES present.

## ODROID C2

- Dist: Ubuntu
- Vers: 18.04 Minimal
- Date: 2019-08-19
- Type: Term
- Note: Non-Canonical source
- User: `root`
- Pass: `odroid`

```bash
apt update && apt dist-upgrade -y
apt install cryptsetup -y
cryptsetup benchmark
```

- Modules: AES, Serpent, Twofish
- Enc: 46.9 MiB/s, 31.1 MiB/s, 46.4 MiB/s
- Dec: 50.0 MiB/s, 33.9 MiB/s, 51.0 MiB/s

## ODROID XU4

- Dist: [Ubuntu 18.04 Minimal DROID XU4 (20190911)](https://odroid.in/ubuntu_18.04lts/XU3_XU4_MC1_HC1_HC2/)
- Creds: `root` | `odroid`

```bash
apt update && apt dist-upgrade -y
apt install cryptsetup -y
reboot
cryptsetup benchmark | tee xu4_crypto_20200511.txt
```

| Algorithm   | Key  | Encryption | Decryption |
|-------------|------|------------|------------|
| aes-cbc     | 128b | 74.6       | 70.4       |
| serpent-cbc | 128b | 41.8       | 43.6       |
| twofish-cbc | 128b | 59.4       | 62.2       |
| aes-cbc     | 256b | 59.8       | 56.6       |
| serpent-cbc | 256b | 41.8       | 43.6       |
| twofish-cbc | 256b | 59.4       | 62.3       |

*All results in MiB/s*

[raw](xu4_crypto_20200511.txt)