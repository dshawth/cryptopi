import numpy as np
import matplotlib.pyplot as plt

#tick info
x = np.arange(10)
x_labels = [str(i) for i in range(2,22,2)]
fig,ax = plt.subplots()


#################### ENCRYPT DATA ##############################

###SERPENT
nuc_serpent_encrypt = 79.2 
mrd_serpent_encrypt = 100.8
pi_serpent_encrypt = [52.54, 108.9, 165.15, 220.79, 276.91, 332.91, 388.33, 444.91, 501.04, 554.09]


###TWOFISH data
nuc_twofish_encrypt = 182.3
mrd_twofish_encrypt = 194.8
pi_twofish_encrypt = [78.03, 161.88, 245.24, 327.55, 410.9, 493.95, 576.59, 659.61, 743.01, 823.11]


###AES DATA
nuc_aes_encrypt = 977.0
mrd_aes_encrypt = 1167.2
pi_aes_encrypt = [95.26, 197.74, 299.99, 401.5, 503.73, 602.6, 703.38, 806.23, 909.04, 1007.0]

ax.set_ylabel('MiB/s')
ax.set_xlabel('Number of Pis')

bar_width=0.2

ax.bar(x, pi_serpent_encrypt, bar_width, color='c', label="Pi Serpent")
plt.axhline(y=mrd_serpent_encrypt, color='c', linestyle='-', label="MRD Serpent", linewidth=2)
plt.axhline(y=nuc_serpent_encrypt, color='c', linestyle='--', label="NUC Serpent", linewidth=2)

ax.bar(x+bar_width, pi_aes_encrypt, bar_width, color='k', label="Pi AES")
plt.axhline(y=mrd_aes_encrypt, color='k', linestyle='-', label="MRD AES", linewidth=2)
plt.axhline(y=nuc_aes_encrypt, color='k', linestyle='--', label="NUC AES", linewidth=2)

ax.bar(x+bar_width+bar_width, pi_twofish_encrypt, bar_width, color='g', label="Pi Twofish")
plt.axhline(y=mrd_twofish_encrypt, color='g', linestyle='-', label="MRD Twofish", linewidth=2)
plt.axhline(y=nuc_twofish_encrypt, color='g', linestyle='--', label="NUC Twofish", linewidth=2)


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

