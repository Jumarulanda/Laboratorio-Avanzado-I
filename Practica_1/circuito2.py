import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

import linfit as lfit


data = pd.read_csv("circuito2.csv")
simul = pd.read_csv("circuito2_sim.csv")

data['I'] = data['I'].apply(lambda x: x/1000)
R = 2130 #Ohm

# slope, intercept, r_value, p_value, std_err = linregress(data['V'],data['I'])

# coef, cov = np.polyfit(np.array(data["V"]), np.array(data["I"]), 1, cov=True)


# x = np.linspace(0,20,100)
# fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12,8))

# ax[0].plot(x, slope*x + intercept, '-k', linewidth=1)
# ax[0].plot(x, coef[0]*x + coef[1], '-k', linewidth=1, color = 'b')
# ax[1].plot(simul['V(R1.nA)'],simul['I(R1.nA)'], '-k', linewidth=1, color = 'r')

# ax[0].set_ylabel("Current")
# ax[0].text(5,0.004, r"$I = \left( {:.12f} \pm {:.12f} \right) \; V $" "\n" r"$- \left( {:.10f} \pm {:.10f} \right)$".format(coef[0], cov[0,0], coef[0], cov[1,1]), fontsize=10)

# for ax,name in zip(ax, ["Linear fit","Simulation"]):
#     ax.errorbar(data['V'],data['I'], fmt=".", color="black",xerr = 0.01, yerr = 0.0001)
#     ax.set_xlim(0,20)
#     ax.set_ylim(0,0.006)

#     ax.set_title(name)

#     ax.set_xlabel("Voltage")


# plt.show()

ax, fig = lfit.fit_n_plot(np.array(data["I"]), np.array(data["V"]), 0.0001, 0.01, False, "I", "V")

plt.show()

fig.savefig("cirucuit2_plot_intcero.png", format="png")


