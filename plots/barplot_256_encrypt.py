import numpy as np
import matplotlib.pyplot as plt

#tick info
x = np.arange(10)
x_labels = [str(i) for i in range(2,22,2)]
fig,ax = plt.subplots()
#y_labels = ['0', '1', '10', '100','1000','10000']

#################### ENCRYPT DATA ##############################

###SERPENT
nuc_secrypt = 83.4 
hpc_secrypt = 102.5
pi_secrypt = [52.99, 109.49, 165.66, 221.78, 277.72, 333.67, 389.39, 445.48, 501.85, 555.92]


###TWOFISH data
nuc_tecrypt = 175.7
hpc_tecrypt = 193.1
pi_tecrypt = [78.67, 162.89, 245.24, 328.64, 411.93, 494.73, 577.22, 660.32, 743.47, 824.23]


###AES DATA
nuc_aecrypt = 750.9
hpc_aecrypt = 854.7
pi_aecrypt = [71.51, 148.29, 224.71, 300.1, 376.4, 452.16, 527.57, 603.79, 679.94, 753.58]



ax.set_ylabel('MiB/s')
ax.set_xlabel('Number of Pis')

bar_width=0.2

ax.bar(x, pi_aecrypt, bar_width, color='c', label="Pi Serpent")


plt.axhline(y=hpc_secrypt, color='c', linestyle='-', label="MRD Serpent", linewidth=2)
plt.axhline(y=nuc_secrypt, color='c', linestyle='--', label="NUC Serpent", linewidth=2)

ax.bar(x+bar_width, pi_aecrypt, bar_width, color='k', label="Pi AES")
plt.axhline(y=hpc_aecrypt, color='k', linestyle='-', label="MRD AES", linewidth=2)
plt.axhline(y=nuc_aecrypt, color='k', linestyle='--', label="NUC AES", linewidth=2)

ax.bar(x+bar_width+bar_width, pi_tecrypt, bar_width, color='g', label="Pi Twofish")
plt.axhline(y=hpc_tecrypt, color='g', linestyle='-', label="MRD Twofish", linewidth=2)
plt.axhline(y=nuc_tecrypt, color='g', linestyle='--', label="NUC Twofish", linewidth=2)


ax.set_xticks(x)
ax.set_xticklabels(x_labels)

box = ax.get_position()

handles, labels = plt.gca().get_legend_handles_labels()
order = [6,1,0,7,3,2,8,5,4]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],
bbox_to_anchor=(0., 1.02, 1., 0.2), loc='lower left', ncol=3,  mode="expand", borderaxespad=0.)
plt.subplots_adjust(top=0.8)

ax.set_ylim([0,1500])

plt.show()
