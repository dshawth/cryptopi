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

### HPL measurements
nuc_hpl = 16.51
MRD_hpl = 20.48
pi_hpl = [6.38, 11.46, 15.72, 19.73, 23.26, 26.51, 30.4, 34.1, 38.3, 44.13]


#This part of file changes

ax.set_ylabel('GFLOPS') #uncomment for HPL
ax.set_xlabel('Number of Pis')


bar_width=0.2

cselect='lightslategray'

ax.bar(x, pi_hpl, bar_width, color=cselect, label="Bitscope Blade Cluster")
#ax.bar(x+.2, mini_cluster, bar_width, color=cselect2, label="Mini Cluster")
plt.axhline(y=MRD_hpl, color=cselect, linestyle='-', label="MRD", linewidth=2)
plt.axhline(y=nuc_hpl, color=cselect, linestyle='--', label="NUC", linewidth=2)

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
