import numpy as np
import matplotlib.pyplot as plt

#tick info
x = np.arange(10)
x_labels = [str(i) for i in range(2,22,2)]
fig,ax = plt.subplots()

######################## DECRYPT DATA #########################

###SERPENT
nuc_serpent_decrypt =  610.5 
mrd_serpent_decrypt = 360.6
pi_serpent_decrypt = [56.36, 116.87, 177.2, 236.77, 297.08, 357.06, 416.78, 477.14, 537.23,594.79]


###TWOFISH data
nuc_twofish_decrypt = 341.1
mrd_twofish_decrypt = 386.6 
pi_twofish_decrypt = [83.62, 173.32, 262.44, 350.58, 439.68, 528.52, 616.56, 705.74, 794.89, 880.6]


###AES DATA
nuc_aes_decrypt =  2889.1
mrd_aes_decrypt = 3663.1
pi_aes_decrypt = [112.01, 232.32, 352.67, 471.62, 591.98, 710.41,  827.78, 949.13, 1069.88, 1183.05]



ax.set_ylabel('MiB/s')
ax.set_xlabel('Number of Pis')

bar_width=0.2

ax.bar(x, pi_serpent_decrypt, bar_width, color='c', label="Pi Serpent")
plt.axhline(y=mrd_serpent_decrypt, color='c', linestyle='-', label="MRD Serpent", linewidth=2)
plt.axhline(y=nuc_serpent_decrypt, color='c', linestyle='--', label="NUC Serpent", linewidth=2)

ax.bar(x+bar_width, pi_aes_decrypt, bar_width, color='k', label="Pi AES")
plt.axhline(y=mrd_aes_decrypt, color='k', linestyle='-', label="MRD AES", linewidth=2)
plt.axhline(y=nuc_aes_decrypt, color='k', linestyle='--', label="NUC AES", linewidth=2)

ax.bar(x+bar_width+bar_width, pi_twofish_decrypt, bar_width, color='g', label="Pi Twofish")
plt.axhline(y=mrd_twofish_decrypt, color='g', linestyle='-', label="MRD Twofish", linewidth=2)
plt.axhline(y=nuc_twofish_decrypt, color='g', linestyle='--', label="NUC Twofish", linewidth=2)


ax.set_xticks(x)
ax.set_xticklabels(x_labels)

box = ax.get_position()

handles, labels = plt.gca().get_legend_handles_labels()
order = [6,1,0,7,3,2,8,5,4]
ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],
bbox_to_anchor=(0., 1.02, 1., 0.2), loc='lower left', ncol=3,  mode="expand", borderaxespad=0.)
plt.subplots_adjust(top=0.8)

ax.set_ylim([0,4000])

plt.show()
