import numpy as np
import matplotlib.pyplot as plt

#tick info
x = np.arange(10)
x_labels = [str(i) for i in range(2,22,2)]
fig,ax = plt.subplots()

######################## DECRYPT DATA #########################

###SERPENT DATA
nuc_serpent_decrypt = 581.1
mrd_serpent_decrypt = 374.3 
pi_serpent_decrypt = [56.94, 117.47, 177.78, 237.44, 297.69, 357.55, 417.43, 477.64, 538.07, 596.07]


###TWOFISH data
nuc_twofish_decrypt = 340.4
mrd_twofish_decrypt = 378.7
pi_twofish_decrypt = [84.24, 174.39, 263.29, 351.52, 440.33, 528.99, 616.92, 706.24, 795.29, 881.62]


###AES DATA
nuc_aes_encrypt = 2335.6 
mrd_aes_encrypt =  3164.7
pi_aes_encrypt = [85.07, 176.64, 267.42, 357.07, 447.79, 538.5, 628.38, 719.12, 810.24, 897.66]


ax.set_ylabel('MiB/s')
ax.set_xlabel('Number of Pis')

bar_width=0.2

ax.bar(x, pi_serpent_decrypt, bar_width, color='c', label="Pi Serpent")
plt.axhline(y=mrd_serpent_decrypt, color='c', linestyle='-', label="MRD Serpent", linewidth=2)
plt.axhline(y=nuc_serpent_decrypt, color='c', linestyle='--', label="NUC Serpent", linewidth=2)

ax.bar(x+bar_width, pi_aes_encrypt, bar_width, color='k', label="Pi AES")
plt.axhline(y=mrd_aes_encrypt, color='k', linestyle='-', label="MRD AES", linewidth=2)
plt.axhline(y=nuc_aes_encrypt, color='k', linestyle='--', label="NUC AES", linewidth=2)

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
