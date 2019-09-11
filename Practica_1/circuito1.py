import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

data = pd.read_csv("circuito1.csv")
simul = pd.read_csv("circuito1_sim.csv")

data['I'] = data['I'].apply(lambda x: x/100)
R = 2130 #Ohm

# slope, intercept, r_value, p_value, std_err = linregress(data['V'],data['I'])

coef, cov = np.polyfit(np.array(data["V"]), np.array(data["I"]), 1, cov=True)

x = np.linspace(0,20,100)

# plt.plot(x, slope*x + intercept, 'r')

# plt.errorbar(data['V'],data['I'], fmt=".",xerr = 0.01, yerr = 0.0001)
# plt.plot(simul['V(R1.nA)'],simul['I(R1.nA)'], 'b')


fig, ax = plt.subplots(nrows=1, ncols=2, sharey=True, figsize=(12,8))

# ax[0].plot(x, slope*x + intercept, '-k', linewidth=1)
ax[0].plot(x, coef[0]*x + coef[1], '-k', linewidth=1)
ax[1].plot(simul['V(R1.nA)'],simul['I(R1.nA)'], '-k', linewidth=1)

ax[0].set_ylabel("Current")
ax[0].text(0,0.006, r"$I = \left( {:.12f} \pm {:.12f} \right) \; V $".format(coef[0], cov[0,0]), fontsize=10)
ax[0].text(0.5,0.0057,r"$- \left( {:.10f} \pm {:.10f} \right)$".format(np.abs(coef[1]), cov[1,1]), fontsize=10)

for ax,name in zip(ax, ["Linear fit","Simulation"]):
    ax.errorbar(data['V'],data['I'], fmt=".", color="black",xerr = 0.01, yerr = 0.0001)
    ax.set_xlim(0,20)
    # ax.set_ylim(0,0.006)

    ax.set_title(name)

    ax.set_xlabel("Voltage")


plt.show()

fig.savefig("circuito1_plot.png",format="png")
