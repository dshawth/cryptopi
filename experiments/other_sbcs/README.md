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

## TinkerBoard (Rev 1.2)

- Dist: [TinkerOS Debian v2.0.11 (20190821)](https://tinkerboarding.co.uk/wiki/index.php/TinkerOS)
- Creds: `linaro` | `linaro`

```bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt install cryptsetup -y
sudo reboot
/sbin/cryptsetup benchmark
```

| Algorithm | Key  | Encryption | Decryption |
|-----------|------|------------|------------|
| aes-cbc   | 128b | 54.7       | 57.0       |
| aes-cbc   | 256b | 41.6       | 43.7       |

- *Results in MiB/s*
- [raw](tinker_crypto_20200512.txt)

## Raspberry Pi 4B

- Dist: Raspbian Buster Lite
- Vers: February 2020
- Date: 2020/02/13
- Type: Term
- Creds: `pi` | `raspberry`

```bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt install cryptsetup -y
sudo reboot
cryptsetup benchmark | tee pi4_crypto_20200512.txt
```

| Algorithm | Key  | Encryption | Decryption |
|-----------|------|------------|------------|
| aes-cbc   | 128b | 44.6       | 77.2       |
| aes-cbc   | 256b | 36.8       | 58.4       |

- *Results in MiB/s*
- [raw](pi4_crypto_20200512.txt)

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

- Dist: [Libre Ubuntu Bionic Headless (20190624)](http://share.loverpi.com/board/libre-computer-project/libre-computer-board-aml-s905x-cc/image/ubuntu/)
- Creds: `libre` | `computer`

```bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt install cryptsetup -y
sudo reboot
cryptsetup benchmark | tee libre_crypto_20200512.txt
```

| Algorithm | Key  | Encryption | Decryption |
|-----------|------|------------|------------|

- No modules, no results, oddly absent as normally part of 18.04; noted DES present.
- *Results in MiB/s*
- [raw](libre_crypto_20200512.txt)

## ODROID C2

- Dist: [Ubuntu 18.04 Minimal ODROID C2 (20190819)](https://odroid.in/ubuntu_18.04lts/C2/)
- Creds: `root` | `odroid`

```bash
apt update && apt dist-upgrade -y
apt install cryptsetup -y
reboot
cryptsetup benchmark | tee c2_crypto_20200511.txt
```

| Algorithm   | Key  | Encryption | Decryption |
|-------------|------|------------|------------|
| aes-cbc     | 128b | 45.6       | 48.4       |
| serpent-cbc | 128b | 30.1       | 32.9       |
| twofish-cbc | 128b | 46.8       | 51.3       |
| aes-cbc     | 256b | 38.1       | 39.3       |
| serpent-cbc | 256b | 31.9       | 34.1       |
| twofish-cbc | 256b | 47.7       | 51.3       |

- *Results in MiB/s*
- [raw](c2_crypto_20200511.txt)

## ODROID XU4

- Dist: [Ubuntu 18.04 Minimal ODROID XU4 (20190911)](https://odroid.in/ubuntu_18.04lts/XU3_XU4_MC1_HC1_HC2/)
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

- *Results in MiB/s*
- [raw](xu4_crypto_20200511.txt)
