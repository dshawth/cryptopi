import numpy as np
import matplotlib.pyplot as plt

#tick info
x = np.arange(10)
x_labels = [str(i) for i in range(2,22,2)]
fig,ax = plt.subplots()
#y_labels = ['0', '1', '10', '100','1000','10000']

#################### ENCRYPT DATA ##############################
######new run#######

###SERPENT
nuc_secrypt = 83.4 
hpc_secrypt = 0.0
pi_secrypt = [52.99, 109.49, 165.66, 221.78, 277.72, 333.67, 389.39, 445.48, 501.85, 555.92]

###TWOFISH data
nuc_tecrypt = 175.7
hpc_tecrypt = 0.0
pi_tecrypt = [78.67, 162.89, 246.2, 328.64, 411.93, 494.73, 577.22, 660.32, 743.47, 824.23]

###AES DATA
nuc_aecrypt = 750.9
hpc_aecrypt = 0.0
pi_aecrypt = [71.51, 148.29, 224.71, 300.1, 376.4, 452.16, 527.57, 603.79, 679.94, 753.58]

#####old run##########
###SERPENT
#nuc_secrypt = 86.13
#hpc_secrypt = 111.36
#pi_secrypt = [56.17, 111.62, 168.48, 224.59, 280.62, 336.64, 392.84, 449.11, 505.1, 561.6]

###TWOFISH data
#nuc_tecrypt = 194.8
#hpc_tecrypt = 246.34
#pi_tecrypt = [82.99, 165.03, 248.97, 331.89, 414.76, 497.75, 580.66, 663.68, 746.69, 830]

###AES DATA
#nuc_aecrypt = 793.78
#hpc_aecrypt = 1003.83
#pi_aecrypt = [75.94, 150.97, 227.83, 303.74, 379.59, 455.47, 531.44, 607.47, 683.48, 759.5]


######################## DECRYPT DATA #########################
###New run###

###SERPENT DATA
nuc_sdcrypt = 581.1
hpc_sdcrypt = 0.0
pi_sdcrypt = [56.94, 117.47, 177.78, 237.44, 297.69, 357.55, 417.43, 477.64, 538.07, 596.07]


###TWOFISH data
nuc_tdcrypt = 340.4
hpc_tdcrypt = 0.0
pi_tdcrypt = [84.24, 174.39, 263.29, 351.52, 440.33, 528.99, 616.92, 706.24, 795.29, 881.62]


###AES DATA
nuc_adcrypt = 2335.6 
hpc_adcrypt = 0.0
pi_adcrypt = [85.07, 176.64, 267.42, 357.07, 447.79, 538.5, 628.38, 719.12, 810.24, 897.66]


###old run###
###SERPENT DATA
nuc_sdcrypt = 643.16
hpc_sdcrypt = 841.36
pi_sdcrypt = [60.02, 119.32, 179.99, 240, 300.02, 359.98, 420.02, 480.01, 540.05, 600]



###TWOFISH data
nuc_tdcrypt = 355.39
hpc_tdcrypt = 453.17
pi_tdcrypt = [88.77, 176.60, 266.27, 354.98, 443.61, 532.34, 620.92, 709.83, 798.48, 887.4]


###AES DATA
nuc_adcrypt = 2520.06
hpc_adcrypt = 3171.71
pi_adcrypt = [90.44, 180.02, 271.26, 361.63, 451.98, 542.52, 632.83, 723.33, 813.69, 904.31]



#creates seperate plots for encrypt and decrypt --uncomment the one you need

#This part of file changes

#ax.set_ylim(0, 1100)
#ax.set_yscale('log')
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
#ax.set_yticklabels(y_labels)

box = ax.get_position()

handles, labels = plt.gca().get_legend_handles_labels()
order = [6,1,0,7,3,2,8,5,4]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],
bbox_to_anchor=(0., 1.02, 1., 0.2), loc='lower left', ncol=3,  mode="expand", borderaxespad=0.)
plt.subplots_adjust(top=0.8)

ax.set_ylim([0,3000])
#plt.xlim([0,x.size])
#plt.axis('tight')



plt.show()
