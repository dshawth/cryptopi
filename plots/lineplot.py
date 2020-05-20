"""
=============================
Demo of the errorbar function
=============================

This exhibits the most basic use of the error bar method.
In this case, constant values are provided for the error
in both the x- and y-directions.
"""

import numpy as np
import matplotlib.pyplot as plt

#tick info
x = np.arange(10)
x_labels = [str(i) for i in range(2,22,2)]
fig,ax = plt.subplots()

#creates seperate plots for serpent and twofish --uncomment out the version
#you need

#####SERPENT DATA
#NUC Data
nuc_encrypt = [86.13]* 10
nuc_decrypt = [643.16]*10

#HPC system
hpc_encrypt = [111.36]*10
hpc_decrypt = [841.36]*10

#Pi data
encrypt = [56.17, 111.62, 168.48, 224.59, 280.62, 336.64, 392.84, 449.11, 505.1, 561.6]
decrypt = [60.02, 119.32, 179.99, 240, 300.02, 359.98, 420.02, 480.01, 540.05, 600]
#ax.set_title('Serpent Results')


'''
###TWOFISH data

#NUC
nuc_encrypt = [194.8]* 10
nuc_decrypt = [355.39]*10

#HPC
hpc_encrypt = [246.34]*10
hpc_decrypt = [453.17]*10

#Pi data
encrypt = [82.99, 165.03, 248.97, 331.89, 414.76, 497.75, 580.66, 663.68, 746.69, 830]
decrypt = [88.77, 176.60, 266.27, 354.98, 443.61, 532.34, 620.92, 709.83, 798.48, 887.4]
#ax.set_title('Twofish Results')
'''

#This part of file doesn't change
ax.set_ylim(0,900)
ax.set_ylabel('Mb/s')
ax.set_xlabel('Number of Pis')
ax.plot(x, hpc_encrypt, '-r', label="HPC encrypt")
ax.plot(x, hpc_decrypt, '--r', label="HPC decrypt")
ax.plot(x, nuc_encrypt, '-k', label="NUC encrypt")
ax.plot(x, nuc_decrypt, '--k', label="NUC decrypt")
ax.plot(x, encrypt, '-b', label="Pi encrypt")
ax.plot(x, decrypt, '--b', label="Pi decrypt")
ax.set_xticks(x)
ax.set_xticklabels(x_labels)
ax.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left',
           ncol=3, mode="expand", borderaxespad=0.)
plt.show()
