"""
=============================
New plots (For power)
=============================
"""

import numpy as np
import matplotlib.pyplot as plt

#tick info
x = np.arange(10)
x_labels = [str(i) for i in range(2,22,2)]
fig,ax = plt.subplots()

### Power measurements (peak only, in Watts)
nuc_power = 42
MRD_power = 73.5
pi_power = [40, 51, 62, 72, 85, 96, 110, 125, 139,149]

#updated pi_power to include switch
pi_power = [i+10.5 for i in pi_power]

#new bars
pi_eff = [16.4, 27.5, 37.6]

mini_cluster = [13.7, 25.9, 37.9, 0, 0, 0, 0, 0, 0, 0]



ax.set_ylabel('Watts')
ax.set_xlabel('Number of Pis')

bar_width=0.2

cselect='lightslategray'

ax.bar(x, pi_power, bar_width, color=cselect, label="BitScope Blade Cluster")
ax.bar(x+bar_width, mini_cluster, bar_width, color='limegreen', label="Green cluster")
plt.axhline(y=MRD_power, color=cselect, linestyle='-', label="MRD", linewidth=2)
plt.axhline(y=nuc_power, color=cselect, linestyle='--', label="NUC", linewidth=2)

ax.set_xticks(x)
ax.set_xticklabels(x_labels)

#box = ax.get_position()
#handles, labels = plt.gca().get_legend_handles_labels()
#order = [6,1,0,7,3,2,8,5,4]

ax.legend(bbox_to_anchor=(0., 1.02, 1., 0.2), loc='lower left', mode="expand", borderaxespad=0., ncol=3)


#ax.legend([handles[idx] for idx in order],[labels[idx] for idx in order],
#bbox_to_anchor=(0., 1.02, 1., 0.2), loc='lower left', ncol=3,  mode="expand", borderaxespad=0.)
plt.subplots_adjust(top=0.8)

#plt.xlim([0,x.size])
plt.axis('tight')



plt.show()
