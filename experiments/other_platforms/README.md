# Other Platforms

We also investigated the performance of the other ARM-based SBC platforms listed below:

- ODROID-XU4
- BeagleBone Black
- Libre Computer Board
- Tinker Board ??

The operating system (OS) options were limited in comparison to the Pi.
We chose the most supported OS for each at the time and ran the `cryptsetup benchmark`.
We found that none had hardware AES instructions and most did not include the Serpent or Twofish kernel modules.

**TODO rerun these**