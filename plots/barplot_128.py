"""
=============================
New plots (transforming Ray's plots to Python)
=============================
"""

import numpy as np
import matplotlib.pyplot as plt

#tick info
x = np.arange(10)
x_labels = [str(i) for i in range(2,22,2)]
fig,ax = plt.subplots()


#################### ENCRYPT DATA ##############################

###SERPENT
nuc_secrypt = 79.2 
hpc_secrypt = 100.8
pi_secrypt = [52.54, 108.9, 165.15, 220.79, 276.91, 332.91, 388.33, 444.91, 501.85, 554.09]

###TWOFISH data
nuc_tecrypt = 182.3
hpc_tecrypt = 194.8
pi_tecrypt = [78.03, 161.88, 245.24, 327.55, 410.9, 493.95, 576.59, 659.61, 743.01, 823.11]

###AES DATA
nuc_aecrypt = 977.0
hpc_aecrypt = 1167.2
pi_aecrypt = [95.26, 197.74, 299.99, 401.5, 503.73, 602.6, 703.38, 806.23, 909.04, 1007.0]



######################## DECRYPT DATA #########################

###SERPENT
#nuc_secrypt =  610.5 
#hpc_secrypt = 360.6
#pi_secrypt = [56.36, 116.87, 177.2, 236.77, 297.08, 357.06, 416.78, 477.14, 537.23,594.79]

###TWOFISH data
#nuc_tecrypt = 341.1
#hpc_tecrypt = 386.6 
#pi_tecrypt = [83.62, 173.32, 262.44, 350.58, 439.68, 528.52, 616.56, 705.74, 794.89, 880.6]

###AES DATA
#nuc_aecrypt =  2889.1
#hpc_aecrypt = 3663.1
#pi_aecrypt = [112.01, 232.32, 352.67, 471.62, 591.98, 710.41,  827.78, 949.13, 1069.88, 1183.05]


#creates seperate plots for encrypt and decrypt --uncomment the one you need

#This part of file changes

ax.set_ylabel('MiB/s')
ax.set_xlabel('Number of Pis')

bar_width=0.2

ax.bar(x, pi_secrypt, bar_width, color='c', label="Pi Serpent")
plt.axhline(y=hpc_secrypt, color='c', linestyle='-', label="HEDT Serpent", linewidth=2)
plt.axhline(y=nuc_secrypt, color='c', linestyle='--', label="NUC Serpent", linewidth=2)

ax.bar(x+bar_width, pi_aecrypt, bar_width, color='k', label="Pi AES")
plt.axhline(y=hpc_aecrypt, color='k', linestyle='-', label="HEDT AES", linewidth=2)
plt.axhline(y=nuc_aecrypt, color='k', linestyle='--', label="NUC AES", linewidth=2)

ax.bar(x+bar_width+bar_width, pi_tecrypt, bar_width, color='g', label="Pi Twofish")
plt.axhline(y=hpc_tecrypt, color='g', linestyle='-', label="HEDT Twofish", linewidth=2)
plt.axhline(y=nuc_tecrypt, color='g', linestyle='--', label="NUC Twofish", linewidth=2)


ax.set_xticks(x)
ax.set_xticklabels(x_labels)

box = ax.get_position()

handles, labels = plt.gca().get_legend_handles_labels()
order = [6,1,0,7,3,2,8,5,4]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],
bbox_to_anchor=(0., 1.02, 1., 0.2), loc='lower left', ncol=3,  mode="expand", borderaxespad=0.)
plt.subplots_adjust(top=0.8)

ax.set_ylim([0,2000])



plt.show()
