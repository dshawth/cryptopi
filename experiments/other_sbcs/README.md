# Other SBCs

We also investigated the cryptographic performance of the other ARM-based SBC platforms after selecting the Raspberry 3 B+ for its popularity, wide community support, and inexpensiveness.

- The operating system (OS) options were limited in comparison to the Pi 3 B+.
- We chose the **officially supported** OS for each of our non-selected platforms.

For reference, our selected SBC platform, the Raspberry Pi 3B+, has the below performance on Ubuntu Core 18.04 with cryptsetup version 2.0.2 \*:

| Algorithm   | Key  | Encryption | Decryption |
|-------------|------|------------|------------|
| aes-cbc     | 128b | 47.3       | 57.6       |
| serpent-cbc | 128b | 26.4       | 29.5       |
| twofish-cbc | 128b | 38.5       | 43.2       |
| aes-cbc     | 256b | 37.2       | 43.9       |
| serpent-cbc | 256b | 27.5       | 29.6       |
| twofish-cbc | 256b | 40.5       | 43.3       |

- *Results in MiB/s*
- [raw](pi3_crypto_20200513.txt)

\* We chose Ubuntu Core 18.04 for our selected platform due to the availability of the cryptographic modules and compatibility with the Raspberry Pi 3B+.

## BeagleBone Black (REV C)

- Dist: [Debian Buster IoT 10.3 (20200406)](https://beagleboard.org/latest-images)
- Creds: `debian` | `temppwd`
- Note: booting to SD card requires boot button.

```bash
sudo apt update && sudo apt dist-upgrade -y
sudo apt install cryptsetup -y
sudo reboot
cryptsetup benchmark | tee beagle_crypto_20200513.txt
```

| Algorithm   | Key  | Encryption | Decryption |
|-------------|------|------------|------------|
| aes-cbc     | 128b | 24.5       | 28.0       |
| serpent-cbc | 128b | 16.0       | 18.8       |
| twofish-cbc | 128b | 20.8       | 24.1       |
| aes-cbc     | 256b | 27.0       | 26.9       |
| serpent-cbc | 256b | 17.3       | 18.7       |
| twofish-cbc | 256b | 22.8       | 24.2       |

- *Results in MiB/s*
- [raw](beagle_crypto_20200513.txt)

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