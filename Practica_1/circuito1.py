import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import linfit as lfit

data = pd.read_csv("circuito1.csv")
simul = pd.read_csv("circuito1_sim.csv")

data['I'] = data['I'].apply(lambda x: x/100)
R = 2130 #Ohm
errI = np.full_like(data['I'],0.01e-3)

# slope, intercept, r_value, p_value, std_err = linregress(data['V'],data['I'])

# coef, cov = np.polyfit(np.array(data["V"]), np.array(data["I"]), 1, w = 1/errI,cov=True)


# R_ajust = 1/coef[0]
# dR_ajust = (1/coef[0]**2)*cov[0,0]
# x = np.linspace(0,20,100)


# fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12,8))


# ax[0].plot(x, coef[0]*x + coef[1], '-k', linewidth=1, color = 'b')
# ax[1].plot(simul['V(R1.nA)'],simul['I(R1.nA)'], '-k', linewidth=1, color = 'r')


# ax[0].set_ylabel("Current (A)")
# ax[0].text(0.5,0.008, r"$I = 1/{} \pm {} V$" "\n" r"$\ \ \ \ - \left( {:.10f} \pm {:.10f} \right) $".format(R_ajust, dR_ajust, np.abs(coef[1]), cov[1,1]),fontsize = 10,bbox=dict(facecolor = 'white',  alpha=0.5))

# ax[0].text(1.5,0.00, r"$Resistance Value: {} \pm {}$".format(1/coef[0], 1/coef[0]**2 * cov[0,0]))

# ax[1].text(0.5,0.008, r"$I = \frac{1}{2130 \Omega} V$",fontsize = 12,bbox=dict(facecolor = 'white',  alpha=0.5))

# for ax,name in zip(ax, ["Linear fit","Simulation"]):
#     ax.errorbar(data['V'],data['I'], fmt=".", color="black",xerr = 0.01, yerr = 0.0001)
#     ax.set_xlim(0,20)
#     # ax.set_ylim(0,0.006)

#     ax.set_title(name)

#     ax.set_xlabel("Voltage (V)")

ax, fig = lfit.fit_n_plot(np.array(data["I"]), np.array(data["V"]), 0.0001, 0.01, False, "I", "V")

plt.show()

fig.savefig("circuit1_plot_intcero.png",format="png")


